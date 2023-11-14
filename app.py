from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # You can replace these values with your actual data
    data = {
        'paragraph': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        'option': 'None',  # or 'video'
        'selected_image': 'example.jpg',  # Image file in the static folder
        'selected_video': 'example.mp4',  # Video file in the static folder
        'anger_percent': 30,
        'happiness_percent': 50,
        'sadness_percent': 10,
        'surprise_percent': 70,
    }

    return render_template('index.html', **data)

if __name__ == '__main__':
    app.run(debug=True)
