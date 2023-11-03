from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'file_upload_app/uploads'  # Set the upload folder

@app.route('/')
def index():
    # Sample paragraph
    paragraph = "This will contain a summary kind of thing."

    # Sample emotion percentages (you can replace these with real data)
    anger_percent = 0
    happiness_percent = 0
    sadness_percent = 100
    surprise_percent = 20

    return render_template('index.html', paragraph=paragraph, anger_percent=anger_percent, happiness_percent=happiness_percent, sadness_percent=sadness_percent, surprise_percent=surprise_percent)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    # Print the file name to the terminal
    print("Uploaded file name:", file.filename)


if __name__ == '__main__':
    app.run(debug=True)
