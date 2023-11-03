from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from pytube import YouTube
import os

app = Flask(__name__)

# Define the download directory
download_dir = os.path.join(app.root_path, 'downloads')

# Ensure the download directory exists
os.makedirs(download_dir, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form['video_url']
        selected_itag = request.form['itag']

        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the stream with the selected itag
        video_stream = yt.streams.get_by_itag(selected_itag)

        # Download the video to the download directory
        video_stream.download(output_path=download_dir)

        return redirect(url_for('download', filename=video_stream.default_filename))

    return render_template('index.html')

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(download_dir, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
