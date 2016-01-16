from CardLibrary import CardManager
from UserLibrary import UserManager
from DeviceLibrary import DeviceManager
from UserLibrary import User
from ExceptionLibrary import UserNotFoundError
from random import randint
from DeviceLibrary import Device

class GameManager:
	
	def __init__(self):
		self.TotalWinners=0
		self.LastResult=""
		self.FirstRun=True
		self.LastWinner=None

	def setup(self,userman,cardman,deviceman):
		self.UserManager=userman
		self.CardManager=cardman
		self.DeviceManager=deviceman

	def addUser(self,username,cardid):
		self.UserManager.AddUser(User(username,cardid))
		return User(username,cardid)

	def getCoffee(self,user):
		print("COFFEE TIME!")
		if(randint(0,10)>4):
			print("Pay up!")
			self.DeviceManager.sendCommandToAllDevices("PAY")
		else:
			print("Hey "+user.Name+" you win coffee")
			self.DeviceManager.sendCommandToAllDevices("WIN")


	def getCardUID(self):
		return self.CardManager.getUID()

	def getUser(self,cardid):
		try:
			foundUser=self.UserManager.GetUserByCardId(cardid)
			return foundUser
		except UserNotFoundError:
			print("-not found-")
			raise UserNotFoundError

	def addNewUser(self,uid):
		print("Hi New Person!")
		newuser=raw_input("Please enter your name...")
		self.addUser(newuser,uid)
