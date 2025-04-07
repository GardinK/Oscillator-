####make two new classes that inheret from wave,,, one for sine and one for square,,, and comments

import math
import numpy as np
from oscillatorwave import Wave

class Sqr(Wave):
    def __init__(self, amp, wavelen, freq, phase):
        super().__init__(amp, wavelen, freq, phase)

    def generate_waveform(self, sample_rate, seconds):
        t = np.linspace(0, seconds, int(sample_rate * seconds), endpoint=False)
        waveform = self.amp * np.sign(np.sin(2 * np.pi * self.freq * t + self.phase))
        return waveform.astype(np.int16)

square = Sqr(23,11,51,52)

print(square.getamp())