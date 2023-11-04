### VIDEO -> Images & Audio -> Audio -> NLP -> Text -> Emotions
###       -> Images -> CV -> Emotions

from moviepy.editor import VideoFileClip

def convert_video_to_wav(input_video, output_wav):
    video_clip = VideoFileClip(input_video)
    audio_clip = video_clip.audio

    # Save the audio as a WAV file
    audio_clip.write_audiofile(output_wav, codec='pcm_s16le')

import torch
import torchaudio
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

# Load the pre-trained Wav2Vec 2.0 model and processor
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

# Load an audio file for recognition
audio_input, _ = torchaudio.load("your_audio.wav")

# Preprocess the audio
input_values = processor(audio_input, return_tensors="pt").input_values

# Perform speech recognition
with torch.no_grad():
    logits = model(input_values).logits

# Convert the output logits to text
predicted_ids = torch.argmax(logits, dim=-1)
transcription = processor.batch_decode(predicted_ids)

print("Recognized transcription:", transcription[0])

from transformers import pipeline

nlp = pipeline("sentiment-analysis")
result = nlp("I love this product! It's amazing.")
print(result)

from textblob import TextBlob

# Create a TextBlob object with your text
text = "hello there peter parker here and i am very angry and sad"
blob = TextBlob(text)


# You can access the sentiment polarity and subjectivity of the text
polarity = blob.sentiment.polarity
subjectivity = blob.sentiment.subjectivity
surprise = abs(polarity) * (0.5 - subjectivity)
anger = polarity * (0.5 - subjectivity)

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
