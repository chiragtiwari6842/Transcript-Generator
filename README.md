# Video to Text Transcription Web App

This Flask-based web application allows users to upload video files, extracts the audio from the video, and generates a text transcription using Google's Speech Recognition API.

You can access the web app at this [link] (https://transcript-generator.onrender.com/)

## Features
- Upload videos in `.mp4`, `.avi`, or `.mov` formats.
- Extracts audio from the uploaded video.
- Converts audio to text using Google's Speech Recognition API.
- Displays the transcription directly on the webpage.

## Tech Stack
- **Flask**: A lightweight web framework for Python.
- **MoviePy**: A video editing library used to extract audio from video.
- **SpeechRecognition**: A Python library for performing speech recognition with Google Web Speech API.
- **HTML/CSS**: For frontend design.

## Setup and Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/chiragtiwari6842/Transcript-Generator.git
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows use: venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    python app.py
    ```

5. Open your browser and navigate to `http://127.0.0.1:5000/` to access the web app.

## File Structure
  ├── app.py # Main Flask application 
    ├── requirements.txt # Python dependencies 
    └── README.md # Documentation file
    ├── templates/ │ 
        ├── upload.html # Upload page template 
        │ └── result.html # Result page template  

## How It Works
1. User uploads a video via the home page.
2. The video is processed in-memory, and the audio is extracted using MoviePy.
3. The extracted audio is transcribed into text using the SpeechRecognition library.
4. The transcription is displayed directly on the result page.

## Dependencies
- Flask
- MoviePy
- SpeechRecognition

To install all dependencies, run:
```bash
pip install -r requirements.txt
```

## Customization

* `Allowed video formats:` You can modify the allowed video formats by updating the ALLOWED_EXTENSIONS set in the app.py file.

* `Speech Recognition API:` Currently, the app uses Google’s free Speech Recognition API. You can modify this to use other services such as Azure, IBM, or Sphinx by editing the generate_transcription() function.
