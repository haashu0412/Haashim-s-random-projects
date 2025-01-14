import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()

while True:
    try:

        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            print("Listening...")
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"Recognized: {text}")

    except sr.UnknownValueError: 
        print("Sorry, I did not catch that.")
        recognizer = sr.Recognizer()  
        continue
