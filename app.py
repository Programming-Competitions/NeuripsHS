import os
import threading
import json
from flask import Flask, render_template, request, redirect, url_for
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from googletrans import Translator

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Load language codes from JSON file
def load_language_codes():
    with open('language_codes.json', 'r') as f:
        data = json.load(f)
    return data['codes'], data['names']

language_codes, language_names = load_language_codes()

keep_running = False

# Function to update the translated text
def update_translation(input_lang_code, output_lang_code):
    global keep_running

    if keep_running:
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Speak Now!\n")
            audio = recognizer.listen(source)

            try:
                speech_text = recognizer.recognize_google(audio)

                # Translate the recognized text
                translator = Translator()
                translated_text = translator.translate(speech_text, src=input_lang_code, dest=output_lang_code).text

                # Generate and play audio for the translated text
                voice = gTTS(translated_text, lang=output_lang_code)
                voice.save('static/voice.mp3')
                playsound('static/voice.mp3')
                os.remove('static/voice.mp3')

                return speech_text, translated_text

            except sr.UnknownValueError:
                return None, "Could not understand!"
            except sr.RequestError:
                return None, "Could not request from Google!"

@app.route('/', methods=['GET', 'POST'])
def index():
    global keep_running

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'Start Translation':
            keep_running = True
            input_lang_code = request.form.get('input_lang')
            output_lang_code = request.form.get('output_lang')
            recognized_text, translated_text = update_translation(input_lang_code, output_lang_code)
            return render_template('index.html', language_names=language_names, recognized_text=recognized_text, translated_text=translated_text, input_lang=input_lang_code, output_lang=output_lang_code)

        elif action == 'Kill Execution':
            keep_running = False

    return render_template('index.html', language_names=language_names)

if __name__ == '__main__':
    app.run(debug=True)