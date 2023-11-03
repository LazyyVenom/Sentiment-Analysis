### VIDEO -> Images & Audio -> Audio -> NLP -> Text -> Emotions
###       -> Images -> CV -> Emotions

from moviepy.editor import VideoFileClip

def convert_video_to_wav(input_video, output_wav):
    """
    Gives Audio File from video Give directories
    """
    video_clip = VideoFileClip(input_video)
    audio_clip = video_clip.audio

    # Save the audio as a WAV file
    audio_clip.write_audiofile(output_wav, codec='pcm_s16le')

