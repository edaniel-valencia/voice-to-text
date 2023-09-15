import speech_recognition as sr
import time

r = sr.Recognizer()

# Cambia la ruta del archivo usando barras diagonales dobles o barras diagonales normales
with sr.AudioFile('D:\\TEACH - LEARN\\Python\\test3.wav') as source:
    audio = r.listen(source)
    
    try: 
        print("Leyendo el audio, espera...")
        text = r.recognize_google(audio, language='es-ES')  # Reconocimiento en español
        time.sleep(1.5)
        print(text)
    except:
        print("No se pudo reconocer el audio")
