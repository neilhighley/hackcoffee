import requests

class DeviceManager:

	def __init__(self):
		print("Device Manager initialised")
		self.devices=[]

	def addDevice(self,dev):
		self.devices.append(dev)
		print("Device added:",dev.Name)
		print("Device type:",dev.Type)		
	
	def sendCommandToAllDevices(self,cmd):
		for dev in self.devices:
			dev.send(cmd)
	
class Device:

	def __init__(self,name):
		self.Type=0
		self.Name=name
	
	def send(self,cmd):
		print("Command Received:",cmd)
		

class ArduinoDevice(Device):

	def __init__(self,name):
		self.Type=1
		self.Name=name
		self.Url="http://mockbin.org/bin/489b2d3d-049e-48b2-bc67-f632bf7018bb"

	def send(self,cmd):
		print("Arduino Command Received:",cmd)
		self.LastResponse=requests.get(self.Url+"?foo="+cmd)
		print(self.LastResponse)
		
		
