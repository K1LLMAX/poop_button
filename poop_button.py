import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# Path to the fart sound
FART_SOUND = os.path.join(os.path.dirname(__file__), 'fart.mp3')
PEE_SOUND = os.path.join(os.path.dirname(__file__), 'pee.mp3')
POOP_IMAGE = os.path.join(os.path.dirname(__file__), 'poop.png')
PEE_IMAGE = os.path.join(os.path.dirname(__file__), 'pee.png')

def play_fart():
    try:
        pygame.mixer.music.load(FART_SOUND)
        pygame.mixer.music.play()
    except Exception as e:
        messagebox.showerror("Error", f"Could not play sound: {e}")

def play_pee():
    try:
        pygame.mixer.music.load(PEE_SOUND)
        pygame.mixer.music.play()
    except Exception as e:
        messagebox.showerror("Error", f"Could not play sound: {e}")

root = tk.Tk()
root.title("Poop Button App")
root.geometry("600x350")  # Made wider to accommodate both buttons

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(expand=True, fill='both')

# Left side - Poop button
left_frame = tk.Frame(button_frame)
left_frame.pack(side='left', expand=True, fill='both')

poop_img = PhotoImage(file=POOP_IMAGE)
poop_img_label = tk.Label(left_frame, image=poop_img)
poop_img_label.pack(pady=(20, 10))

poop_button = tk.Button(left_frame, text="poop", font=("Comic Sans MS", 24), command=play_fart, 
                       bg="#8B4513", fg="white", activebackground="#A0522D", activeforeground="white")
poop_button.pack(expand=True)

# Right side - Pee button
right_frame = tk.Frame(button_frame)
right_frame.pack(side='right', expand=True, fill='both')

pee_img = PhotoImage(file=PEE_IMAGE)
pee_img_label = tk.Label(right_frame, image=pee_img)
pee_img_label.pack(pady=(20, 10))

pee_button = tk.Button(right_frame, text="pee", font=("Comic Sans MS", 24), command=play_pee,
                      bg="#FFFF00", fg="black", activebackground="#FFE600", activeforeground="black")
pee_button.pack(expand=True)

root.mainloop() 