#For Image And Captions:
import cv2 
from deepface import DeepFace
from textblob import TextBlob
from os import remove as removeFile

def imageAnalysis(img):
    try:
        #Analyzing
        img = cv2.imread(img)
        result = DeepFace.analyze(img, actions = ['emotion'], enforce_detection=False)

        #Storing values
        neutral = round(result[0]['emotion']['neutral'],3)
        angry = round(result[0]['emotion']['angry'],3)
        happy = round(result[0]['emotion']['happy'],3)
        sad = round(result[0]['emotion']['sad'],3)
        surprise = round(result[0]['emotion']['surprise'],3)
        
        #Giving the most dominant emotion as a message
        dominant = result[0]['dominant_emotion']

        data = {
            "neutral" : neutral,
            "angry" : angry,
            "happy" : happy,
            "sad" : sad,
            "surprise" : surprise,
            "message" : f"Most Dominant/Significant Emotion is {dominant}"
        }

        return data
    
    except Exception as e:
        return {
            "neutral" : 0,
            "angry" : 0,
            "happy" : 0,
            "sad" : 0,
            "surprise" : 0,
            "message" : f"Error:{e}"
        }
    
def captionAnalysis(caption):
    blob = TextBlob(caption)

    # You can access the sentiment polarity and subjectivity of the text
    polarity = blob.sentiment.polarity

    if 0.5 > polarity > 0 :
        sentiment = "Positive"
    elif polarity >= 0.5:
        sentiment = "Very Positive"
    elif -0.5 < polarity < 0:
        sentiment = "Negative"
    elif polarity <= -0.5:
        sentiment = "Very Negative"
    else:
        sentiment = "Neutral"

    return f"Sentiment of Caption is {sentiment}: {polarity*100}%"

def videoAnalysis(video):
    # Open video capture
    cap = cv2.VideoCapture(video)

    # Get frames per second (FPS) of the video
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Variables to store overall emotion scores
    total_emotion_scores = {'angry': 0, 'disgust': 0, 'fear': 0, 'happy': 0, 'sad': 0, 'surprise': 0, 'neutral': 0}
    total_frames = 0

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        image_path = "temp_frame.jpg"
        cv2.imwrite(image_path, cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR))

        result = DeepFace.analyze(img_path=image_path, actions=['emotion'], enforce_detection=False)

        # Extract the emotion
        emotion = result[0]['emotion']

        # Update overall emotion scores
        for emotion_type, score in emotion.items():
            total_emotion_scores[emotion_type] += score

        total_frames += 1

        # Skip frames based on the desired interval (1 frame per 5 seconds)
        skip_frames = int(fps * 5)
        cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_POS_FRAMES) + skip_frames)

    # Calculate average emotion scores
    average_emotion_scores = {emotion_type: total_score / total_frames for emotion_type, total_score in total_emotion_scores.items()}

    # Release the video capture object
    cap.release()

    # Remove the temporary image file
    removeFile(image_path)

    return average_emotion_scores

