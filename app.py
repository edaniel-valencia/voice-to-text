import speech_recognition as sr
import time

r = sr.Recognizer()

# Cambia la ruta del archivo usando barras diagonales dobles o barras diagonales normales
audio_file_path = 'D:\\TEACH - LEARN\\Python\\test2.wav'

# Divide el audio en fragmentos
def split_audio(audio_file, chunk_duration=30):
    with sr.AudioFile(audio_file) as source:
        audio_duration = source.DURATION
    chunk_duration = min(chunk_duration, audio_duration)
    audio_chunks = []
    start_time = 0
    while start_time < audio_duration:
        end_time = min(start_time + chunk_duration, audio_duration)
        audio_chunks.append((start_time, end_time))
        start_time = end_time
    return audio_chunks

# Realiza el reconocimiento de voz en cada fragmento
def recognize_chunks(chunks, audio_file):
    for i, (start_time, end_time) in enumerate(chunks):
        with sr.AudioFile(audio_file) as source:
            audio = r.record(source, offset=start_time, duration=end_time - start_time)
            try:
                print(f"Transcripción del fragmento {i + 1}:")
                text = r.recognize_google(audio, language='es-ES')
                print(text)
                time.sleep(1.5)
            except sr.UnknownValueError:
                print(f"No se pudo reconocer el fragmento {i + 1}")
            except sr.RequestError as e:
                print(f"Error en la solicitud de reconocimiento de voz: {e}")

if __name__ == "__main__":
    audio_chunks = split_audio(audio_file_path)
    recognize_chunks(audio_chunks, audio_file_path)