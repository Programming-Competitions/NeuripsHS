import os
import threading
import tkinter as tk
import json
from gtts import gTTS
from tkinter import ttk
from playsound import playsound
import speech_recognition as sr
from googletrans import Translator  
#from deep_translator import GoogleTranslator
from google.transliteration import transliterate_text

# Load language codes from JSON file
def load_language_codes():
    with open('language_codes.json', 'r') as f:
        data = json.load(f)
    return data['codes'], data['names']

language_codes, language_names = load_language_codes()

# Create the main tkinter window instance
win = tk.Tk()

# Set the window size and title
win.geometry("700x450")
win.title("Real-Time Voice Translator")

# Function to update the translated text
def update_translation():
    global keep_running

    if keep_running:
        recognizer = sr.Recognizer()  # Create a recognizer instance

        with sr.Microphone() as source:
            print("Speak Now!\n")
            audio = recognizer.listen(source)

            try:
                speech_text = recognizer.recognize_google(audio)

                # Handle transliteration if input language is not English or auto
                if input_lang.get() not in ('auto', 'en'):
                    speech_text_transliteration = transliterate_text(speech_text, lang_code=input_lang.get())
                else:
                    speech_text_transliteration = speech_text

                # Update input text with recognized/transliterated speech
                input_text.insert(tk.END, f"{speech_text_transliteration}\n")

                # Exit if user says "exit" or "stop"
                if speech_text.lower() in {'exit', 'stop'}:
                    keep_running = False
                    return

                # Translate the recognized text
                translated_text = GoogleTranslator(source=input_lang.get(), target=output_lang.get()).translate(text=speech_text_transliteration)

                # Generate and play audio for the translated text
                voice = gTTS(translated_text, lang=output_lang.get())
                voice.save('voice.mp3')
                playsound('voice.mp3')
                os.remove('voice.mp3')

                # Update output text with translated text
                output_text.insert(tk.END, translated_text + "\n")

            except sr.UnknownValueError:
                output_text.insert(tk.END, "Could not understand!\n")
            except sr.RequestError:
                output_text.insert(tk.END, "Could not request from Google!\n")

        # Schedule the next update after 100 milliseconds
        win.after(100, update_translation)

# Function to start the translation process
def run_translator():
    global keep_running

    if not keep_running:
        keep_running = True
        # Use threading for efficient CPU usage
        update_translation_thread = threading.Thread(target=update_translation)
        update_translation_thread.start()

# Function to stop the translation process
def kill_execution():
    global keep_running
    keep_running = False

# Create labels and text boxes for recognized and translated text
input_label = tk.Label(win, text="Recognized Text ⮯")
input_label.pack()
input_text = tk.Text(win, height=5, width=50)
input_text.pack()

output_label = tk.Label(win, text="Translated Text ⮯")
output_label.pack()
output_text = tk.Text(win, height=5, width=50)
output_text.pack()

blank_space = tk.Label(win, text="")
blank_space.pack()

# Create dropdown menus for input and output languages with labels
def update_input_lang_code(event):
    selected_language_name = event.widget.get()
    selected_language_code = language_codes[selected_language_name]
    # Update the selected language code for input language
    input_lang.set(selected_language_code)

input_lang_label = tk.Label(win, text="Select Input Language:")
input_lang_label.pack()

input_lang = ttk.Combobox(win, values=language_names)
input_lang.bind("<<ComboboxSelected>>", lambda e: update_input_lang_code(e))
# Set default language code for input (can be 'auto' for automatic detection)
if input_lang.get() == "":
    input_lang.set("auto")
input_lang.pack()

down_arrow = tk.Label(win, text="▼")
down_arrow.pack()

output_lang_label = tk.Label(win, text="Select Output Language:")
output_lang_label.pack()

output_lang = ttk.Combobox(win, values=language_names)
def update_output_lang_code(event):
    selected_language_name = event.widget.get()
    selected_language_code = language_codes[selected_language_name]
    # Update the selected language code for output language
    output_lang.set(selected_language_code)

output_lang.bind("<<ComboboxSelected>>", lambda e: update_output_lang_code(e))
# Set default language code for output (English)
if output_lang.get() == "":
    output_lang.set("en")
output_lang.pack()

blank_space = tk.Label(win, text="")
blank_space.pack()

# Create buttons for starting, stopping translation
keep_running = False  # Flag to control translation loop

run_button = tk.Button(win, text="Start Translation", command=run_translator)
run_button.place(relx=0.25, rely=0.9, anchor="c")

kill_button = tk.Button(win, text="Kill Execution", command=kill_execution)
kill_button.place(relx=0.5, rely=0.9, anchor="c")

# Run the main application loop
win.mainloop()