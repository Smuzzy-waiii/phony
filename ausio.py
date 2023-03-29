# Sender, Microphone

import sounddevice as sd
from UDPClientHelper import UDPHelper

duration = 60  # seconds
block_size = 512
sample_rate = 44100  # Sample rate in Hz

udp_service = UDPHelper("192.168.249.74", 15000)

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    #outdata[:] = indata
    udp_service.sendPacket(indata.tobytes())
    # print(indata.dtype, indata.shape)

with sd.Stream(channels=1, samplerate=sample_rate, blocksize=block_size, callback=callback):
    sd.sleep(int(duration * 1000))

print('stopped listening')
