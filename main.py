import praw
import os
import time
from common import clear
import os
from replier import main


reddit = praw.Reddit('bot1')

while True:
    try:
        print("Hello. Welcome to the MK11PremiumStore character update notification bot")
        input("\nThis bot is in alpha testing. It may not run as intended.\n\nPress ENTER to acknowledge and continue...")
        clear()
        main()

    except Exception as e: #Prints out the debug code as to why it couldn't run.
        clear()
        print("Bot failed to start. Trying again in 30 seconds.\n")
        print(e)
        time.sleep(30) #Pauses for 30 seconds, then retries to start.
        clear()
