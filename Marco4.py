# Marco

import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
TurkeyCount = 0
Valid = True 

PinLDR = 27


def ReadLDR ():
	LDRCount = 0
	GPIO.setup(PinLDR, GPIO.OUT)
	GPIO.output(PinLDR, GPIO.LOW)
	time.sleep(0.1)
	GPIO.setup(PinLDR, GPIO.IN)

	while (GPIO.input(PinLDR) == GPIO.LOW):
		LDRCount += 1 
	return LDRCount

while True:
	value = ReadLDR()
	print(value)
	if(value < 900):
		print("NOPE.NOPE.NOPE") 
		LEDon = GPIO.output(24, 1)
		BUZZoff = GPIO.output(22,0)
		Valid = True
	else:
		print("TURKEY!TURKEYY!TURKEY!!!")
		BUZZon = GPIO.output(22, 1)
		LEDoff = GPIO.output(24, 0)
		if (Valid == True):
			TurkeyCount += 1
			Valid = False
		else:
			BUZZoff = GPIO.output(22,0)
	
	print("Number Of Turkeys That Have Escaped: ", TurkeyCount)
	time.sleep(0.1)
		
	
