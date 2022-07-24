import serial
import keyboard
DEVICE = '/dev/rfcomm0'
BAUD_RATE = 9600
MAX = 180
MIN = 0
# Connect to the device
s = serial.Serial(DEVICE, BAUD_RATE)
print('Connect to', DEVICE)
cl = 180
sl = 180
al = 100
while True:
    if keyboard.is_pressed("c"):
        print("c pressed")
        if keyboard.is_pressed("-"):
            if cl > MIN:
                cl = cl - .1
                print(cl)
                s.write(bytes('c' + str(int(cl)) + '\n', 'UTF-8'))
        elif keyboard.is_pressed("+"):
            if cl < MAX:
                cl = cl + 0.1
                print(cl)
                s.write(bytes('c' + str(int(cl)) + '\n', 'UTF-8'))


# Send data

# Receive data

print(data)