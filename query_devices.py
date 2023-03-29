import sounddevice as sd

# Get a list of all available audio devices
devices = sd.query_devices()

# Loop over each device and print its properties
for device in devices:
    print("Name: ", device["name"])
    # print("Sample rates: ", device["rates"])
    print(device)
