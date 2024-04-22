import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Record audio from the microphone
with sr.Microphone() as source:
    print("Speak something:")
    audio = r.listen(source, timeout=5)  # Set timeout to 10 seconds


try:
    # Recognize speech using Google Web Speech API
    text = r.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Google Web Speech API could not understand the audio.")
except sr.RequestError as e:
    print("Could not request results from Google Web Speech API; {0}".format(e))
