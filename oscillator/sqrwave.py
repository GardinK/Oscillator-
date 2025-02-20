####make two new classes that inheret from wave,,, one for sine and one for square,,, and comments

import math
from oscillatorwave import Wave

class Sqr(Wave):
    def __init__(self, amp, wavelen, freq, phase):
        super().__init__(amp, wavelen, freq, phase)
    
square = Sqr(23,11,51,52)

print(square.getamp())