# Oscillator- 
Human hearing is limited to 20 and 20,000 hertz 

Common sample rate for audio == 44.1 kHz --> 44,100 Hz 

Bit depth refers to the amount of information stored in each individual data point (like a pixel in an image or a sample in audio)

Bitrate refers to the rate at which data is transmitted over time, meaning how much information is transferred per second

The human ear can hear sounds up to 90dB

Generators
	A special type of function which does not return a single value: it returns an iterator object with a sequence of values. 
	Unlike the `return` statement, which terminates a function and returns a value, the `yield` statement suspends the function's execution and returns a value. The function's state is saved, allowing it to resume execution from where it left off the next time it's called. 

Iterators
	An iterator is an object that can be iterated upon. Thus, iterators contain a countable number of values.
	


EFFICIENCY ! ! !
==Using generators and iterators we can generate infinite streams of integers== which can be fed to some output like a speaker or a file, without these features the memory requirements would be very high.

Changing the amplitude would change the volume of the specific wave function (Or add vibrato) 0 <--> 1


PHASE

**Phase is the position of a point in time on a cycle of a waveform**

Phases from left and right output oscillating at the same time in the same place cancel each other out effectively causing silence.
	What are constructive and destructive interference? **When 2 or more waveforms mix with each other, depending on their alignment the resulting level either increases or decreases. If the resulting level decreases, it is destructive interference. But if the resulting level increases, it is constructive interference.**

If there is only a single oscillator in use, **the phase does not have any significance unless there is a moderate to fast modulation**. However, the role of Phase becomes very important if there are more than 2 oscillators or sound sources playing. **That’s because of the constructive and destructive interference of waveforms.



*Build an oscillator that allows change to three parameters on the fly*

Metaclasses 
	 **metaclasses specify the behaviors of classes and their instances**

	ABC (Abstract Base classes)

An Abstract Base Class in computer science is **a class that defines the interface which other classes must implement**.



In Python, `@property` is a decorator that allows you to define methods that act like attributes. This means you can access them like regular attributes, but they can have additional logic behind them.

Getter

Setter

Deleter

*random*
	def get_sin_oscillator(freq, amp=1, phase=0, sample_rate=44100):
    """
         
    Parameters
    ----------
    num_terms : int
        The number of terms inside ()
    precision : int
        The number of digits after the decimal point
         
    Returns 


    """
    phase = (phase / 360) * 2 * math.pi
    
    
    increment = (2 * math.pi * freq)/ sample_rate                         #Scalar measure rate of change of a sine function
                                                                              #w(increment) = (2pi)/T
   
    return (math.sin(v) for v in itertools.count(start=0, step=increment))



	osc = get_sin_oscillator(freq=1, sample_rate=512)                         #First 512 samples
	samples = [next(osc) for i in range(512)]



Works Cited
	https://www.adobe.com/uk/creativecloud/video/discover/audio-sampling.html#:~:text=Sample%20rates%20are%20usually%20measured,can%20create%20more%20accurate%20recordings.
	
	https://python.plainenglish.io/making-a-synth-with-python-oscillators-2cb8e68e9c3b

	https://www.datacamp.com/tutorial/python-iterators-generators-tutorial

	https://www.samplelogic.com/audio-basics-what-is-phase-in-synthesizers-phase-explained/#:~:text=Phase%20is%20the%20position%20of,SWC%20starts%20from%20the%20end

https://www.reddit.com/r/learnpython/comments/ukdpmc/having_a_hard_time_understanding_getters_and/ -@fiddle_n
