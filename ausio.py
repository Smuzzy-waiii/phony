# Sender, Microphone

import sounddevice as sd
from UDPClientHelper import UDPHelper
import sys
my_port = int(sys.argv[1])
not_my_port = int(sys.argv[2])

duration = 15.5  # seconds
block_size = 2048
sample_rate = 44100  # Sample rate in Hz

udp_service = UDPHelper("localhost", not_my_port, my_port)

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    #outdata[:] = indata
    udp_service.sendPacket(indata.tobytes())
    message, clientAddress = udp_service.recv(block_size*4)
    data = np.frombuffer(message, dtype="float32")
    data = data.reshape((len(data), 1))
    outdata[:] = data
    # print(indata.dtype, indata.shape)

with sd.Stream(channels=1, samplerate=sample_rate, blocksize=block_size, callback=callback):
    sd.sleep(int(duration * 1000))

print('stopped listening')
