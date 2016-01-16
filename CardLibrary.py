import rfid

class CardManager:
	def __init__(self):
		return		

	def waitTag(self):
		rfid.waitTag()
	
	def isCard(self,cardtype):
		ret = rfid.readMifare()
		return ret
	
	def cardType(self):
		return rfid.getTypeName()

	def getUID(self):
		return rfid.getUniqueId()

	def waitNoTag(self):
		rfid.waitNoTag()
