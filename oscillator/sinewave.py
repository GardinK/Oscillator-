####make two new classes that inheret from wave,,, one for sine and one for square,,, and comments

import math
from oscillatorwave import Wave

class Sine(Wave):
    def __init__(self, amp, wavelen, freq, phase):
         super().__init__(amp, wavelen, freq, phase)
    
sine = Sine(32,11,25,15)

print(sine.getamp())