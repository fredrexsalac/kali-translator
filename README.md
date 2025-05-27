Kali Translator
Kali Translator is a secure, private translation web app inspired by Kali Linux, built with Django. It features voice input using the Vosk offline speech recognition model, text-to-speech playback, language swap, and a polished UI with accessibility in mind.

Features
Secure and private translation (no external APIs by default)

Offline speech-to-text powered by Vosk

Text-to-speech playback (Web Speech API)

Language selection and swap functionality

Audio file upload for transcription

Responsive and accessible UI with custom cursors and sparkle click effects

CSRF protection and secure Django setup

Easily deployable on Render, Heroku, or locally

Getting Started
Prerequisites
Python 3.11+

pip package manager

(Optional) Virtual environment tool (recommended)

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/kali-translator.git
cd kali-translator
Create and activate a virtual environment (recommended):

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Download the Vosk model (required for offline speech recognition):

The Vosk model is not included due to its large size. To get it:

bash
Copy
Edit
bash download_model.sh
This script downloads and extracts the Vosk model to the project directory.

Apply migrations:

bash
Copy
Edit
python manage.py migrate
Run the development server:

bash
Copy
Edit
python manage.py runserver
Open your browser at http://127.0.0.1:8000

Configuration
Environment variables:

SECRET_KEY — Django secret key (production only)

DEBUG — Set to True or False (default: False)

ALLOWED_HOSTS — Comma-separated list of allowed hosts (e.g., localhost,127.0.0.1)

Vosk model path:

The model folder path is set in settings.py as:

python
Copy
Edit
VOSK_MODEL_PATH = os.path.join(BASE_DIR, "vosk-model-small-en-us-0.15")
Deployment
For deployment on Render or other services:

Include the download_model.sh script in your build/start commands to automatically fetch the Vosk model.

Ensure environment variables are configured correctly.

Use gunicorn or similar WSGI servers for production.

Example start commands on Render:

bash
Copy
Edit
bash download_model.sh
python manage.py migrate
gunicorn kali_translator_app.wsgi:application
Notes
The Vosk speech recognition model is large (~50-70MB), so it is excluded from Git repository and must be downloaded separately.

If you want to use online or cloud-based translation APIs, modify the backend accordingly.

This project focuses on privacy and offline capabilities wherever possible.

License
MIT License — see LICENSE file.

Acknowledgments
Vosk for offline speech recognition

Django framework

Inspired by a Computer Science Student and Themed by Kali Linux

