import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")
OLLAMA_API_KEY  = os.getenv("OLLAMA_API_KEY",  "ollama")
OLLAMA_MODEL    = os.getenv("OLLAMA_MODEL",    "llama3.2")

OLLAMA_PROMPTS = {
    "✨ Mejorar redacción":   "Mejora la redacción del siguiente texto transcrito de audio. Corrige la gramática, añade puntuación correcta y haz el texto más fluido. Devuelve SOLO el texto mejorado, sin explicaciones:\n\n",
    "📋 Resumir":             "Resume el siguiente texto en 3-5 puntos clave concisos. Devuelve SOLO el resumen:\n\n",
    "🔤 Corregir puntuación": "Añade puntuación y mayúsculas correctas al siguiente texto. Devuelve SOLO el texto corregido:\n\n",
    "📝 Formato lista":       "Convierte el siguiente texto en una lista de puntos ordenados y claros. Devuelve SOLO la lista:\n\n",
    "🌐 Traducir al inglés":  "Translate the following text to English. Return ONLY the translation:\n\n",
}

@st.cache_resource(show_spinner=False)
def get_ollama_client():
    return OpenAI(base_url=OLLAMA_BASE_URL, api_key=OLLAMA_API_KEY)

def run_ollama(prompt_prefix: str, text: str) -> str:
    """Envía texto a Ollama y devuelve la respuesta."""
    try:
        client = get_ollama_client()
        response = client.chat.completions.create(
            model=OLLAMA_MODEL,
            messages=[{"role": "user", "content": prompt_prefix + text}],
            temperature=0.3,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error con Ollama: {e}"
