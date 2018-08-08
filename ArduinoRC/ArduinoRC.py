#! py -2
# This project requires PyBluez
from Tkinter import *
import bluetooth

#Look for all Bluetooth devices
#the computer knows about.
print "Searching for devices..."
print ""
#Create an array with all the MAC
#addresses of the detected devices
nearby_devices = bluetooth.discover_devices()
#Run through all the devices found and list their name
num = 0
print "Select your device by entering its coresponding number..."
for i in nearby_devices:
    num+=1
    print num , ": " , bluetooth.lookup_name( i )

#Allow the user to select their Arduino
#bluetooth module. They must have paired
#it before hand.
selection = input("> ") - 1
print "You have selected", bluetooth.lookup_name(nearby_devices[selection])
bd_addr = nearby_devices[selection]

port = 1

#Create the GUI
class Application(Frame):

#Create a connection to the socket for Bluetooth communication
    sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )

    def forward(self,event):
        data = "F"
        self.sock.send(data)

    def backwards(self,event):
        data = "B"
        self.sock.send(data)

    def left(self,event):
        data = "L"
        self.sock.send(data)

    def right(self,event):
        data = "R"
        self.sock.send(data)

    def stop(self,event):
        data = "S"
        self.sock.send(data)

    def createWidgets(self):
        # This opens a new window that accepts keyboard arrows. Uncomment if it's not desired
        self.root = Tk()
        self.root.bind("<KeyPress-Up>", self.forward)
        self.root.bind("<KeyRelease-Up>", self.stop)
        self.root.bind("<KeyPress-Down>", self.backwards)
        self.root.bind("<KeyRelease-Down>", self.stop)
        self.root.bind("<KeyPress-Right>", self.right)
        self.root.bind("<KeyRelease-Right>", self.stop)
        self.root.bind("<KeyPress-Left>", self.left)
        self.root.bind("<KeyRelease-Left>", self.stop)

         #Form all the buttons. Look at a Tkinter reference for explanations.
        self.rBtn = Button(self)
        self.rBtn["text"] = "Right"
        self.rBtn.bind("<ButtonPress>", self.right)
        self.rBtn.bind("<ButtonRelease>", self.stop)
        self.rBtn.pack({"side": "left"})

        self.lBtn = Button(self)
        self.lBtn["text"] = "Left"
        self.lBtn.bind("<ButtonPress>", self.left)
        self.lBtn.bind("<ButtonRelease>", self.stop)
        self.lBtn.pack({"side": "left"})

        self.fBtn = Button(self)
        self.fBtn["text"] = "Forward",
        self.fBtn.bind("<ButtonPress>", self.forward)
        self.fBtn.bind("<ButtonRelease>", self.stop)
        self.fBtn.pack({"side": "left"})

        self.bBtn = Button(self)
        self.bBtn["text"] = "Backwards"
        self.bBtn.bind("<ButtonPress>", self.backwards)
        self.bBtn.bind("<ButtonRelease>", self.stop)
        self.bBtn.pack({"side": "left"})

    def __init__(self, master=None):
    	#Connect to the bluetooth device and initialize the GUI
        self.sock.connect((bd_addr, port))
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

#Begin the GUI processing
root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()