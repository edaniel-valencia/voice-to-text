import speech_recognition as sr
import time
from pydub import AudioSegment
from pydub.playback import play
from pydub.silence import split_on_silence

r = sr.Recognizer()

# Cambia la ruta del archivo MP3 usando barras diagonales dobles o barras diagonales normales
mp3_file_path = 'D:\TEACH - LEARN\Python\voice-to-text\mp3-mp3'

# Convierte el archivo MP3 a WAV
def convert_mp3_to_wav(mp3_file):
    audio = AudioSegment.from_mp3(mp3_file)
    wav_file = mp3_file.replace('.mp3', '.wav')
    audio.export(wav_file, format="wav")
    return wav_file

# Divide el audio en fragmentos
def split_audio(audio_file, chunk_duration=30):
    sound = AudioSegment.from_wav(audio_file)
    audio_chunks = split_on_silence(sound, min_silence_len=500, silence_thresh=-40, keep_silence=100)
    return audio_chunks

# Realiza el reconocimiento de voz en cada fragmento
def recognize_chunks(chunks):
    for i, chunk in enumerate(chunks):
        chunk.export(f"chunk_{i}.wav", format="wav")  # Exporta el fragmento como archivo WAV
        with sr.AudioFile(f"chunk_{i}.wav") as source:
            audio = r.listen(source)
            try:
                print(f"Transcripción del fragmento {i}:")
                text = r.recognize_google(audio, language='es-ES')
                print(text)
                time.sleep(1.5)
            except sr.UnknownValueError:
                print(f"No se pudo reconocer el fragmento {i}")
            except sr.RequestError as e:
                print(f"Error en la solicitud de reconocimiento de voz: {e}")

if __name__ == "__main__":
    wav_file_path = convert_mp3_to_wav(mp3_file_path)  # Convierte MP3 a WAV
    audio_chunks = split_audio(wav_file_path)
    recognize_chunks(audio_chunks)
