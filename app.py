from flask import Flask, render_template, request, redirect, flash,url_for
import os
from sentimentsAnalysis import imageAnalysis,videoAnalysis,captionAnalysis

def youtubeDownload(link):
    from pytube import YouTube
    yt = YouTube(link)
    video_stream = yt.streams.get_by_resolution("360p")
    video_stream.download(output_path='static',filename="video.mp4")
    return "Completed"
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
    'neutral_percent': 0,
    'anger_percent': 0,
    'happiness_percent': 0,
    'sadness_percent': 0,
    'surprise_percent': 0,
}

@app.route('/')
def index():
    # You can replace these values with your actual data
    return render_template('index.html',**data)


@app.route('/select', methods=['POST'])
def select_option():
    selected_option = request.form.get('selected_option')
    
    return render_template('index.html',selected_option=selected_option)


@app.route('/link',methods=['POST','GET'])
def linkAnalysis():
    #https://www.youtube.com/watch?v=ePNzlRFvR4E
    link = request.form.get("linkyt")
    print(link)
    print("HERE")
    youtubeDownload(link)
    emotions = videoAnalysis(r"static/video.mp4")
    data = {
                    'processed':'True',
                    'option': "video", 
                    'selected_option':"youtube",
                }

    data['neutral_percent'] = emotions['neutral']
    data['angry_percent'] = emotions['angry']
    data['happy_percent'] = emotions['happy']
    data['sad_percent'] = emotions['sad']
    data['surprise_percent'] = emotions['surprise']
    data['paragraph'] = "Check Out the Meters"

    return render_template("index.html",**data)


@app.route('/insta', methods=['POST','GET'])
def upload_insta():
    print(request.files)
    print(request.form)
    if 'file' not in request.files:
        flash('No file part', 'error')
        return "ERROR - No file part"

    file = request.files['file']
    # selected_option = request.form.get('selected_option')
    caption = request.form.get('caption')

    if file.filename == '':
        flash('No selected file', 'error')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
        if file.filename.rsplit('.', 1)[1].lower() in ['jpg', 'png', 'jpeg']:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], "image.jpg"))
            option = 'image'
        else:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], "video.mp4"))
            option = 'video'
        flash('File uploaded successfully!', 'success')

        data = {
                    'processed':'True',
                    'option': option, 
                    'selected_option':"instaReel",
                }
        
        if option == 'image':
            emotions = imageAnalysis(r"static/image.jpg")
            captionFeedback = captionAnalysis(caption)
            
            #Feeding Data
            data['neutral_percent'] = emotions['neutral']
            data['angry_percent'] = emotions['angry']
            data['happy_percent'] = emotions['happy']
            data['sad_percent'] = emotions['sad']
            data['surprise_percent'] = emotions['surprise']
            data['paragraph'] = emotions['message'] + captionFeedback

        else:
            emotions = videoAnalysis(r"static/video.mp4")
            captionFeedback = captionAnalysis(caption)

            #Feeding Data
            data['neutral_percent'] = emotions['neutral']
            data['angry_percent'] = emotions['angry']
            data['happy_percent'] = emotions['happy']
            data['sad_percent'] = emotions['sad']
            data['surprise_percent'] = emotions['surprise']
            data['paragraph'] = "Check Out the Meters" + captionFeedback
        
        return render_template("index.html",**data)
    else:
        return "ERROR - Error"


@app.route('/upload', methods=['POST','GET'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part', 'error')
        return "ERROR"

    file = request.files['file']
    selected_option = request.form.get('selected_option')

    if file.filename == '':
        flash('No selected file', 'error')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
        if file.filename.rsplit('.', 1)[1].lower() in ['jpg', 'png', 'jpeg']:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], "image.jpg"))
            option = 'image'
        else:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], "video.mp4"))
            option = 'video'
        flash('File uploaded successfully!', 'success')

        data = {
                    'processed':'True',
                    'option': option, 
                    'selected_option':selected_option,
                }
        
        if option == 'image':
            emotions = imageAnalysis(r"static/image.jpg")
            #Feeding Data
            data['neutral_percent'] = emotions['neutral']
            data['angry_percent'] = emotions['angry']
            data['happy_percent'] = emotions['happy']
            data['sad_percent'] = emotions['sad']
            data['surprise_percent'] = emotions['surprise']
            data['paragraph'] = emotions['message']

        else:
            emotions = videoAnalysis(r"static/video.mp4")
            #Feeding Data
            data['neutral_percent'] = emotions['neutral']
            data['angry_percent'] = emotions['angry']
            data['happy_percent'] = emotions['happy']
            data['sad_percent'] = emotions['sad']
            data['surprise_percent'] = emotions['surprise']
            data['paragraph'] = "Check Out the Meters"
        
        return render_template("index.html",**data)
    else:
        return "ERROR"

if __name__ == '__main__':
    app.run(debug=True)
