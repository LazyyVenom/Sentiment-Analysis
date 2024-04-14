# Sentiment-Analysis

Sentiment-Analysis is a project aimed at analyzing the sentiment of videos and images, specifically targeting Instagram posts and reels, as well as YouTube videos.

## Functionality

1. **Caption Analysis**: Analyzes captions of Instagram posts and reels using TextBlob.
2. **Video Analysis**: Analyzes YouTube videos, reels, and uploaded videos.
3. **Image Analysis**: Analyzes images from Instagram posts.

## Details

### Front End

The front end of the project is implemented using a WebApp built with Flask framework, HTML, CSS, and basic JavaScript.

### Back End

The back end of the project consists of various functionalities implemented in Python:

1. **Youtube Downloader**: Utilizes `pytube` library for downloading YouTube videos.
2. **Sentiment Analysis (Images & Video)**: Employs `DeepFace` and `cv2` for analyzing sentiment in both images and videos.
3. **Caption Analysis (Text)**: Utilizes `TextBlob` for analyzing captions of Instagram posts and reels.

## Libraries Used

- Flask: For creating the WebApp.
- HTML, CSS, Basic JS: For front end development.
- Pytube: For downloading YouTube videos.
- DeepFace: For analyzing sentiment in images and videos.
- OpenCV (cv2): For image and video processing.
- TextBlob: For analyzing text sentiment.

## Usage

1. Clone the repository to your local machine.
2. Install the required libraries listed above.
3. Run the Flask app using `python app.py`.
4. Access the web application via the provided URL.
5. Follow the instructions on the interface to analyze videos, images, or captions.

## Contributing

Contributions are welcome! If you have any ideas for improvements, new features, or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
