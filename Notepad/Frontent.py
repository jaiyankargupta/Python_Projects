import tkinter as tk
from tkinter import filedialog, messagebox
import speech_recognition as sr

class NotepadBackend:
    def __init__(self):
        pass
    
    def new_file(self, textarea):
        textarea.delete(1.0, tk.END)
    
    def open_file(self, textarea):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
            textarea.delete(1.0, tk.END)
            textarea.insert(1.0, content)
    
    def save_file(self, textarea):
        content = textarea.get(1.0, tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(content)
    
    def quit_app(self, root):
        root.destroy()
    
    def cut_text(self, textarea):
        textarea.event_generate("<<Cut>>")
    
    def copy_text(self, textarea):
        textarea.event_generate("<<Copy>>")
    
    def paste_text(self, textarea):
        textarea.event_generate("<<Paste>>")
    
    def voice_to_text(self, textarea):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak something...")
            audio = recognizer.listen(source)
        
        try:
            text = recognizer.recognize_google(audio)
            textarea.insert(tk.END, text)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

backend = NotepadBackend()
