# Complete Rewrite for full release v1.0 #
## Current Version: alpha v2.0 ##

# Changelog #

## Changes in alpha v1.0 ##
- Added a function that only searches for a subreddit format that was implemented in order to elimiate false positives for bot replies. Prior to this change, the bot would recognize the first character mentioned in the comment regardless of whether or not the new content post was about them. Now, this format eliminates them provided that the moderators use the proper format. (Please note: Bot will not reply to any comments if the format is not followed.)


## Changes from older versions: ##

- Readded "and comment.created_utc > start_time:" to the beginning of the main function. I intend to fix it. This function is to make sure that it only replies to comments that were created after the initial launch of the bot. ~~As of beta v13.3a, it only works about 40% of  the time, and only for certain characters. Next release should fix that.~~ ***This function now works as of alpha v1.0*** If you run into issues with the bot not replying to anything and just showing "The Bot is now ready", add a # to the beginning of line 138 and remove the # from line 139 then run the bot. (Or if you want to search comments from the past )

- Optimized bot for running 24/7 on a hosted server. This was done by creating a While true: Try/Except exception condition which tries to execute the main program, but if it runs into any errors, it doesn't exit. It just restarts. This will also show debug codes.

- Changed spelling of the replies to abide by the theme of the subreddit

- Fixed issue where the elif statements were listed inside the Kitana if statement and the elif statements would never have a condition to run.

# TODO #

- Use variables to define the praw.ini authentication fields so that a user may run this bot from an EXE file (expected to be implemented by or in release v1.0).

- Utilize characters.txt for reading usernames. (File not yet in use. It just exists in the repo for the future.)

- ~~Fix issue where bot only replies a certain percentage of the time~~

- ~~Work out solution to issue where a false positive will ensue if two different characters are mentioned in one comment~~ Issue fixed by implementing a format for the moderators of the subreddit to use which the bot will search for. Instead of just a character name, the bot will now search for "New kontent on:" Followed by the character name. 

# Moderator bot for MK11PremiumStore #

Hello! Welcome to the biggest bot I have ever written by far.

This is a bot that searches a Moderator's distinguished comment for each one of the characters within the file, and mentions the people who subscribed for notifications in a reply to the original comment. scroll down to the bottom to see the instructions on modifying the subscriber lists and reply text.

If you encounter any bugs, the program replies with/to something it shouldn't, or you'd like to suggest a feature, file an issue report, or message me on reddit at u/kapow-bitch and I will see what I can do to improve it.

To use this program, follow these instructions:

- Install Python3. Python2 will not work due to major formatting differences. If you intend to run program on a Linux based operating system or MacOS, scroll down to the respective section below. ***PLEASE NOTE: on the first screen that pops up during the Python installation on Windows, you will see a checkbox that says "add Python3.x to PATH". Check this box. You will have trouble running this bot if you don't check the box.***

- Install Praw. Do this by going into the command prompt and typing "pip install praw" (note: you must have Python installed to do this, and Python must be added to the PATH variable in Windows.)
- Create an app in the Reddit settings. To do that, follow these steps:
    - Go to https://www.reddit.com/prefs/apps
    - scroll down until you see "Create another app" or if you're not a nerd like me, click the box that says "Are you a developer? Create an app..." or something like that. I don't wanna delete my apps to find out. You get the point.
    - name it whatever you would like.
    - You will see 3 selection options. "Web app," "Installed app," and "Script." For this, you will choose "Script."
    - Description: Just type jibberish text in this box.
    - About URL: just type "http://www.example.com." (Without quotes)
    - Redirect URL: Same as About URL.
    - Click "Create app"
    - Keep this tab open for the "Setting up Praw.ini" section.
    - (Optional) Install Geany text editor for easy code editing and running. I only recommend this text editor because it's easy to use and install, however, this is not an absolutely required step. It's just here if you want it to make running the bot easier. (Please Note: I am not affilated with Geany or its developers in any way, it is just the first text editor that I used when learning how to code and it made running Python scripts easier.
    - Open main.py in geany. This file looks small I know. However, all the brains of the app is in replier.py. The main.py file optimizes it for running 24/7 on a hosted server so that in the event that Reddit or the API goes down temporarily, you don't have to manually restart it as it will be constantly running due to the While True: Try/Except exception condition.
    - To run program in geany, simply press the F5 key.
    - Thank You and I hope you enjoy this program!


# Setting up Praw.ini.
- You will next need to setup the Praw.ini file. I have included a shell file for you within the files. It is in the folder "init praw file." On many online examples, you'll see people plug their credentials straight into their main python file. I discourage doing that as it just leaves your credentials out in the open for people to see if you share that file with others and forget that your credentials are still in there.
    - Open the Praw.ini shell file from the repository.
    - Open the tab with the app you just created.
    - client_id: 2 spaces underneath your script name is the client_id. Copy and paste that into your Praw.ini file under "client_id"
    - client_secret: You will see something in the applet page you just created that says "Secret." The code to the right of that is your client secret. Copy and paste that into the client secret portion of the praw.ini file.
    - password: your reddit password
    - username: your reddit username
    - user_agent: Enter jibberish here. I just put "Idk" (without the quotes.)
    - Put the praw.ini file in the same folder that the main and replier files are. Otherwise, program will have trouble importing it.


# Instructions for running bot on Linux.
- Depending on the Operating system that you are using, Python3 may already be installed. If you're unsure if it is or not, go into the terminal and check by typing "Python3 --version." If it is installed, the output of that response will tell you which Python3 version you are running.


- If Previous step turns back an error such as "Python3 not found," type "sudo apt-get install Python3" to install Python3.


- Install pip package manager in order to install the praw module. If you already have Python pip3 installed, skip this step. If you don't, or are unsure, type "sudo apt-get install Python3-pip." (If using macOS, the command is: )


- (Optional) Install Geany text editor for easy code editing and running. I only recommend this text editor because it's easy to use and install, however, this is not an absolutely required step. It's just here if you want it to make running the bot easier. (Please Note: I am not affilated with Geany or its developers in any way, it is just the first text editor that I used when learning how to code and it made running Python scripts easier.)


- Setting up the Praw.ini. (See above: Setting up the Praw.ini file.)

- Right click in the folder where main.py is and type: "Python3 main.py" in order to run the file. If you run into any errors, file an issue report.


# Installing on MacOS
- If you already have Python3 installed, follow the Linux tutorial starting with "Install Geany" as Linux and MacOS instructions are the same. If you don't know if you have Python3 installed, type "Python3 --version" in the terminal. If this returns with something like "Python 3.7.3", make sure you have pip installed by typing "pip3 --version." If both of those come back with a version number, go to the Linux install instructions. If not, continue here.

- To install Python3 and Pip on MacOS, follow [this tutorial](https://evansdianga.com/install-pip-osx/).

- After you have installed Python3 and pip for Python3, you can follow the rest of the Linux instructions as they are the same.

# Modification instructions
- To add a user to a notification subscription to a certain character, follow these steps:

    I will use Jade's subscriber list as an example.

    Default code is this for every character:

    Jade_subs_original = ['u/kapow-bitch\n\n' 'u/RikimaruLDR\n\n']
    Jade_subs = ', '.join(map(str, Jade_subs_original))


    let's say you wanted to add u/bdoghomieg123 to the list. then the list would become:


    Jade_subs_original = ['u/kapow-bitch\n\n' 'u/RikimaruLDR\n\n' 'u/bdoghomieg123\n\n']
    Jade_subs = ', '.join(map(str, Jade_subs_original))


    Simply add a space, write 'u/<username>\n\n' (with the single quote. Output will be messy if you use traditional quotation marks.) It's Simple as that. Adding "\n\n" at the end of every u/ is vital, as that means "New line" which spaces out the comment to make it readable and less jumbled.


- To Remove a user, just remove 'u/[username]' and they will not receive mentions anymore.

- To edit the reply text for a certain character, go to the elif statement with that character's name, find the line that starts with "comment.reply" and edit the text within the quotation marks. (Note: Do not touch the text that says something like "+str(Cetrion_subs[0:])" That is the part of the code that adds all the subscriber's usernames to the comment.)

- If you have any other questions, DM the creator of the bot: u/kapow-bitch on Reddit.
