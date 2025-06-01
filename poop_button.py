#!/usr/bin/env python3
"""
A simple GUI application with poop and pee buttons that play sounds when clicked.
"""

# Standard library imports
import os
import sys
import subprocess
from pathlib import Path

# Third-party imports
import tkinter as tk
from tkinter import messagebox, PhotoImage

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

# Resource paths
FART_SOUND = resource_path('fart.mp3')
PEE_SOUND = resource_path('pee.mp3')
POOP_IMAGE = resource_path('poop.png')
PEE_IMAGE = resource_path('pee.png')

def play_sound(sound_file):
    """Play a sound file using the system's default audio player"""
    try:
        if sys.platform.startswith('linux'):
            subprocess.Popen(['paplay', sound_file])
        elif sys.platform.startswith('win'):
            os.startfile(sound_file)
        elif sys.platform.startswith('darwin'):
            subprocess.Popen(['afplay', sound_file])
    except Exception as e:
        messagebox.showerror("Error", f"Could not play sound: {e}")

def play_fart():
    play_sound(FART_SOUND)

def play_pee():
    play_sound(PEE_SOUND)

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