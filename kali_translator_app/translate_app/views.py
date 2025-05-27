import os
import wave
import json
import uuid
import subprocess
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import default_storage
from googletrans import Translator
from vosk import Model, KaldiRecognizer
import pyttsx3

# Initialize Vosk model once
VOSK_MODEL_PATH = os.path.join(settings.BASE_DIR, "vosk-model-small-en-us-0.15")
vosk_model = Model(VOSK_MODEL_PATH)

def convert_to_wav(input_path, output_path):
    """Convert any audio file to 16kHz mono WAV using ffmpeg."""
    cmd = [
        'ffmpeg', '-y', '-i', input_path,
        '-ar', '16000', '-ac', '1',
        output_path
    ]
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        raise RuntimeError(f"ffmpeg error: {proc.stderr.decode()}")

def speech_to_text(wav_path):
    wf = wave.open(wav_path, "rb")
    rec = KaldiRecognizer(vosk_model, wf.getframerate())
    results = []

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            results.append(res.get("text", ""))
    res = json.loads(rec.FinalResult())
    results.append(res.get("text", ""))
    wf.close()
    return " ".join(results).strip()

def text_to_speech(text, output_path):
    """Use pyttsx3 to save speech audio locally as WAV or MP3."""
    engine = pyttsx3.init()
    engine.save_to_file(text, output_path)
    engine.runAndWait()

def translate_view(request):
    languages = {
        'af': 'Afrikaans', 'sq': 'Albanian', 'am': 'Amharic', 'ar': 'Arabic',
        'hy': 'Armenian', 'az': 'Azerbaijani', 'eu': 'Basque', 'be': 'Belarusian',
        'bn': 'Bengali', 'bs': 'Bosnian', 'bg': 'Bulgarian', 'ca': 'Catalan',
        'ceb': 'Cebuano', 'ny': 'Chichewa', 'zh-cn': 'Chinese (Simplified)', 'zh-tw': 'Chinese (Traditional)',
        'co': 'Corsican', 'hr': 'Croatian', 'cs': 'Czech', 'da': 'Danish', 'nl': 'Dutch',
        'en': 'English', 'eo': 'Esperanto', 'et': 'Estonian', 'tl': 'Filipino', 'fi': 'Finnish',
        'fr': 'French', 'fy': 'Frisian', 'gl': 'Galician', 'ka': 'Georgian', 'de': 'German',
        'el': 'Greek', 'gu': 'Gujarati', 'ht': 'Haitian Creole', 'ha': 'Hausa', 'haw': 'Hawaiian',
        'he': 'Hebrew', 'hi': 'Hindi', 'hmn': 'Hmong', 'hu': 'Hungarian', 'is': 'Icelandic',
        'ig': 'Igbo', 'id': 'Indonesian', 'ga': 'Irish', 'it': 'Italian', 'ja': 'Japanese',
        'jw': 'Javanese', 'kn': 'Kannada', 'kk': 'Kazakh', 'km': 'Khmer', 'rw': 'Kinyarwanda',
        'ko': 'Korean', 'ku': 'Kurdish (Kurmanji)', 'ky': 'Kyrgyz', 'lo': 'Lao', 'la': 'Latin',
        'lv': 'Latvian', 'lt': 'Lithuanian', 'lb': 'Luxembourgish', 'mk': 'Macedonian',
        'mg': 'Malagasy', 'ms': 'Malay', 'ml': 'Malayalam', 'mt': 'Maltese', 'mi': 'Maori',
        'mr': 'Marathi', 'mn': 'Mongolian', 'my': 'Myanmar (Burmese)', 'ne': 'Nepali',
        'no': 'Norwegian', 'or': 'Odia (Oriya)', 'ps': 'Pashto', 'fa': 'Persian', 'pl': 'Polish',
        'pt': 'Portuguese', 'pa': 'Punjabi', 'ro': 'Romanian', 'ru': 'Russian', 'sm': 'Samoan',
        'gd': 'Scots Gaelic', 'sr': 'Serbian', 'st': 'Sesotho', 'sn': 'Shona', 'sd': 'Sindhi',
        'si': 'Sinhala', 'sk': 'Slovak', 'sl': 'Slovenian', 'so': 'Somali', 'es': 'Spanish',
        'su': 'Sundanese', 'sw': 'Swahili', 'sv': 'Swedish', 'tg': 'Tajik', 'ta': 'Tamil',
        'tt': 'Tatar', 'te': 'Telugu', 'th': 'Thai', 'tr': 'Turkish', 'tk': 'Turkmen',
        'uk': 'Ukrainian', 'ur': 'Urdu', 'ug': 'Uyghur', 'uz': 'Uzbek', 'vi': 'Vietnamese',
        'cy': 'Welsh', 'xh': 'Xhosa', 'yi': 'Yiddish', 'yo': 'Yoruba', 'zu': 'Zulu',
    }

    source_text = ''
    translated_text = ''
    audio_file_url = ''
    source_lang = 'en'
    target_lang = 'tl'

    if request.method == 'POST':
        src_lang_post = request.POST.get('source_lang', 'en').lower()
        tgt_lang_post = request.POST.get('target_lang', 'tl').lower()
        source_lang = src_lang_post if src_lang_post in languages else 'en'
        target_lang = tgt_lang_post if tgt_lang_post in languages else 'tl'

        if 'audio_file' in request.FILES:
            audio = request.FILES['audio_file']
            raw_filename = f"raw_audio_{uuid.uuid4()}"
            wav_filename = f"wav_audio_{uuid.uuid4()}.wav"

            raw_path = default_storage.save(raw_filename, audio)
            abs_raw_path = os.path.join(settings.MEDIA_ROOT, raw_path)
            abs_wav_path = os.path.join(settings.MEDIA_ROOT, wav_filename)

            try:
                convert_to_wav(abs_raw_path, abs_wav_path)
                source_text = speech_to_text(abs_wav_path)
            except Exception as e:
                source_text = f"Error processing audio: {e}"
            finally:
                default_storage.delete(raw_path)
                if os.path.exists(abs_wav_path):
                    os.remove(abs_wav_path)
        else:
            source_text = request.POST.get('source_text', '').strip()

        if source_text and not source_text.startswith("Error"):
            try:
                translator = Translator()
                translated = translator.translate(source_text, src=source_lang, dest=target_lang)
                translated_text = translated.text

                # Save TTS audio as WAV or MP3 file using pyttsx3
                tts_filename = f"tts_{uuid.uuid4()}.mp3"
                tts_path = os.path.join(settings.MEDIA_ROOT, tts_filename)
                text_to_speech(translated_text, tts_path)

                audio_file_url = settings.MEDIA_URL + tts_filename
            except Exception as e:
                translated_text = f"Translation/TTS error: {e}"
                audio_file_url = ''
        else:
            translated_text = ''
            audio_file_url = ''

    context = {
        'languages': languages,
        'source_text': source_text,
        'translated_text': translated_text,
        'source_lang': source_lang,
        'target_lang': target_lang,
        'audio_file_url': audio_file_url,
    }
    return render(request, 'index.html', context)
