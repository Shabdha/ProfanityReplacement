from pydub import AudioSegment
from pydub.playback import play
#import pyaudio
import wave
import fleep
#recording

# chunk = 1024  # Record in chunks of 1024 samples
# sample_format = pyaudio.paInt16  # 16 bits per sample
# channels = 2
# fs = 44100  # Record at 44100 samples per second
# seconds = 10
# filename = "outputRecord.wav"
#
# p = pyaudio.PyAudio()  # Create an interface to PortAudio
#
# print('Recording')
#
# stream = p.open(format=sample_format,
#                 channels=channels,
#                 rate=fs,
#                 frames_per_buffer=chunk,
#                 input=True)
#
# frames = []  # Initialize array to store frames
#
# # Store data in chunks for 3 seconds
# for i in range(0, int(fs / chunk * seconds)):
#     data = stream.read(chunk)
#     frames.append(data)
#
# # Stop and close the stream
# stream.stop_stream()
# stream.close()
# # Terminate the PortAudio interface
# p.terminate()
#
# print('Finished recording')
#
# # Save the recorded data as a WAV file
# wf = wave.open(filename, 'wb')
# wf.setnchannels(channels)
# wf.setsampwidth(p.get_sample_size(sample_format))
# wf.setframerate(fs)
# wf.writeframes(b''.join(frames))
# wf.close()

#conversion from other formats to wav
file_in = r"m4aSamplefile.m4a"
file_in_video = r"videoMp4.mp4"
file_out='converted3'

song_out=AudioSegment.from_file(file_in_video).export(file_out+".wav", format="wav")


#get file type
with open(file_in, "rb") as file:
    info = fleep.get(file.read(128))

print(info.type)
print(info.extension)
#print(info.mime)


if info.type[0] =="audio":
    print('Audio file accepted')
