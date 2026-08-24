import os
import time
import whisper
import streamlit as st
from pathlib import Path
from typing import Optional
from pydub import AudioSegment

SUPPORTED_FORMATS = ["wav", "mp3", "aac", "ogg", "flac", "m4a", "mp4", "webm"]

@st.cache_resource(show_spinner=False)
def load_whisper_model(model_name: str):
    return whisper.load_model(model_name)

def to_wav(input_path: str) -> str:
    """Convert any supported audio format to WAV using pydub (requires ffmpeg)."""
    ext = Path(input_path).suffix.lower().lstrip(".")
    if ext == "wav":
        return input_path
    audio = AudioSegment.from_file(input_path)
    wav_path = input_path.rsplit(".", 1)[0] + "_converted.wav"
    audio.export(wav_path, format="wav")
    return wav_path

def transcribe_audio(audio_path: str, model_choice: str, lang_code: Optional[str]):
    """Run Whisper transcription with progress feedback."""
    progress = st.progress(0, text="")
    status = st.empty()

    status.markdown("🔄 **Procesando audio...**")
    progress.progress(15, text="Procesando audio...")
    wav_path = to_wav(audio_path)

    status.markdown("🧠 **Transcribiendo con Whisper...**")
    progress.progress(40, text="Transcribiendo con IA...")

    model = load_whisper_model(model_choice)

    options = {}
    if lang_code:
        options["language"] = lang_code

    result = model.transcribe(wav_path, **options)

    progress.progress(95, text="Finalizando...")
    time.sleep(0.3)
    progress.progress(100, text="¡Completado!")
    time.sleep(0.4)

    progress.empty()
    status.empty()

    # Cleanup converted file
    if wav_path != audio_path and os.path.exists(wav_path):
        os.remove(wav_path)

    return result["text"].strip(), result.get("language", "desconocido")
