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
    @property
    def amp(self):
        return self._amp
    
    @amp.setter
    def amp(self, value):
        if value < 0:
            raise ValueError("Amplitude cannot be negative.")
        self._amp = value

    # Getter and Setter for frequency (freq)
    @property
    def freq(self):
        return self._freq
    
    @freq.setter
    def freq(self, value):
        if value <= 0:
            raise ValueError("Frequency must be greater than 0.")
        self._freq = value
        self._speed = 1 / value  # Recalculate speed when frequency changes

    # Getter and Setter for wavelength (wavelen)
    @property
    def wavelen(self):
        return self._wavelen
    
    @wavelen.setter
    def wavelen(self, value):
        if value <= 0:
            raise ValueError("Wavelength must be greater than 0.")
        self._wavelen = value

    # Getter and Setter for phase (phase)
    @property
    def phase(self):
        return self._phase
    
    @phase.setter
    def phase(self, value):
        if value < 0 or value >= 360:
            raise ValueError("Phase should be between 0 and 360 degrees.")
        self._phase = (value / 360) * 2 * math.pi  # Convert phase to radians

    # Optional: Getter for speed (calculated from frequency)
    @property
    def speed(self):
        return self._speed
