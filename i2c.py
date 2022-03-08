from umachine import I2C

def start_i2c():

	global i2c 
	i2c = I2C(1,freq=400000)
	print(i2c.scan())
def write_i2c(data,add):
	i2c.writeto(add,data.encode('utf-8'))