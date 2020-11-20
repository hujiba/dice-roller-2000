from random import seed
from random import randint
import time
from art import text2art
from colorama import init, Back, Fore, Style
from sys import platform
# remember to run pip install colorama
# and also pip install art
if platform == "win32":
  init(convert=True)

colors = ["RED", "YELLOW", "BLUE", "CYAN", "GREEN", "MAGENTA", "RED", "YELLOW", "BLUE", "CYAN", "GREEN", "MAGENTA", "RED", "YELLOW", "BLUE", "CYAN", "GREEN", "MAGENTA", "RED", "YELLOW", "BLUE", "CYAN", "GREEN", "MAGENTA"]

sides = int(input("How many sides should the dice have?\n"))
if sides == 0:
  print("you cant do that what were you thinking its 0 how can you have a 0 sided dice like cmon bro youre better than this")
elif sides > 999:
  print("if you do that many digits it will probably look bad because of the ascii art sorry")
else:
    for loop1 in range(24):
      seed()
      rolled = str(randint(1, sides))
      art = text2art("  " + rolled,font='block',chr_ignore=True) # Return ASCII text with block font
      for loop2 in range(13):
        print ("\033[A                                                                        \033[A")
      color = colors[loop1]
      print(getattr(Fore, color) + Style.BRIGHT + art)

      time.sleep(0.075)
    for loop4 in range(2):
      for loop3 in range(13):
        print ("\033[A                                                                        \033[A")
      print(Fore.WHITE + Style.BRIGHT + art)
      time.sleep(0.5)
      for loop3 in range(13):
        print ("\033[A                                                                        \033[A")
      print(Fore.BLACK + Style.BRIGHT + art)
      time.sleep(0.5)
    for loop3 in range(13):
      print ("\033[A                                                                        \033[A")
    print(Fore.WHITE + Style.BRIGHT + art)
    time.sleep(0.5)
