import thinkdsp
import thinkplot
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile # get the api

audio = thinkdsp.read_wave("blood_audio.wav")
# plot the wave of the input audio
audio.plot()
thinkplot.show()

audio_spec = audio.make_spectrum()
# get the spectrum of the input audio
audio_spec.plot()
thinkplot.show()

audio_spec.low_pass(cutoff=230, factor=0.01)
# Apply low pass filter for the spectrum to filter out the audio into an audible range.
# Attenuates all frequencies above 600 by 99%
wave = audio_spec.make_wave()
# convert spectrum back to a wave
wave.write(filename='test6_1.wav')
# write the wave into an audio file
wave.play('test6_1.wav')
# play the filtered audio

low_wave = wave.make_spectrum()
# spectrum after first low pass filter is applied
low_wave.plot()
thinkplot.show()

low_wave.high_pass(cutoff=80, factor=0.01)
# Apply high pass filter for the low passed spectrum to get into an audible range.
wave2 = low_wave.make_wave()
# convert spectrum back to a wave
wave2.write(filename='test6_2.wav')
wave2.play('test6_2.wav')

high_wave = wave2.make_spectrum()
# spectrum after first high pass filter is applied
high_wave.plot()
# thinkplot.show()


def apply_transfer(signal, transfer, interpolation = 'linear'):

    constant = np.linspace(-1, 1, len(transfer))
    interpolator = interp1d(constant, transfer, interpolation)
    return interpolator(signal)


# hard limiting


def limiter(x, treshold=0.8):
    transfer_len = 1000
    transfer = np.concatenate([ np.repeat(-1, int(((1-treshold)/2)*transfer_len)),
                                np.linspace(-1, 1, int(treshold*transfer_len)),
                                np.repeat(1, int(((1-treshold)/2)*transfer_len)) ])
    return apply_transfer(x, transfer)

# smooth compression: if factor is small, its near linear, the bigger it is the
# stronger the compression


def arctan_compressor(x, factor=2):
    constant = np.linspace(-1, 1, 1000)
    transfer = np.arctan(factor * constant)
    transfer /= np.abs(transfer).max()
    return apply_transfer(x, transfer)

sr,x = wavfile.read("test6_2.wav")
x = x / np.abs(x).max() # x scale between -1 and 1

x2 = limiter(x)
x2 = np.int16(x2 * 32767)
wavfile.write("output_limit_6.wav", sr, x2)

x3 = arctan_compressor(x)
x3 = np.int16(x3 * 32767)
wavfile.write("output_comp_6.wav", sr, x3)

fs, data = wavfile.read('output_comp_6.wav') # load the data
# a = data.T[0] # this is a two channel soundtrack, I get the first track
# b =[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
c = fft(data) # calculate fourier transform (complex numbers list)
d = len(c)/2  # you only need half of the fft list (real signal symmetry)
plt.plot(abs(c))
plt.show()





