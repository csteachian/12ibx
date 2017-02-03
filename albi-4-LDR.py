import time
import RPi.GPIO as Albi

Albi.setmode(Albi.BCM)
Albi.setwarnings(False)
Albi.setup(24, Albi.OUT)
Albi.setup(22, Albi.OUT)

PinLDR = 27
CARCount = 0 
Valid = True

def ReadLDR():
	LDRCount = 0
	Albi.setup(PinLDR, Albi.OUT)
	Albi.output(PinLDR, Albi.LOW)
	time.sleep(0.1)
	Albi.setup(PinLDR, Albi.IN)
	while (Albi.input(PinLDR) == Albi.LOW):
		LDRCount += 1
	return LDRCount

while True:
	value = ReadLDR()
	print(value)
	if(value < 1900):
		#print("Its bright!!", CARCount, "Turkeys Have Obscured me today")
		LEDon = Albi.output(24, 1)
		Valid = True
		BUZZoff = Albi.output(22, 0)
		
	else:
		#print("ITS DARK", value)
		LEDoff = Albi.output(24, 0)
                BUZZon = Albi.output(22, 1)

		if(Valid == True):
			CARCount += 1
			Valid = False
		else:
			BUZZoff = Albi.output(22, 0)

		#print("Turkeys Passed:", CARCount)
		
		if(CARCount > 20):
			print(CARCount, "A SloCO CEO  has escaped")
		else:
			print("System is operational")

	time.sleep(0.1)#polling time

