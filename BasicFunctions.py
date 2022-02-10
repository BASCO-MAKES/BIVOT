import utime
from umachine import ADC, Pin

def check_d(n = 20, pin = 'D0', t = 500):
	p = Pin(pin,Pin.IN)
	for i in range(n):
		print(p.value())
		utime.sleep_ms(t)
def check_a(n = 20, pin = 'D1', samples = 10, t = 500):
	p = ADC(pin)
	for i in range(n):
		sum = 0
		for j in range(samples):
			sum+=p.read()
			utime.sleep_us(5)
		print(sum//samples)
		utime.sleep_ms(t)
def square_wave(t=50,p ='D0'):
	p4 = Pin('D4',Pin.IN,Pin.PULL_DOWN)
	p1 = Pin('D1',Pin.IN,Pin.PULL_DOWN)
	p0 = Pin('D0',Pin.OUT)
	
	out = 1
	while p4.value() == 0:
		p0.value(out)

		utime.sleep_ms(t)
		out = abs(out -1)
def analog_in(pin = 'D1',samples = 10,wait = 5):
	sum = 0
	p = ADC(pin)
	for i in range(samples):
		sum+=p.read()
		utime.sleep_us(wait)
	output = sum//samples
	return output
def digital_in(pin = 'D0'):
	p = Pin(pin,Pin.IN)
	return p.value()







