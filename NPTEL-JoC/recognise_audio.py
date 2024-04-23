import speech_recognition as sr

audio_file = "path/to/file.wav"

# Initialise recogniser
recogniser = sr.Recognizer()

with sr.AudioFile(audio_file) as source:
    audio = recogniser.record(source)

try:
    print("Audio file contains: " + recogniser.recognize_google_cloud(audio_data=audio))
except sr.UnknownValueError:
    print("Google speech recognition could not understand audio")
except sr.RequestError:
    print("Couldn't get the results from Google Speech Recognition")
