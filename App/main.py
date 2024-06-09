# Python program to translate speech to text and text to speech

from setuptools import distutils; import speech_recognition as sr
import pyttsx3
from translate import Translator

# Initialize the recognizer and translator
r = sr.Recognizer()
translator = Translator(to_lang="en")
# Function to convert text to speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()

    # If the language is Hindi, set the voice to a suitable one
    voices = engine.getProperty('voices', en_voice_id)
    for voice in voices:
        if 'english' in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break

    engine.say(command)
    engine.runAndWait()

# Loop infinitely for user to speak
while True:
    try:
        # Use the microphone as source for input
        with sr.Microphone() as source2:
            # Wait for a second to let the recognizer adjust the energy threshold
            # based on the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # Listens for the user's input
            audio2 = r.listen(source2)

            # Using Google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print("Did you say: ", MyText)

            # Translate the text to Hindi
            translated_text = translator.translate(MyText)

            print("Translation: ", translated_text)

            # Speak the translated text
            SpeakText(translated_text)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")
