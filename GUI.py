import tkinter as tk
import time,serial,threading
import serial.tools.list_ports_windows

def ReadSerial():
	if(device_names[0]=='None'):
		return
	p = devices[option.get()]
	b = baud.get()
	
	ser = serial.Serial(p, b, timeout=1)
	print(ser.name,ser.baudrate)
	while 1:
		data = ser.readline().decode('utf-8')
		#print(data,len(data))

		received = data[:-1]
		sec.set(received)
		UpdateImage(received)
		print(data,end='')
		time.sleep(0.2)
		if(stop):
			ser.close()
			break

def GetPorts():
	ports = serial.tools.list_ports_windows.comports()

	

	com_port = []
	device_name = []
	for device in ports:
		com_port.append(device[0])
		device_name.append(device[1])
	if(len(device_name)==0):
		device_name.append('None')
	return dict(zip(device_name,com_port)),device_name

def setstop():
	toggle_value.set('Start')

	
	global stop
	stop = True
	print(stop)

def startThread():
	toggle_value.set('Stop')

	global x,stop
	stop = False
	x = threading.Thread(target=ReadSerial,daemon=True)

	x.start()

def toggleSerialConnection():
	if(not stop):
		print('set-',stop)
		setstop()
	else:
		print('start- ',stop)
		startThread()

def UpdateImage(state):
	print('---',state)
	if(state == "Closed"):
		num = 0
	elif(state == "Partial"):
		num = 1
	elif(state == "Open"):
		num = 2
	else:
		num = 3
	canvas.itemconfig(imagecontainer,image=images[num])

stop = True
window = tk.Tk()
window.title('Serial Monitoring')
window.iconbitmap("C:/Users/aswin/Downloads/Copy of Untitled 7.ico")

font1 = ('Arial Rounded MT Bold',80)
font2 = ('Arial Rounded MT Bold',30)
font3 = ('Calibri',15)
font4 = ('Arial Rounded MT Bold',15)

baudrates = [9600,115200]

image_Files = [
	"C:/Users/aswin/Documents/Closed.png",
	"C:/Users/aswin/Documents/Partial.png",
	"C:/Users/aswin/Documents/Open.png",
	"C:/Users/aswin/Documents/Other.png"]



sec = tk.StringVar()
print(sec)
sec.set('00')
print(sec)

title = tk.Frame(master=window,borderwidth=10)
heading = tk.Label(master = title,text='BIVOT',font=font1)

subtitle = tk.Frame(window)


devices,device_names = GetPorts()
option = tk.StringVar()

option.set(device_names[0])
	
port_dropdown = tk.OptionMenu(subtitle,option,*device_names)
port_dropdown.config(font=font3)


#port_dropdown.pack(side=tk.LEFT)


baud = tk.IntVar()
baud.set(baudrates[0])
baud_dropdown = tk.OptionMenu(subtitle,baud,*baudrates)
baud_dropdown.config(font=font3)
#baud_dropdown.pack(side=tk.LEFT)


toggle_value = tk.StringVar()

toggle_value.set("Start")

toggle_serial = tk.Button(
	subtitle,
	textvariable=toggle_value,
	command=toggleSerialConnection,
	font=font3)


port_dropdown.grid(row=0,column=0,padx=3,pady=5,columnspan=2)
baud_dropdown.grid(row=0,column=2,padx=3,pady=5,columnspan=2)
toggle_serial.grid(row=0,column=4,padx=3,pady=5)



body = tk.Frame(master=window,borderwidth=5)

images = []
for item in image_Files:
	images.append(tk.PhotoImage(file=item))

canvas = tk.Canvas(master=body,width=300,height=200)
imagecontainer = canvas.create_image(10,10,anchor='nw',image=images[0])
canvas.pack()

print(images)
img = tk.PhotoImage(file="C:/Users/aswin/Documents/Open.png")
tk.Label(master=body,font=font2,textvariable=sec,width=40,height=3,borderwidth=2,relief=tk.SOLID,anchor=tk.CENTER,).pack(side=tk.TOP)





title.pack()
subtitle.pack()
body.pack()
heading.pack()

window.mainloop()



