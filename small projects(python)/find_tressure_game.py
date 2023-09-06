print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

direction=input("You're at a cross road. Where do yo want to go? Type 'left' or 'right'\n").lower()
if direction=="left":
  print("You came to a lake. There is an island in the middle of the lake.Type 'wait' to wait for the boat.Type 'swim' to swim accross'")
  river=input().lower()
  if river=="wait":
    print("you arrive at the island unharmed. There is a house with three doors.One red, One yellow and one blue.Which colour do you choose?")
    door=input().lower()
    if door=="red":
      print("you entered a room full of fire.GAME OVER")
    elif door=="blue":
      print("you entered a room with lion. GAME OVER")
    elif door=="yellow":
      print("CONGRATULATIONS. YOU GOT  THE TREASURE.")
    else:
      print("wrong input")
  elif river=="swim":
    print("you have bitten by a crocadile . GAME OVER")
  else:
    print("wrong input")
elif direction =="right":
  print("you went to a wrong direction . GAME OVER")
else:
  print("wrong input")
  
