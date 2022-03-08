import tkinter as tk
import time,serial,threading

def ReadSerial():
	p = port.get()
	b = baud.get()
	ser = serial.Serial(p, b, timeout=1)
	print(ser.name,ser.baudrate)
	while 1:
		data = ser.readline().decode('utf-8')
		sec.set(data)
		print(data,end='')
		time.sleep(0.2)
		if(stop):
			ser.close()
			break

		


def setstop():
	global stop
	stop = True
	print(stop)

def startThread():
	global x,stop
	stop = False
	x = threading.Thread(target=ReadSerial,daemon=True)
	x.start()
stop = False
window = tk.Tk()
window.title('Serial Monitoring')
font1 = ('Arial Rounded MT Bold',50)
font2 = ('Arial Rounded MT Bold',20)

sec = tk.StringVar()
sec.set('00')

title = tk.Frame(master=window,borderwidth=10)
heading = tk.Label(master = title,text='BIVOT',font=font1)

body = tk.Frame(master=window,borderwidth=5)
tk.Label(master=body,font=font2,textvariable=sec,width=40,height=2).pack()

bottom = tk.Frame(window)

port = tk.Entry(bottom)
port.insert(0,'COM12')
port.pack(side=tk.LEFT)

baud = tk.Entry(bottom)
baud.insert(0,'115200')
baud.pack(side=tk.LEFT)

tk.Button(bottom,text='start',command=startThread,borderwidth=5).pack(side = tk.LEFT)
tk.Button(bottom,text='stop',command=setstop,borderwidth=5).pack()


title.pack()
body.pack()
bottom.pack()
heading.pack()

window.mainloop()



