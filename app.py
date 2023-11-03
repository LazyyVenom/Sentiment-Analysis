from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from sentiAnalysis import convert_video_to_wav

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'file_upload_app/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'mp4'}
app.config['SECRET_KEY'] = 'your_secret_key_here'  

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

paragraph = "This will contain a summary kind of thing."
anger_percent = 0
happiness_percent = 0
sadness_percent = 100
surprise_percent = 20

@app.route('/')
def index():

    return render_template('index.html', paragraph=paragraph, anger_percent=anger_percent, happiness_percent=happiness_percent, sadness_percent=sadness_percent, surprise_percent=surprise_percent)

@app.route('/upload', methods=['POST'])
def upload():
    selected_option = request.form.get('selected_option')
    print(selected_option)
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        converted_file = 'audio.wav'
        convert_video_to_wav(file_path, converted_file)

        flash('File uploaded and converted successfully')
        return render_template('index.html', paragraph=paragraph, anger_percent=anger_percent, happiness_percent=happiness_percent, sadness_percent=sadness_percent, surprise_percent=surprise_percent,selected_video=filename)

    flash('Invalid file format. Allowed formats: mp4')
    return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True)