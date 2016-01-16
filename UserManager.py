import User

class UserManager:

	def __init__(self):
		self.users=[]
	
	def AddUser(self,usr):
		self.users.append(usr)

	def GetUserByCardId(self,cardid):
		return User("Neil",cardid)
		
