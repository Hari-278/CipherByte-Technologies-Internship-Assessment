# RECORD YOUR VOICE
# Python can be used to perform a variety of tasks. One of them is creating a voice recorder. We can use python's sounddevice module to record and play audio. This module along with the wavio or the scipy module provides a way to save recorded audio.


import sounddevice as sd
import numpy as np
import wavio

def record_audio(duration, filename):
    print("Recording...")
    # Record audio
    recording = sd.rec(int(duration * 44100), samplerate=44100, channels=2, dtype='int16')
    sd.wait()
    print("Recording stopped.")

    # Save audio to WAV file
    wavio.write(filename, recording, 44100, sampwidth=2)

    print(f"Audio saved as {filename}")

if __name__ == "__main__":
    duration = int(input("Enter duration of recording (in seconds): "))
    filename = input("Enter filename to save recording (e.g., recording.wav): ")

    record_audio(duration, filename)
