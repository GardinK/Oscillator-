import streamlit as st
import numpy as np
from knobs import knob
from matplotlib.pyplot import * 
from sqrwave import Sqr
from sinewave import Sine
from trianglewav import Tri
from sawwave import Saw
from scipy.io.wavfile import write
import io

SAMPLE_RATE = 44100  # 44.1 kHz sample rate
SECONDS = 2  # Duration of the audio
MIN_VALUE = 0
MAX_VALUE = 100


st.set_page_config(
    page_title='TyroOsc',
    layout = 'wide', 
    initial_sidebar_state = 'auto'
    )
 
with st.container():
    ampcolumn, wavcolumn, freqcolumn, phasecolumn = st.columns(4)
    with ampcolumn:
        AMP = knob(
        min_value=MIN_VALUE,
        max_value=MAX_VALUE,
        step=1,
        size="small",
        initial_value=0,
        title = "amp",
        knob_type = '2'
    )
        
    with wavcolumn:
        WAVLEN = knob(
        min_value=MIN_VALUE,
        max_value=MAX_VALUE,
        step=1,
        size="small",
        initial_value=0,
        title = "wavlen",
        knob_type = '2'
    )
        
    with freqcolumn:
        FREQ = knob(
        min_value=1,
        max_value=MAX_VALUE,
        step=1,
        size="small",
        initial_value=1,
        title = 'freq',
        knob_type = '2'
        )
        
    with phasecolumn:
        PHASE = knob(
        min_value=MIN_VALUE,
        max_value=MAX_VALUE,
        step=1,
        size="small",
        initial_value=0,
        title = 'phase',
        knob_type = '2'    
    )
        

choice = st.radio(
    "Wavetype",
    ["Sine","Square","Sawtooth","Triangle"],
    index = None
)

if choice == "Square":
 
    square = Sqr(AMP, WAVLEN, FREQ, PHASE)
 
    st.write(square.getall())

    audio_data = square.generate_waveform(SAMPLE_RATE, SECONDS)
 
    st.audio(audio_data, format="wav", start_time=0, sample_rate = SAMPLE_RATE, end_time= SECONDS, loop=True, autoplay=False)


if choice == "Sine":
 
    sine = Sine(AMP, WAVLEN, FREQ, PHASE)
 
    st.write(sine.getall())

    audio_data = sine.generate_waveform(SAMPLE_RATE, SECONDS)
 
    st.audio(audio_data, format="wav", start_time=0, sample_rate = SAMPLE_RATE, end_time= SECONDS, loop=True, autoplay=False)


if choice == "Sawtooth":
 
    saw = Saw(AMP, WAVLEN, FREQ, PHASE)
 
    st.write(saw.getall())

    audio_data = saw.generate_waveform(SAMPLE_RATE, SECONDS)
 
    st.audio(audio_data, format="wav", start_time=0, sample_rate = SAMPLE_RATE, end_time= SECONDS, loop=True, autoplay=False)


if choice == "Triangle":
 
    triangle = Tri(AMP, WAVLEN, FREQ, PHASE)
 
    st.write(triangle.getall())

    audio_data = triangle.generate_waveform(SAMPLE_RATE, SECONDS)
 
    st.audio(audio_data, format="wav", start_time=0, sample_rate = SAMPLE_RATE, end_time= SECONDS, loop=True, autoplay=False)
