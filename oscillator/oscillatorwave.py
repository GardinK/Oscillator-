#### Waves Class
import math 

class Wave:
  def __init__(self, amp, wavelen, freq, phase):
    ## Define Attributes
    self.amp = amp
    self.freq = freq
    self.wavelen = wavelen
    self.speed = 1/freq
    self.phase = (phase / 360) * 2 * math.pi

  # TODO: define 4 getters and 4 setters for amp/freq/wavelen/phase
  
  def getamp(self):
      return self.amp
    
  def getfreq(self):
      return self.freq
  
  def getwavelen(self):
      return self.wavelen
   
  def getspeed(self):
      return self.speed
    
  def getphase(self):
      return self.phase
   
  def setamp(self,x):
      self.amp = x
    
if __name__ == "__main__":

    sine = Wave(32,12,42,11)

    print(sine.getamp())

    sine.amp = 52 

    print(sine.amp)

    ####make two new classes that inheret from wave,,, one for sine and one for square,,, and comments

