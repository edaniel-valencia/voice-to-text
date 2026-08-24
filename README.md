# 🎙️ VoiceScript — Transcriptor de Voz a Texto

> Convierte archivos de audio o grabaciones de micrófono a texto usando **Whisper** de OpenAI, con interfaz web moderna hecha en **Streamlit** e historial persistente en **SQLite**.

---

## ✨ Características

| Funcionalidad | Detalle |
|---|---|
| 📁 **Subir archivos** | Drag & drop · WAV, MP3, AAC, OGG, FLAC, M4A |
| 🎤 **Grabar desde micrófono** | Grabadora integrada en el navegador |
| 🧠 **Whisper local** | Modelos `tiny`, `base`, `small`, `medium` — sin API key |
| 🌐 **Multi-idioma** | Español, Inglés, Francés, Portugués, Alemán, Italiano, Japonés, Chino |
| 💾 **Historial persistente** | SQLite — sobrevive recargas de página |
| 📊 **Exportar** | TXT, DOCX y PDF con un clic |
| ✏️ **Editor** | Edita la transcripción antes de exportar |

---

## 🚀 Instalación

### 1. Requisitos previos

- Python 3.9+
- [ffmpeg](https://ffmpeg.org/) instalado en el sistema

```bash
# macOS
brew install ffmpeg

# Ubuntu / Debian
sudo apt install ffmpeg
```

### 2. Instalar dependencias

```bash
pip3 install -r requirements.txt
```

### 3. Lanzar la app

```bash
~/.local/bin/streamlit run app.py
# o bien:
/Users/<tu_usuario>/Library/Python/3.9/bin/streamlit run app.py
```

Luego abre tu navegador en **http://localhost:8501**

---

## 🧠 Modelos de Whisper

Puedes seleccionar el modelo desde la barra lateral de la app:

| Modelo | Tamaño | Velocidad | Precisión |
|--------|--------|-----------|-----------|
| `tiny` | ~40 MB | ⚡ Muy rápido | Básica |
| `base` | ~150 MB | ✅ Rápido | **Recomendado** |
| `small` | ~500 MB | 🐢 Moderado | Alta |
| `medium` | ~1.5 GB | 🐌 Lento | Muy alta |

El modelo se descarga automáticamente la primera vez y queda cacheado.

---

## 📂 Estructura del Proyecto

```
voice-to-text/
├── app.py                 # App principal (Streamlit)
├── requirements.txt       # Dependencias Python
├── transcriptions.db      # Base de datos SQLite (se crea automáticamente)
└── README.md              # Este archivo
```

---

## 🗄️ Base de Datos SQLite

Las transcripciones se guardan automáticamente en `transcriptions.db`. La tabla tiene esta estructura:

```sql
CREATE TABLE transcriptions (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    filename    TEXT,       -- Nombre del archivo de audio
    language    TEXT,       -- Idioma detectado (ej: "es", "en")
    model       TEXT,       -- Modelo Whisper usado
    text        TEXT,       -- Texto transcrito
    word_count  INTEGER,    -- Número de palabras
    created_at  TEXT        -- Fecha y hora de la transcripción
);
```

Cada transcripción se guarda automáticamente y persiste aunque recargues la página o reinicias la app.

---

## 📦 Dependencias Principales

```
streamlit              # Interfaz web
openai-whisper         # Motor de transcripción IA
pydub                  # Conversión de formatos de audio
python-docx            # Exportar a Word (.docx)
fpdf2                  # Exportar a PDF
audio-recorder-streamlit  # Grabación de micrófono
torch                  # Requerido por Whisper
```

---

## 🛠️ Solución de Problemas

### ❌ `ffmpeg not found`
```bash
brew install ffmpeg  # macOS
sudo apt install ffmpeg  # Linux
```

### ❌ NumPy incompatibility warning
```bash
pip3 install "numpy<2"
```

### ❌ `streamlit: command not found`
Usa la ruta completa:
```bash
/Users/<tu_usuario>/Library/Python/3.9/bin/streamlit run app.py
```

---

## 📄 Licencia

MIT — Libre para uso personal y comercial.
