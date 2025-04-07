import math
import numpy as np
from oscillatorwave import Wave

class Saw(Wave):
    def __init__(self, amp, wavelen, freq, phase):
        super().__init__(amp, wavelen, freq, phase)

    def generate_waveform(self, sample_rate, seconds):
        t = np.linspace(0, seconds, int(sample_rate * seconds), endpoint=False)
        waveform = self.amp * (2 * (t * self.freq - np.floor(t * self.freq + 0.5)) + self.phase) 
        return waveform.astype(np.int16)