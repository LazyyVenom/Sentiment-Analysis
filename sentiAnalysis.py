### VIDEO -> Images & Audio -> Audio -> NLP -> Text -> Emotions
###       -> Images -> CV -> Emotions

from moviepy.editor import VideoFileClip
import cv2 
from deepface import DeepFace

import speech_recognition as sr
def sentimentAnalysis():
    from textblob import TextBlob
    text = "chotu motu"
    blob = TextBlob(text)


    # You can access the sentiment polarity and subjectivity of the text
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    surprise = abs(polarity) * abs(0.5 - subjectivity)
    anger = polarity * abs(1 - subjectivity)

    # The polarity ranges from -1 (negative) to 1 (positive), with 0 being neutral.
    # The subjectivity ranges from 0 (objective) to 1 (subjective).

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"


    print(f"Anger: {anger}")
    print(f"Surprise: {surprise}")
    print(f"Sentiment: {sentiment}")
    print(f"Polarity: {polarity}")
    print(f"Subjectivity: {subjectivity}")
    return anger,surprise,text,polarity

# convert_video_to_wav('Old Stuff\youtube downloader\downloads\Why You Cant Code.mp4','audio.wav')
# anger,surprise,sentiment,polarity = sentimentAnalysis()


def sentiImage(image):
    try:
        img = cv2.imread(image)
        # storing the result 
        result = DeepFace.analyze(img, actions = ['emotion'])
        # 'VGG-Face', 'Emotion FER', or 'Ensemble' 
        print(result)
    except Exception as e:
        print(e)
 
sentiImage(r"C:\Users\Anubhav Choubey\Pictures\Acer\Acer_Wallpaper_01_3840x2400.jpg")