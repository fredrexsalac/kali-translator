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

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/kali-translator.git
   cd kali-translator
