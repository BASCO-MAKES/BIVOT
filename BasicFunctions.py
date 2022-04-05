import utime
from umachine import ADC, Pin

def check_d(n = 20, pin = 'D0', t = 500): #print the digital input at 'pin' for 'n' no. of times
	for i in range(n):
		print(digital_in(pin))
		utime.sleep_ms(t)
def check_a(n = 20, pin = 'D1', samples = 10, t = 500):#print the digital input at 'pin' for 'n' no. of times
	for i in range(n):
		print(analog_in(pin))
		utime.sleep_ms(t)
def square_wave(t=50,p ='D0'): #output a squarewave with a period of '2t'
	p0 = Pin('D0',Pin.OUT)
	out = 1
	while True:
		p0.value(out)
		utime.sleep_ms(t)
		out = abs(out -1)
def analog_in(pin = 'D1',samples = 10,wait = 5): #returns the analog input at 'pin'
	sum = 0
	p = ADC(pin)
	for i in range(samples):
		sum+=p.read()
		utime.sleep_us(wait)
	output = sum//samples
	return output
def digital_in(pin = 'D0'): #returns the digital input at 'pin'
	p = Pin(pin,Pin.IN)
	return p.value()
def CopyFile(f1,f2):
	for line in f1:
		f2.write(line)

