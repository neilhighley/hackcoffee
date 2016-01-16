# SL030 RFID tag reader example  18/08/2014  D.J.Whale
# http://blog.whaleygeek.co.uk/raspberry-pi-rfid-tag-reader
#
# For use with SKPang Electronics SL030 RFID module,
# with a SL030 Raspberry Pi cable, and a Raspberry Pi
# running Raspbian Wheezy.
# product numbers: RFID-SL030, RSP-SL030-CAB
# http://skpang.co.uk/blog/archives/946
#
# Run this program as follows:
#   sudo python rfid_example.py
# or
#   sudo python3 rfid_example.py


# Import this module to gain access to the RFID driver
import rfid
from UserLibrary import User
from UserLibrary import UserManager
from GameLibrary import GameManager
from CardLibrary import CardManager
from DeviceLibrary import DeviceManager
from DeviceLibrary import Device
from DeviceLibrary import ArduinoDevice
from ExceptionLibrary import UserNotFoundError

usermanager=UserManager()
game=GameManager()
cardmanager=CardManager()
devicemanager=DeviceManager()
devicemanager.addDevice(Device("OUT1"))
devicemanager.addDevice(ArduinoDevice("OUT2"))

game.setup(usermanager,cardmanager,devicemanager)

game.addUser("Neil","044B2BCA0E2A80")
game.addUser("WhaleyGeek","2B53B49B")

# MAIN PROGRAM

while True:

  # wait for a card to be detected as present
  print("Waiting for a card...")
  game.CardManager.waitTag()
  print("Card present")

  # This demo only uses Mifare cards
  if not game.CardManager.isCard("miifare"):
    print("This is not a mifare card")
  else:
    # What type of Mifare card is it? (there are different types)
    print("Card type:" + game.CardManager.cardType())

    # look up the unique ID to see if we recognise the user
    uid = game.getCardUID()
    
    try:
      user=game.getUser(uid)
      #user = cards[uid]
      print(user)
      print("Hello there : " + user.Name)
    except UserNotFoundError:
      user=game.addNewUser(uid)

    game.getCoffee(user)

  # wait for the card to be removed
  print("Waiting for card to be removed...")
  game.CardManager.waitNoTag()
  print("Card removed")

# END
