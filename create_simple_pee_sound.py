import wave
import struct
import random
import math

# Create a new wave file
sampleRate = 44100
duration = 2.0  # seconds
nframes = int(sampleRate * duration)
nchannels = 1
sampwidth = 2

# Create the wave file
wav_file = wave.open("pee.wav", "w")
wav_file.setnchannels(nchannels)
wav_file.setsampwidth(sampwidth)
wav_file.setframerate(sampleRate)

# Generate a more realistic water stream sound
for i in range(nframes):
    t = i / sampleRate
    
    # Create multiple frequency components for a more natural sound
    # Base water stream frequencies
    f1 = 200 + random.uniform(-10, 10)  # Low frequency water movement
    f2 = 400 + random.uniform(-20, 20)  # Mid frequency splashing
    f3 = 800 + random.uniform(-40, 40)  # High frequency droplets
    
    # Amplitude modulation for natural variation
    amp_mod = 0.7 + 0.3 * math.sin(2 * math.pi * 2 * t)  # Slow amplitude variation
    
    # Combine frequencies with different amplitudes
    value = (
        0.4 * math.sin(2 * math.pi * f1 * t) * random.uniform(0.8, 1.0) +  # Base stream
        0.3 * math.sin(2 * math.pi * f2 * t) * random.uniform(0.7, 0.9) +  # Splashing
        0.2 * math.sin(2 * math.pi * f3 * t) * random.uniform(0.6, 0.8)    # Droplets
    )
    
    # Apply amplitude modulation and convert to 16-bit integer
    value = int(32767 * 0.5 * value * amp_mod)
    
    # Ensure we don't exceed 16-bit bounds
    value = max(-32767, min(32767, value))
    
    packed_value = struct.pack('h', value)
    wav_file.writeframes(packed_value)

wav_file.close()

# Convert wav to mp3 using ffmpeg
import os
os.system('ffmpeg -i pee.wav -filter:a "volume=0.5" pee.mp3') 