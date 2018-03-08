import serial
import signal
import socket
import sys

name = "noah"

ser = serial.Serial('/dev/tty.usbmodem1451',9600)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def signal_handler(signal, frame):
        print('Stopping...')
        sock.close()
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

telegraf_address = ('localhost', 8094)

while True:
    output = ser.readline()
    output = output.strip()
    message = "heartbeats,name=%s value=%s\n" % (name, output)
    print message
    sock.sendto(message, telegraf_address)
