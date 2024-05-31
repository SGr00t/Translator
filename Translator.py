import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator
import os

class TranslatorApp:
    def __init__(self):
        self.translator = Translator()

    def translate_text(self, text, target_language):
        translation = self.translator.translate(text, dest=target_language)
        return translation.text

    # def text_to_speech(self, text, lang):
    #     tts = gTTS(text=text, lang=lang)
    #     # tts.save("output.mp3")
    #     # os.system("start output.mp3")

    # def speech_to_text(self):
    #     recognizer = sr.Recognizer()
    #     with sr.Microphone() as source:
    #         print("Speak something...")
    #         audio = recognizer.listen(source)
    #         try:
    #             text = recognizer.recognize_google(audio)
    #             print("You said:", text)
    #             return text
    #         except sr.UnknownValueError:
    #             print("Could not understand audio.")
    #         except sr.RequestError as e:
    #             print("Could not request results; {0}".format(e))

if __name__ == "__main__":
    app = TranslatorApp()

    while True:
        print("1. Translate Text")
        # print("2. Speech to Text")
        # print("3. Text to Speech")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            text = input("Enter text to translate: ")
            target_language = input("Enter target language (e.g., hi for Hindi, bn for Bengali): ")
            translated_text = app.translate_text(text, target_language)
            print("Translated text:", translated_text)
        
        # elif choice == "2":
        #     text = app.speech_to_text()
        #     if text:
        #         print("You said:", text)
        
        # elif choice == "3":
        #     text = input("Enter text for speech: ")
        #     lang = input("Enter language code (e.g., en for English, es for Spanish): ")
        #     app.text_to_speech(text, lang)
        
        elif choice == "2":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")
