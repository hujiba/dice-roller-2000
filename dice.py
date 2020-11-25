from random import seed
from random import randint
import time
from art import text2art
from colorama import init, Back, Fore, Style
from sys import platform
import funfacts

if platform == "win32":
  init(convert=True) # idk it just breaks on windows if you dont have it and breaks on linux if you do

loop = 1
colors = ["RED", "YELLOW", "BLUE", "CYAN", "GREEN", "MAGENTA"]

while loop == 1:
  colorRandom = randint(0, 5)
  try:
    sides = int(input("How many sides should the dice have?\n"))
    if sides == 0:
      what = text2art("what",font="larry3d")
      print(getattr(Fore, colors[randint(0, 5)]) + what)
    elif sides > 999999999:
      no = text2art("please no",font="larry3d")
      print(getattr(Fore, colors[randint(0, 5)]) + no)
    else:
        for loop5 in range(7):
          print("\n")
        for loop1 in range(24):
          seed()
          rolled = str(randint(1, sides))
          art = text2art("  " + rolled,font='block',chr_ignore=True)
          for loop2 in range(13):
            print ("\033[A                                                                                       \033[A")
          pickedColor = (loop1 + colorRandom)
          try: # solution for looping over the list of colors. probably not the best way but whatever
            color = colors[pickedColor]
          except:
            try:
              color = colors[(pickedColor - 6)]
            except:
              try:
                color = colors[(pickedColor - 12)]
              except:
                try:
                  color = colors[(pickedColor - 18)]
                except:
                  try:
                    color = colors[(pickedColor - 24)]
                  except:
                    try:
                      color = colors[(pickedColor - 30)]
                    except:
                      print("what")
          print(getattr(Fore, color) + Style.BRIGHT + art)
          spin = loop1 * loop1 * 0.0011 + 0.05
          time.sleep(spin)
        time.sleep(0.3)
        for loop4 in range(2):
          for loop3 in range(14):
            print ("\033[A                                                                                       \033[A")
          print(Fore.WHITE + Style.BRIGHT + "You rolled a:\n" + art)
          time.sleep(0.5)
          for loop3 in range(14):
            print ("\033[A                                                                                       \033[A")
          print(Fore.BLACK + Style.BRIGHT + "You rolled a:\n" + art)
          time.sleep(0.5)
        for loop3 in range(14):
          print ("\033[A                                                                                       \033[A")
        print(Fore.WHITE + Style.BRIGHT + "You rolled a:\n" + art)
        time.sleep(0.5)

        randFact = randint(0, 2)

        try:
          numFacts = funfacts.funfacts[int(rolled)]
          fact = numFacts[randFact]
          if fact[-1] in [".", ".\""]: #adds a period at the end if it doesnt have one
            print(Style.BRIGHT + "Fun fact: " + fact + "\n")
          else:
            print(Style.BRIGHT + "Fun fact: " + fact + ".\n")
        except KeyError:
          pass
  except:
    print("Please enter a number!\n")
  