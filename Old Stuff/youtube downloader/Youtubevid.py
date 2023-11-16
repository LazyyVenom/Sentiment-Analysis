from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from pytube import YouTube
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

# Define the download directory
download_dir = os.path.join(app.root_path, 'downloads')

# Ensure the download directory exists
os.makedirs(download_dir, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    status = {'progress': 0, 'message': 'Not started'}  # Initialize status

    if request.method == 'POST':
        video_url = request.form.get('video_url')
        selected_itag = request.form.get('itag')

        try:
            # Validate and sanitize user inputs
            if not video_url:
                flash('Please enter a valid YouTube video URL.', 'error')
                return redirect(url_for('index'))

            # Create a YouTube object
            yt = YouTube(video_url)

            # Validate selected_itag
            if selected_itag not in [str(stream.itag) for stream in yt.streams]:
                flash('Invalid video quality selected.', 'error')
                return redirect(url_for('index'))

            # Get the stream with the selected itag
            video_stream = yt.streams.get_by_itag(selected_itag)

            # Download the video to the download directory
            video_stream.download(output_path=download_dir)

            status = {'progress': 100, 'message': 'Download completed successfully!'}
            flash(status['message'], 'success')
            return redirect(url_for('download', filename=video_stream.default_filename))

        except Exception as e:
            app.logger.error(f"Error during download: {str(e)}")
            status = {'progress': 0, 'message': f'Error: {str(e)}'}
            flash(status['message'], 'error')

    return render_template('index.html', status=status)  # Pass status to the template

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(download_dir, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
