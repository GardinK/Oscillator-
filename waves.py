#### Waves Class

class Wave:
  def _init_(self, amp, wavelen, freq, phase):
    ## Define Attributes
    self.amp = amp
    self.freq = freq
    self.wavelen = wavelen
    self.speed = 1/freq
    self.phase = (phase / 360) * 2 * math.pi

  # TODO: define 4 getters and 4 setters for amp/freq/wavelen/phase
