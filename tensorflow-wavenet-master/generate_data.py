import os
import wave
import audioop

s1 = wave.open("s1.wav")
fragment1 = wav.readframes(wav.getnframes()), wav.getsampwidth())
print("It worked")