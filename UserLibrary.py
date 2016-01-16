from ExceptionLibrary import UserNotFoundError

class User:
	
	def __init__(self,name,cardid):
		self.NumberOfTimesPaid=0
		self.NumberOfTimesWon=0
		self.Lastresult="win"
		self.Name=name
		self.CardId=cardid

class UserManager:

	def __init__(self):
		self.users=[]
	
	def AddUser(self,usr):
		print("UL:AddUserName",usr.Name)
		print("UL:AddUserUID",usr.CardId)
		self.users.append(usr)

	def GetUserByCardId(self,cardid):
		for u in self.users:
			print("check user:",u.Name)
			if(u.CardId==cardid):
			   return u

		raise UserNotFoundError
		
	def LoadHistory(self):
		return true
