

#CamJam Edukit 2 - sensors
#Worksheet 4 - Light

# Must be run as root - sudo python blink11.py 

import time
import RPi.GPIO as Shali

PinLDR = 27
PinLED = 24
PinBUZZ = 22
Carcount= 0
valid = True

Shali.setmode(Shali.BCM)
Shali.setwarnings(False)
Shali.setup(PinLED, Shali.OUT)
Shali.setup(PinBUZZ, Shali.OUT)


def ReadLDR():
	LDRCount = 0 # sets the count to 0
	Shali.setup(PinLDR, Shali.OUT)
	Shali.output(PinLDR, Shali.LOW)
	time.sleep(0.1) # Drains all charge from the capacitator
	Shali.setup(PinLDR,Shali.IN) # sets the pin to be input
	# whle the input pin reads off or low, count
	while (Shali.input(PinLDR) == Shali.LOW):
		LDRCount += 1 # add one to the counter
	return LDRCount

while True:
	value = ReadLDR()
	print (value)
	if (value <900):#threshold
		#print("bright")
		LEDon = Shali.output(PinLED, 1)
		BUZZoff = Shali.output(PinBUZZ, 0)
		valid = True
	else:
		#print("dark")
		LEDoff = Shali.output(PinLED, 0)
		BUZZon = Shali.output(PinBUZZ, 1)

		if (valid == True):
			Carcount += 1
			valid = False
		else:
			BUZZoff = Shali.output(PinBUZZ, 0)
	

	print("car",Carcount)
	time.sleep (0.1) 

#	LEDon = shali.output(11, 0)
#	time.sleep(1)
#	LEDoff = shali.output(11, 1)
#	time.sleep(2)

