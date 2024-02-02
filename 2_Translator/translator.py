from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
import pyperclip

def translate_text(event=None):
    # Get selected source and destination languages
    src_lang = combo_in.get()
    dest_lang = combo_out.get()

    # Get text to translate
    text_to_translate = in_txt.get(1.0, END).strip()

    # Create Translator object and perform translation
    translator = Translator()
    translated_text = translator.translate(text_to_translate, src=src_lang, dest=dest_lang).text

    # Display translated text
    out_txt.config(state="normal")
    out_txt.delete(1.0, END)
    out_txt.insert(END, translated_text)
    out_txt.config(state="disabled")

def swap_languages():
    # Get selected source and destination languages
    src_lang = combo_in.get()
    dest_lang = combo_out.get()

    # Swap languages in combo boxes
    combo_in.set(dest_lang)
    combo_out.set(src_lang)

    # Swap text in input and output text areas
    in_txt_content = in_txt.get(1.0, END)
    out_txt_content = out_txt.get(1.0, END)

    in_txt.delete(1.0, END)
    in_txt.insert(END, out_txt_content.strip())

    out_txt.config(state="normal")
    out_txt.delete(1.0, END)
    out_txt.insert(END, in_txt_content.strip())
    out_txt.config(state="disabled")

def clear_text():
    # Clear text in input and output text areas
    in_txt.delete(1.0, END)
    out_txt.config(state="normal")
    out_txt.delete(1.0, END)
    out_txt.config(state="disabled")

def copy_to_clipboard():
    # Copy translated text to clipboard
    translated_text = out_txt.get(1.0, END)
    pyperclip.copy(translated_text)

# Create main window
window = Tk()
window.title("Language translator using googletrans library")
window.geometry("600x740")
window.config(bg="black")  # Set background color

# Header label
head_txt = Label(window, text="Translator", font=("Montserrat", 24, 'bold'), fg="white", bg="#004FFF")
head_txt.place(x=150, y=20, height=60, width=300)

# Frame to contain widgets
frame = Frame(window).pack(side=BOTTOM)

# Label for input text
head_txt1 = Label(window, text="Enter text", font=("Montserrat", 22, 'bold'), fg="#5ADBFF", bg="black")
head_txt1.place(x=20, y=108, height=30, width=150)

# Input text area
in_txt = Text(frame, font=("Montserrat", 20, 'bold'), wrap=WORD)
in_txt.place(x=20, y=145, height=200, width=540)

# Label for translated text
head_txt2 = Label(window, text="Translation", font=("Montserrat", 22, 'bold'), fg="#5ADBFF", bg="black")
head_txt2.place(x=20, y=448, height=30, width=180)

# Translated text area
out_txt = Text(frame, font=("Montserrat", 20, "bold"), wrap=WORD, state="disabled")
out_txt.place(x=20, y=485, height=200, width=540) 

# Combo box for source language
combo_in = ttk.Combobox(frame, values=list(LANGUAGES.values()), font=("Montserrat", 14))
combo_in.place(x=20, y=365, height=50, width=150)  # Adjusted width
combo_in.set('english')

# Button to translate
translate_button = Button(frame, text="Translate", relief=RAISED, command=translate_text, font=("Montserrat", 16), bg="#007BFF", fg="white")
translate_button.place(x=180, y=365, height=50, width=150)  # Adjusted position and width

# Combo box for destination language
combo_out = ttk.Combobox(frame, values=list(LANGUAGES.values()), font=("Montserrat", 14))
combo_out.place(x=350, y=365, height=50, width=150)  # Adjusted position and width
combo_out.set('hindi')

# Button to swap languages with up and down arrow symbols
swap_button = Button(frame, text="⬆⬇", relief=RAISED, command=swap_languages, font=("Montserrat", 14), bg="#007BFF", fg="white")
swap_button.place(x=520, y=365, height=50, width=40)  # Adjusted position and width

# Button to clear text
clear_button = Button(frame, text="Clear", relief=RAISED, command=clear_text, font=("Montserrat", 14), bg="#DC3545", fg="white")
clear_button.place(x=20, y=700, height=30, width=80)

# Button to copy to clipboard
copy_button = Button(frame, text="Copy", relief=RAISED, command=copy_to_clipboard, font=("Montserrat", 14), bg="#007BFF", fg="white")
copy_button.place(x=500, y=700, height=30, width=60)

# Start the Tkinter event loop
window.mainloop()