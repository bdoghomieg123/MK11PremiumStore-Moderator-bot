import time
import random
import os
import platform

#Detects the operating system and uses that OS's terminal command to clear output based on one function
def clear():
    if platform.system() == "Linux": #If the OS is Linux
        os.system('clear') #Command for clearing terminal for Linux.

    elif platform.system() == "darwin": #If the OS is MacOS
        os.system("clear") #Linux and MacOS share commands but it's still a different OS so python sees it differently

    elif platform.system() == "Windows": #if the OS is Windows
        os.system('cls')
