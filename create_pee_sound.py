import numpy as np
from scipy.io import wavfile

# Create a simple water stream sound
duration = 2.0  # seconds
sample_rate = 44100
t = np.linspace(0, duration, int(sample_rate * duration))

# Base frequency for water sound
freq = 1000
noise = np.random.normal(0, 1, len(t))
filtered_noise = np.convolve(noise, np.ones(50)/50, mode='same')
water_sound = np.sin(2 * np.pi * freq * t) * filtered_noise * 0.5

# Normalize and convert to 16-bit integer
water_sound = np.int16(water_sound * 32767)

# Save the sound
wavfile.write('pee.wav', sample_rate, water_sound) 