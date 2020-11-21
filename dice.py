from random import seed
from random import randint
import time
from art import text2art
from colorama import init, Back, Fore, Style
from sys import platform

if platform == "win32":
  init(convert=True)

colors = ["RED", "YELLOW", "BLUE", "CYAN", "GREEN", "MAGENTA", "RED", "YELLOW", "BLUE", "CYAN", "GREEN", "MAGENTA", "RED", "YELLOW", "BLUE", "CYAN", "GREEN", "MAGENTA", "RED", "YELLOW", "BLUE", "CYAN", "GREEN", "MAGENTA"]

sides = int(input("How many sides should the dice have?\n"))
if sides == 0:
  what = text2art("what",font="larry3d")
  print(getattr(Fore, colors[randint(0, 30)]) + what)
  #-print(getattr(Fore, GREEN + dumb))
elif sides > 999999999:
  no = text2art("please no",font="larry3d")
  print(getattr(Fore, colors[randint(0, 30)]) + no)
else:
    for loop1 in range(24):
      seed()
      rolled = str(randint(1, sides))
      art = text2art("  " + rolled,font='block',chr_ignore=True) # Return ASCII text with block font
      for loop2 in range(13):
        print ("\033[A                                                                        \033[A")
      color = colors[loop1]
      print(getattr(Fore, color) + Style.BRIGHT + art)
      spin = loop1 * loop1 * 0.0011 + 0.05
      time.sleep(spin)
    time.sleep(0.3)
    for loop4 in range(2):
      for loop3 in range(14):
        print ("\033[A                                                                        \033[A")
      print(Fore.WHITE + Style.BRIGHT + "You rolled a:\n" + art)
      time.sleep(0.5)
      for loop3 in range(14):
        print ("\033[A                                                                        \033[A")
      print(Fore.BLACK + Style.BRIGHT + "You rolled a:\n" + art)
      time.sleep(0.5)
    for loop3 in range(14):
      print ("\033[A                                                                        \033[A")
    print(Fore.WHITE + Style.BRIGHT + "You rolled a:\n" + art)
    time.sleep(0.5)
    # edit edit hahdhgjfghkw fgdsfghdagaf
