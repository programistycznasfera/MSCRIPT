import time
import os
import webbrowser
import random
import operator
from operator import add 
def numberspin(number1, number2):
    random.randint(number1,number2)
def delay(delaytime):
    time.sleep(delaytime)
def printstrings(printstring):
    print(printstring)
def opensite(url):
    webbrowser.open_new_tab(url)
def deletefile(path):
    os.remove(path)
def addnumbers(number,numberalpha):
    operator.add(number + numberalpha)
def help():
    print("_______________________________")
    print("opensite = opens website")
    print("delay = time to wait")
    print("numberspin = generates random number")
    print("_______________________________")
