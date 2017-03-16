# Blinking IP octet utility
# By Ian Simpson @familysimpson

import socket
import RPi.GPIO as GPIO
import time
from sense_hat import SenseHat

sense = SenseHat()

def get_local_ip_address(target):
  ipaddr = ''
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((target, 8000))
    ipaddr = s.getsockname()[0]
    s.close()
  except:
    pass

  return ipaddr


print "Raspberry Pi - Local IP Address"
ip = (get_local_ip_address('10.0.1.1'))
count = 0
while count < 3:
  sense.show_message(ip)
  count += 1
  time.sleep(2)
