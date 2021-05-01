#Import libraries and define any variables
import random, sys, replit, time
from termcolor import colored as col
coin_count = 0
color_list = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]
fast = 0.03
slow = 0.1
normal = 0.05

#Create functions for changing the speed of the typewriter
def text(words, speed):
	for i in words:
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(speed)

#Returns the value of the coin flip 
def flipCoin():
  input("Press 'Enter' to flip a coin. ")
  return random.randint(0,1)

#Ends the program and outputs a message along with it
def end(n):
  sys.exit(n)

#Checks to see if you fliped a coin once. If you flipped the coin more than once, the program will end. 
def checkCoin():
  if coin_count == 1:
    replit.clear()
    text(f"After throwing your coin, you accidentily dropped your coin down a sewer pipe. It must have been all that beer. {name} won't be able to flip a coin another time.\n\n", normal)
  elif coin_count > 1:
    end("\n\nYou can't flip another coin. Run the program again to restart.")

def increment():
  global coin_count
  coin_count += 1

# Instructions
text(f"When making decisions, 'Y' stands for yes, 'N' stands for no, and 'C' stands for coin meaning to flip a coin in making that decision.\nKeep in mind that you can only flip a coin once.", fast)

# # Story Introduction
text("\n\nDecember 16th, 1998 was the date...\n", slow)
name = input("Enter your firstname: ")
text(f"It was a gloomy night. You, {name}, decided to go out with your friends to have a drink. \nYou were just evicted from your house and now have nowhere to stay for the night. Your friends were no help either as they drank the night away. \n\n{col('Suddenly', 'red')}, a hooded-stranger sitting next to you on the bar stand offered you to stay at his place. However, he is no {col('ordinary', color_list[random.randint(0, len(color_list)-1)]) } stranger. He is highly wanted by the FBI and government for commiting numerous crimes. In return for the shelter, he asks that you, {name}, take care of his 3-year-old daughter that is suffering from an incurable disease and laying in bed.", normal)

#Decision 1: Yes, No, or flip a coin. 
text("Do you accept his offer(Y/N/C)?", slow)
decision1 = input("").lower()
if decision1 == "y":
  text(f"Even though you were thinking of saying yes, you were still skeptical of the situation, you couldn't help but feel bad for the stranger's daughter. In the end, you accepted his offer. \nYou waited for the stranger to finish his beer before you both left the building.\n\nUpon leaving the building, you see a couple of police officers in the distance searching for him. He directed you towards a neighbouring parking lot where he stole a {color_list[random.randint(0, len(color_list)-1)]} colored car.", normal)
  replit.clear()
  text(f"Since the stranger was drunk driving, you both got caught up in an accident.", normal)
  end("\n\nYou Died. Call a taxi next time. Run the program again to restart.")
elif decision1 == "n":
  text(f"The stranger understands and leaves you at rest.\n", normal)
elif decision1 == "c":
  result = flipCoin()
  increment()
  checkCoin()
  #checks to see heads or tails
  if result == 1:
    text(f"You landed heads...\nThe stranger thought you were insane to use a coin to make a decision, but he was grateful in the end. You waited for the stranger to finish his beer before you both left the building. Upon leaving the building, you see a couple of police officers in the distance searching for him. He directed you towards a neighbouring parking lot where he stole a {color_list[random.randint(0, len(color_list)-1)]} colored car.", normal)
    replit.clear()
    text(f"Since the stranger was drunk driving, you both got caught up in an accident.", normal)
    end("\n\nYou Died. Call a taxi next time. Run the program again to restart.")
  else:
    text(f"You landed tails...\nThe stranger thought that you were insane to use a coin to make a decision. He downed his last bit of beer and quickly walked out the front gate without saying anything.\n", normal)
replit.clear()

#Decision 2: First option, second option, or third option(flipping a coin.)
text(f"After you finished your last sip of beer, you decide to walk around the streets searching for a cozy place to camp out for the night. You find a nice isolated area inside an alleyway to rest. {col('Suddenly', 'red')}, you hear someone calling your name in the distance: {name.upper()}...{name.upper()}...\n\nYou don't recognize the voice.\n", normal)
text("Do you...\n1. Walk in the direction of the voice\n2. Run away\n3. Flip a Coin\n", slow)
decision2 = int(input("(1/2/3): "))
if decision2 == 1:
  friend1 = input("Enter the name of your friend: ")
  text(f"You decide to walk in the direction of the voice. You realize it was your drunk friend, {friend1}, who was calling your name with his loud voice. He didn't even recognize you at first glance.", normal)
elif decision2 == 2:
  friend2 = input("Enter the name of your friend: ")
  text(f"You decide to run away until you can't hear the voice anymore. {col('Suddenly', 'red')}, you hear someone nervously whisper behind you: \"{name[0].lower()}-{name[0].lower()}-{name[:2].lower()}...{name}?\" You turn around to see it's your friend, {friend2}.", normal)
elif decision2 == 3:
  increment()
  checkCoin()
  result = flipCoin()
  #check to see heads or tails
  if result == 1:
    friend1 = input("Enter the name of your friend: ")
    text(f"You landed heads...\nSo you decide to walk towards the direction of the voice, only to meet your drunk friend, {friend1}.", normal)
  else: 
    friend2 = input("Enter the name of your friend: ")
    text(f"You landed tails...\nSo you decide to run away until the voice wasn't audible, only to meet another one of your drunk friends, {friend2}.", normal)
replit.clear()

#Decision 3: Yes, No, or Flip a coin
text(f"Even though your friend was drunk, he was conscious enough to offer you to stay at his place for the time-being until you get back on your feet.\nDo you accept his kind offer(Y/N/C)? ", normal)
decision3 = input("").lower()
if decision3 == "y":
  text(f"You felt a sense of happiness and relief when he offered it to you, and you gladly accepted the offer.\nHe offered to drive you back to his place. Do you accept this offer(Y/N)? ", normal)
  #Decision 4: Yes or No
  decision4 = input("").lower()
  if decision4 == "y":
    text(f"Since your friend was drunk driving, you both got caught up in an accident.", normal)
    end("\n\nYou Died. Call a taxi next time. Run the program again to restart")
  elif decision4 == "n":
    text(f"You suggested that since he's drunk, it would be safer to call a taxi. Because of that quick decision, you both made it back to your friend's appartment safely.\n\n", normal)
    replit.clear()
    text("Two years later...", slow) 
    text("You moved out from your friend's appartment to your spouse's house and lived happily ever since.\n", normal)

elif decision3 == "n":
  text(f"You rejected his offer and spent the night outside.\nWhen you woke up, you realized all your belongings has been stolen including your wallet and even clothing. You were left a message that read: \"From the criminal at the bar\".\n\nThe days were getting colder and you had no money in your pocket to provide for yourself.\n\n", normal)
  end("You Died. Accept the offer next time. Run the program again to restart")
elif decision3 == "c":
  increment()
  checkCoin()
  result = flipCoin()
  #Checks to see if coin flip is heads or tails
  if result == 1:
    text(f"\n\nYou landed heads...\nSo you accepted the offer.\nHe then offered to drive you back to his place. Do you accept this offer(Y/N)?", normal)
    decision4 = input("").lower()
    if decision4 == "y":
      text(f"Since your friend was drunk driving, you both got caught up in an accident.", normal)
      end("\n\nYou Died. Call a taxi next time and don't flip a coin. Run the program again to restart")
    elif decision4 == "n":
      text(f"You suggested that since he's drunk, it would be safer to call a taxi. Because of that quick decision, you both made it back to your friend's appartment safely.\n\n", normal)
      replit.clear()
      text("Two years later, you moved out from your friend's appartment to your spouse's house and lived happily ever since.\n", slow)
  else:
    text(f"You landed tails...\nYou spent the night outside.\nWhen you woke up, you realized all your belongings has been stolen including your wallet and even clothing. You were left a message that read: \"From the criminal at the bar\".\n\nThe days were getting colder and you had no money in your pocket to provide for yourself.\n\n", normal)
    end("You Died. Don't flip a coin next time. Run the program again to restart")
replit.clear()

text(f"Thank's for playing!".upper(), normal)
