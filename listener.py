import sounddevice as sd
import soundfile as sf
from scipy.fft import fft
import numpy as np
from phone_gui import PhoneGui
from scipy.io.wavfile import write
import tkinter as tk

# Listen for 10 seconds and record all the numbers it hears
# Process:
#   1. take the recording and run fft on it
#   2. take only those measured freqs that are above a certain threshold (say, 300 Hz)
#   3. Check

# Key: DTMF tones mapped to accepted frequencies
phone_gui = PhoneGui('test')

dtmf_freqs = {}

dtmf_freqs[1] = ((695, 696, 697, 698, 699), (1207, 1208, 1209, 1210, 1211))
dtmf_freqs[2] = ((695, 696, 697, 698, 699), (1334, 1335, 1336, 1337, 1338))
dtmf_freqs[3] = ((695, 696, 697, 698, 699), (1475, 1476, 1477, 1478, 1479))

dtmf_freqs[4] = ((768, 769, 770, 771, 772), (1207, 1208, 1209, 1210, 1211))
dtmf_freqs[5] = ((768, 769, 770, 771, 772), (1334, 1335, 1336, 1337, 1338))
dtmf_freqs[6] = ((768, 769, 770, 771, 772), (1475, 1476, 1477, 1478, 1479))

dtmf_freqs[7] = ((850, 851, 852, 853, 854), (1207, 1208, 1209, 1210, 1211))
dtmf_freqs[8] = ((850, 851, 852, 853, 854), (1334, 1335, 1336, 1337, 1338))
dtmf_freqs[9] = ((850, 851, 852, 853, 854), (1475, 1476, 1477, 1478, 1479))

dtmf_freqs['*'] = ((939, 940, 941, 942, 943), (1207, 1208, 1209, 1210, 1211))
dtmf_freqs[0] = ((939, 940, 941, 942, 943), (1334, 1335, 1336, 1337, 1338))
dtmf_freqs['#'] = ((939, 940, 941, 942, 943), (1475, 1476, 1477, 1478, 1479))

sec = 1
threshold = 100
fs = 44100

# Next step: Make it work in real time
y = []
full_num = []
count = 0

while count < 10:
    rec = sd.rec(int(sec * fs), samplerate=fs, channels=1)
    sd.wait()
    rec = rec.squeeze()

    y = fft(rec)
    y = np.abs(y)

    detected_freqs = [int(i / sec) for i in range(len(y)) if y[i] >= threshold]

    nums = [key for key in dtmf_freqs if any(x in dtmf_freqs[key][0] for x in detected_freqs) and any(
        x in dtmf_freqs[key][1] for x in detected_freqs)]

    print(nums)

    count += len(nums)
    full_num.extend(nums)

phone_gui.update(full_num)
