"""PyAudio Example: Play a WAVE file."""

import pyaudio
import wave
import sys
import numpy as np

CHUNK = 4096

if len(sys.argv) < 2:
    print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)

wf = wave.open(sys.argv[1], 'rb')

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

##print(stream.read(CHUNK))
# create a numpy array holding a single read of audio data
##for i in range(10): # do it a few times just to see
##    data = wf.readframes(CHUNK)
##    print(data)


print("Playing:", sys.argv[1] )
##print("Channels:",wf.getnchannels(),"Frame Rate:", wf.getframerate(),"Hz",
##      "Samples:",wf.getsampwidth())
params=wf.getparams()
print(params)
print(params.nframes/params.framerate)

##data = wf.readframes(CHUNK)
##for i in range(100):
##    print(data[i], end=" ")

i=0



data = wf.readframes(CHUNK)

while data != ' ':
    stream.write(data)
    data = wf.readframes(CHUNK)
    print(data[i])
    pos=wf.tell() / (4096*10*60)
    print("%5.2f"%(pos), sep=' ', end=' ', flush=True)
    i+=1
    
stream.stop_stream()
stream.close()
p.terminate()

