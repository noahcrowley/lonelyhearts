import serial
import signal
import socket
import sys

# The name of the workshop participant. This name will be written to the datbase 
# as a tag.
name = "noah"

# Connections to the Arduino, over serial, and Telegraf, over a network socket.
ser = serial.Serial('/dev/tty.usbmodem1441',9600)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# This code waits for the Unix Signal "SIGINT", which can be sent by typing
# "ctrl+c" on the keyboard. When the program receives that signal, it executes 
# the signal_handler function, which closes the network socket and exits the 
# program. 
def signal_handler(signal, frame):
        print('Stopping...')
        sock.close()
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# The network address of the Telegraf process.
telegraf_address = ('localhost', 8094)

# We start a loop which will run until the program is exited (using "ctrl+c").
# First, we read individual lines from the serial port and strip off any whitespace.
# We then create a message in "line-protocol", print it for debugging purposes, and
# send it to Telegraf over the socket connection. Then we repeat.
while True:
    output = ser.readline()
    output = output.strip()
    message = "heartbeats,name=%s value=%s\n" % (name, output.decode('utf-8'))
    print(message)
    sock.sendto(message.encode('utf8'), telegraf_address)
