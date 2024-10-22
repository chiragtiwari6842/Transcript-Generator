from flask import Flask, render_template, request, send_file
import os
import speech_recognition as sr
import moviepy.editor as mp
import tempfile
from io import BytesIO

app = Flask(__name__)
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_audio(video_stream):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video:
        temp_video.write(video_stream.read())
        temp_video.flush()
        video = mp.VideoFileClip(temp_video.name)
        audio_path = tempfile.mktemp(suffix='.wav')
        video.audio.write_audiofile(audio_path)
    return audio_path

def generate_transcription(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Speech Recognition could not understand the audio"
    except sr.RequestError as e:
        return f"Could not request results from Speech Recognition service; {e}"

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file and allowed_file(file.filename):
            audio_path = extract_audio(file)
            transcription = generate_transcription(audio_path)
            os.remove(audio_path)
            
            return render_template('result.html', transcription=transcription)
    return render_template('upload.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
