import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# Path to the fart sound
FART_SOUND = os.path.join(os.path.dirname(__file__), 'fart.mp3')
POOP_IMAGE = os.path.join(os.path.dirname(__file__), 'poop.png')

def play_fart():
    try:
        pygame.mixer.music.load(FART_SOUND)
        pygame.mixer.music.play()
    except Exception as e:
        messagebox.showerror("Error", f"Could not play sound: {e}")

root = tk.Tk()
root.title("Poop Button App")
root.geometry("300x350")

# Load and display the poop image
poop_img = PhotoImage(file=POOP_IMAGE)
img_label = tk.Label(root, image=poop_img)
img_label.pack(pady=(20, 10))

button = tk.Button(root, text="poop", font=("Comic Sans MS", 24), command=play_fart, bg="#8B4513", fg="white", activebackground="#A0522D", activeforeground="white")
button.pack(expand=True)

root.mainloop() 