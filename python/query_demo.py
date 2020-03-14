#!/usr/bin/env python

import serial
from tracer import Tracer, TracerSerial, QueryCommand

# Set Serial interface path
s_path = '/dev/ttyS0' # ttyS0 w/ Bluetooth ttyAMA0 w/o

ser = serial.Serial(s_path, 9600, timeout = 1)

tracer = Tracer(0x16)
t_ser = TracerSerial(tracer, ser)
query = QueryCommand()
t_ser.send_command(query)
result = t_ser.receive_result()

#print "Raw bytes: %s" % ", ".join(map(lambda a: "%0X" % (a), result.data))
print
formatted = str(result).replace('{', '{\n')
formatted = formatted.replace('}', '\n}')
print formatted.replace(', ', '\n')
print
print result
