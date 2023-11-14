from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)

# Set a secret key for session security
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['UPLOAD_FOLDER'] = 'static'
app.config['ALLOWED_EXTENSIONS'] = {'mp4', 'avi', 'mkv', 'mov', 'flv', 'jpg', 'png', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

data = {
    'paragraph': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
    'option': 'None',  # or 'video'
    'anger_percent': 0,
    'happiness_percent': 0,
    'sadness_percent': 0,
    'surprise_percent': 0,
}

@app.route('/')
def index():
    # You can replace these values with your actual data
    selected_option = request.args.get('selected_option', 'None')
    link = request.args.get('link', '')
    return render_template('index.html',**data)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part', 'error')
        return redirect(request.url)

    file = request.files['file']
    selected_option = request.form.get('selected_option')
    link = request.form.get('link')

    if file.filename == '':
        flash('No selected file', 'error')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
        if selected_option == 'image':
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], "image.jpg"))
            option = 'image'
        else:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], "video.mp4"))
            option = 'video'
        flash('File uploaded successfully!', 'success')

        data = {
                    'paragraph': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
                    'option': option,  # or 'video'
                    'anger_percent': 0,
                    'happiness_percent': 0,
                    'sadness_percent': 0,
                    'surprise_percent': 0,
                    'selected_option' : option,
                    'link' : link
                }

        return render_template("index.html",**data)
    else:
        flash('Invalid file format', 'error')
        return redirect(url_for('index', option=selected_option,selected_option=selected_option, link=link))

if __name__ == '__main__':
    app.run(debug=True)
