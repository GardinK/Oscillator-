####make two new classes that inheret from wave,,, one for sine and one for square,,, and comments
import numpy as np
import math
from oscillatorwave import Wave

class Sine(Wave):
    def __init__(self, amp, wavelen, freq, phase):
         super().__init__(amp, wavelen, freq, phase)

    def generate_waveform(self, sample_rate, seconds):
        t = np.linspace(0, seconds, int(sample_rate * seconds), endpoint=False)
        waveform = self.amp * np.sin(2 * np.pi * self.freq * t + self.phase)
        return waveform.astype(np.int16)
    
sine = Sine(32,11,25,15)

print(sine.getamp())