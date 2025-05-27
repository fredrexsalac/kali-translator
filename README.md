# Kali Translator

**Kali Translator** is a secure, private translation web app inspired by Kali Linux, built with Django. It features voice input using the Vosk offline speech recognition model, text-to-speech playback, language swap, and a polished UI with accessibility in mind.

---

## Features

- Secure and private translation (no external APIs by default)
- Offline speech-to-text powered by [Vosk](https://alphacephei.com/vosk/)
- Text-to-speech playback (Web Speech API)
- Language selection and swap functionality
- Audio file upload for transcription
- Responsive and accessible UI with custom cursors and sparkle click effects
- CSRF protection and secure Django setup
- Easily deployable on Render, Heroku, or locally

---

## Getting Started

### Prerequisites

- Python 3.11+
- `pip` package manager
- (Optional) Virtual environment tool (recommended)

---
2. **Create and activate a virtual environment (recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
4. **Download the Vosk model (required for offline speech recognition):**

   The Vosk model is **not included** due to its large size. To get it:

   ```bash
   bash download_model.sh
5. **Apply migrations:**

   ```bash
   python manage.py migrate
6. **Run the development server:**

   ```bash
   python manage.py runserver
7. **Open your browser at** `http://127.0.0.1:8000`


### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/kali-translator.git
   cd kali-translator
---------------------------------------------------------------------------------------------------------------------
## 🌐 Live Web App

The **Kali Translator** is deployed and available as a real-time web application.

🔗 **Live URL:** [https://kali-translator.onrender.com](https://kali-translator.onrender.com)  
*(Replace this with your actual deployed URL)*

### Features Available Online

- 🔐 Secure, privacy-focused translation interface  
- 🎙️ Voice input via microphone (speech-to-text)  
- 🔊 Text-to-speech output  
- 🌍 Language detection and swapping  
- 📱 Mobile-friendly, responsive UI  
- 🛡️ No tracking or third-party cookies  

### Deployment Details

- **Platform:** [Render](https://render.com/)  
- **Web Server:** Gunicorn (WSGI)  
- **Framework:** Django (Python)  
- **Database:** SQLite (default, can be upgraded)  
- **Offline Speech Recognition:** Vosk (model downloaded on server during build/start)  
