# Receiver, Speaker

import sounddevice as sd
from UDPServerHelper import UDPServerHelper
import numpy as np

duration = 15.5  # seconds
block_size = 512
sample_rate = 48000  # Sample rate in Hz

udp_service = UDPServerHelper(15000)

def callback(indata, outdata, frames, time, status):
    global printed
    # if status:
    #     print(status, '<--- STATUS')
    message, clientAddress = udp_service.recv(block_size*4)
    data = np.frombuffer(message, dtype="float32")
    data = data.reshape((len(data), 1))
    outdata[:] = data

with sd.Stream(channels=1, samplerate=sample_rate, blocksize=block_size, callback=callback):
    sd.sleep(int(duration * 1000))
print('no more output :(')