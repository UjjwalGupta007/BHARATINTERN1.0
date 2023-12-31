import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox

# Function to translate text using Google Translate API
def translate_text():
    translator = Translator()
    translated = translator.translate(text=entry_text.get(), dest=dest_lang.get())
    output_text.delete(1.0, tk.END)  # Clear the output box before adding the translation
    output_text.insert(tk.END, translated.text)
    status_var.set("Translation Successful")

# Function to clear the input and output text fields
def clear_text():
    entry_text.delete(0, tk.END)
    output_text.delete(1.0, tk.END)
    status_var.set("Text cleared")

# Function to copy the translated text to the clipboard
def copy_text():
    root.clipboard_clear()
    root.clipboard_append(output_text.get(1.0, tk.END))
    status_var.set("Text copied to clipboard")

# Create the main root window
root = tk.Tk()
root.geometry('1100x400')
root.title('Language Translator by UJJWALGUPTA X BharatIntern')

# Create a themed style with a tint effect
style = ThemedStyle(root)
style.set_theme("radiance")  # You can try other themes like "arc", "breeze", etc.

# Input Frame
input_frame = ttk.Frame(root, width=500, height=250, borderwidth=2)
input_frame.pack(side=tk.LEFT, padx=10, pady=10)

# Output Frame
output_frame = ttk.Frame(root, width=500, height=250, borderwidth=2)
output_frame.pack(side=tk.RIGHT, padx=10, pady=10)

# Input Frame Widgets
# Title label
ttk.Label(input_frame, text="Language Translator", font="Arial 25 bold").pack(pady=20)

# Label and Entry widget for entering the text to be translated
ttk.Label(input_frame, text="Enter Text", font='Arial 15 bold').pack()
entry_text = ttk.Entry(input_frame, width=60)
entry_text.pack(pady=10)
entry_text.focus_set()

# Combobox for selecting the destination language for translation
languages = list(LANGUAGES.values())
dest_lang = ttk.Combobox(input_frame, values=languages, width=25)
dest_lang.set('Choose language')
dest_lang.pack(pady=10)

# Button to trigger the translation
translate_btn = ttk.Button(input_frame, text='Translate', command=translate_text)
translate_btn.pack(pady=10)

# Button to clear the input and output text fields
clear_btn = ttk.Button(input_frame, text='Clear', command=clear_text)
clear_btn.pack(pady=5)

# Output Frame Widgets
# Title label
ttk.Label(output_frame, text="Output", font='Arial 15 bold').pack()

# Text widget to display the translated text
output_text = tk.Text(output_frame, font='Arial 10', wrap=tk.WORD, padx=5, pady=5, width=50, height=5)
output_text.pack(pady=10)

# Button to copy the translated text to the clipboard
copy_btn = ttk.Button(output_frame, text='Copy', command=copy_text)
copy_btn.pack(pady=5)

# Apply shadow effect to the input frame using PIL (pillow)
input_frame_shadow = Image.open("D:\download.png")  # Replace with your shadow image
input_frame_shadow = ImageTk.PhotoImage(input_frame_shadow)
shadow_label = tk.Label(root, image=input_frame_shadow)
shadow_label.place(x=400, y=100)

# Status Bar
status_var = tk.StringVar()
status_bar = ttk.Label(root, textvariable=status_var, font='Arial 10 italic', anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# Start the main event loop
root.mainloop()
