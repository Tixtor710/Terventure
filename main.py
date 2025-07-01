#A space-based adventure of a crew of curious individuals exploring an unknown galaxy.
#A “Day in the Life” story that walks you through choices the main character makes based on conditions like the time of day, the actions that the player take, etc.
#A classic mini-RPG (role-playing game) with hp health points, character moves like attack/block/heal, and NPCs (non-player characters) that attacks based on a random number generator.
import random

print("Terminal Adventure")
char_name= str(input("Enter your character's name: "))

print("Welcome "+char_name)

print("Answer the following questions; Your answer will determine your path.Hence,Choose wisely.")

q1=input("What kind of adjective suits you the best\n 1. The Warrior\n 2.The lone Wolf\n 3.The Trickster\n")

if q1== "1" or "The Warrior":
  print("That sounds Great "+char_name+" the Warrior")
elif q1 =="2" or "The lone Wolf":
  print("Don't worry!, along the way you'll find your mates, "+char_name+" the lone wolf")
elif q1 == "3" or "The Trickster":
  print("Hold Up, I don't think you can best loki, but you can still try")
else:
  print("invalid input")

character=q1
if character == "1" or "The Warrior":
  print("A day in the life of a warrior is nothing short of hurdles and pain but you have your crew to support you!")
elif character == "2" or "The lone Wolf":
  print("The way of the lone wolf, trouble follows you everywhere but your might will overcome any odds.")
else:
  print("You are beloved and hated by many, but convicted by none.")