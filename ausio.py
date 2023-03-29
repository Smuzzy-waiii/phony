# Sender, Microphone

import sounddevice as sd
from UDPClientHelper import UDPHelper
import sys
import numpy as np

my_port = int(sys.argv[1])
not_my_port = int(sys.argv[2])

duration = 60  # seconds
block_size = 2048
sample_rate = 44100  # Sample rate in Hz

udp_service = UDPHelper("localhost", not_my_port, my_port)

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)

    # Send audio data to remote client
    udp_service.sendPacket(indata.tobytes())
    print(f"Sent {len(indata.tobytes())} bytes to remote client")

    # Receive audio data from remote client
    message, clientAddress = udp_service.recv(block_size*4)
    print(f"Received {len(message)} bytes from remote client")

    # Convert received data to numpy array
    data = np.frombuffer(message, dtype="float32")
    data = data.reshape((len(data), 1))

    # Output received data to speaker
    outdata[:] = data

    # Debugging output
    print(f"indata shape: {indata.shape}")
    print(f"outdata shape: {outdata.shape}")
    print(f"data shape: {data.shape}")


with sd.Stream(channels=1, samplerate=sample_rate, blocksize=block_size, callback=callback):
    sd.sleep(int(duration * 1000))

print('stopped listening')
