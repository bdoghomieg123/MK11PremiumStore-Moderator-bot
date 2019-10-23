import praw #The Reddit API module
import os #send commands to the CMD/Terminal. This is complimentary to the common file to clear the output
import time #Used to create the start_time variable and slow down the speed at which some actions happen
from common import clear #Small little library I wrote for organizing things I commonly use in programs
import re #regular expression operations
import pprint #Used for debbuging praw modules.


reddit = praw.Reddit('bot1')
#Import the praw.ini file (Note, after cloning repo, you'll need to
#move this to the main folder and add it to a .gitignore if you plan on developing on this repo)

#Kitana Subs
Kitana_subs_original = ['u/kapow-bitch\n\n' 'u/RikimaruLDR\n\n']
Kitana_subs = ', '.join(map(str, Kitana_subs_original))


#Jade Subs
Jade_subs_original = ['u/kapow-bitch\n\n' 'u/RikimaruLDR\n\n']
Jade_subs = ', '.join(map(str, Jade_subs_original))

#Erron Black subs
EB_subs_original = ['u/kapow-bitch\n\n' 'u/RikimaruLDR\n\n']
EB_subs = ', '.join(map(str, EB_subs_original))

#Kabal Subs
Kabal_subs_original = ['u/kapow-bitch\n\n' 'u/RikimaruLDR\n\n']
Kabal_subs = ', '.join(map(str, Kabal_subs_original))

#Kung Lao subs
KL_subs_original = ['u/kapow-bitch\n\n' 'u/RikimaruLDR\n\n']
KL_subs = ', '.join(map(str, KL_subs_original))

#Sub-Zero Subs
SZ_subs_original = ['u/kapow-bitch\n\n' 'u/RikimaruLDR\n\n']
SZ_subs = ', '.join(map(str, SZ_subs_original))

#Scorpion Subs
Scorpion_subs_original = ['u/kapow-bitch\n\n' 'u/RikimaruLDR\n\n']
Scorpion_subs = ', '.join(map(str, Scorpion_subs_original))

#Cetrion Subs
Cetrion_subs_original = ['u/kapow-bitch\n\n' 'u/RikimaruLDR\n\n']
Cetrion_subs = ', '.join(map(str, Cetrion_subs_original))

#Frost Subs
Frost_subs_original = ['u/kapow-bitch\n\n' 'u/RikimaruLDR\n\n']
Frost_subs = ', '.join(map(str, Frost_subs_original))

#Baraka Subs
Baraka_subs_original = ['u/kapow-bitch\n\n' 'u/RikimaruLDR\n\n']
Baraka_subs = ', '.join(map(str, Baraka_subs_original))

#Raiden Subs
Raiden_subs_original = ['u/kapow-bitch\n\n' 'u/RikimaruLDR\n\n']
Raiden_subs = ', '.join(map(str, Raiden_subs_original))

#Raiden Subs
SK_subs_original = ['u/kapow-bitch\n\n' 'u/RikimaruLDR\n\n']
SK_subs = ', '.join(map(str, SK_subs_original))

#D'vorah SUbs
DVH_subs_original = ['u/kapow-bitch\n\n' 'u/RikimaruLDR\n\n']
DVH_subs = ', '.join(map(str, DVH_subs_original))

#Jax SUbs
Jax_subs_original = ['u/kapow-bitch\n\n' 'u/RikimaruLDR\n\n']
Jax_subs = ', '.join(map(str, Jax_subs_original))

#Geras Subs
Geras_subs_original = ['u/kapow-bitch\n\n' 'u/RikimaruLDR\n\n']
Geras_subs = ', '.join(map(str, Geras_subs_original))

#Kano Subs
Kano_subs_original = ['u/kapow-bitch\n\n' 'u/RikimaruLDR\n\n']
Kano_subs = ', '.join(map(str, Kano_subs_original))


#Nightwolf Subs
Nightwolf_subs_original = ['u/kapow-bitch\n\n' 'u/RikimaruLDR\n\n']
Nightwolf_subs = ', '.join(map(str, Nightwolf_subs_original))

#Cassie Cage/CC Subs
CC_subs_original = ['u/kapow-bitch\n\n' 'u/RikimaruLDR\n\n']
CC_subs = ', '.join(map(str, CC_subs_original))

#Kotan Kahn Subs
KK_subs_original = ['u/kapow-bitch\n\n' 'u/RikimaruLDR\n\n']
KK_subs = ', '.join(map(str, KK_subs_original))


#Skarlet Subs
Skarlet_subs_original = ['u/kapow-bitch\n\n' 'u/RikimaruLDR\n\n']
Skarlet_subs = ', '.join(map(str, Skarlet_subs_original))


#Sonya Blade Subs
SB_subs_original = ['u/kapow-bitch\n\n' 'u/RikimaruLDR\n\n']
SB_subs = ', '.join(map(str, SB_subs_original))


#Shang Tsung Subs
ST_subs_original = ['u/kapow-bitch\n\n' 'u/RikimaruLDR\n\n']
ST_subs = ', '.join(map(str, ST_subs_original))

#Johnny Cage
JC_subs_original = ['u/kapow-bitch\n\n' 'u/RikimaruLDR\n\n']
JC_subs = ', '.join(map(str, JC_subs_original))

#Noob Saibot Subs
NS_subs_original = ['u/kapow-bitch\n\n' 'u/RikimaruLDR\n\n']
NS_subs = ', '.join(map(str, NS_subs_original))

#Kollector Subs
Kollector_subs_original = ['u/kapow-bitch\n\n''u/RikimaruLDR\n\n']
Kollector_subs = ', '.join(map(str, Kollector_subs_original))

#Jacqui Briggs Subs
JB_subs_original = ['u/kapow-bitch\n\n' 'u/RikimaruLDR\n\n']
JB_subs = ', '.join(map(str, JB_subs_original))

start_time = time.time()

def main():
    print("Bot is Starting up... Please Wait...")
    time.sleep(2)
    comments_already_seen = []
    subreddit = reddit.subreddit('bdoghomieg123') #The subreddit that it searches for the comments
    runNow = False
    #init setup. lets the user know that the bot isn't ready until it loops back to newer comments
    for comment in subreddit.stream.comments():
        comment_as_str = str(comment.body)
        if runNow == False:
            clear()
            print("Bot Initialization Complete.")
            time.sleep(3)
            clear()
            print("Searching comments on r/",subreddit)
            runNow = True
        #if comment.distinguished:
        if comment.distinguished and comment.created_utc > start_time:#Looks for comments that are mod distinguished and were created after the bot was started
            if comment.stickied: #If comment is stickied, performs the bot's action
                if comment.id not in comments_already_seen:
                    if 'new kontent on: kitana' in comment.body.lower():
                        comment.reply("Calling All kombatants\n\n"+str(Kitana_subs[0:])+"\n\n\n"+"New kontent on Kitana Has been posted")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                    elif 'new kontent on: jade' in comment.body.lower():
                        comment.reply("Calling All kombatants\n\n"+str(Jade_subs[0:])+"\n\n\n"+"New kontent on Jade Has been posted")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                    elif 'new kontent on: kabal' in comment.body.lower():
                        comment.reply("Calling All kombatants\n\n"+str(Kabal_subs[0:])+"\n\n\n"+"New kontent on Kabal Has been posted")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()


                    elif 'new kontent on: kung lao' in comment.body.lower():
                        comment.reply("Calling All kombatants\n\n"+str(KL_subs[0:])+"\n\n\n"+"New kontent on Kung Lao Has been posted")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()


                    elif 'new kontent on: sub-zero' in comment.body.lower():
                        comment.reply("Calling All kombatants\n\n"+str(SZ_subs[0:])+"\n\n\n"+"New kontent on Sub-Zero Has been posted")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                    elif 'new kontent on: sub zero' in comment.body.lower():
                        comment.reply("Calling All kombatants\n\n"+str(SZ_subs[0:])+"\n\n\n"+"New kontent on Sub-Zero Has been posted")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                    elif 'new kontent on: scorpion' in comment.body.lower():
                        comment.reply("Calling All kombatants\n\n"+str(Scorpion_subs[0:])+"\n\n\n"+"New kontent on Scorpion Has been posted")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()


                    elif 'new kontent on: cetrion' in comment.body.lower():
                        comment.reply("Calling All kombatants\n\n"+str(Cetrion_subs[0:])+"\n\n\n"+"New kontent on Cetrion Has been posted")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                    elif 'new kontent on: frost' in comment.body.lower():
                        comment.reply("Calling All kombatants\n\n"+str(Frost_subs[0:])+"\n\n\n"+"New kontent on Frost Has been posted")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                    elif 'new kontent on: baraka' in comment.body.lower():
                        comment.reply("Calling All kombatants\n\n"+str(Baraka_subs[0:])+"\n\n\n"+"New kontent on Baraka Has been posted")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                    elif 'new kontent on: raiden' in comment.body.lower():
                        comment.reply("Calling All kombatants\n\n"+str(Raiden_subs[0:])+"\n\n\n"+"New kontent on Raiden Has been posted")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                    elif 'new kontent on: shao kahn' in comment.body.lower():
                        comment.reply("Calling All kombatants\n\n"+str(SK_subs[0:])+"\n\n\n"+"New kontent on Shao Kahn Has been posted")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                    elif "new kontent on: d'vorah" in comment.body.lower():
                        comment.reply("Calling All kombatants\n\n"+str(DVH_subs[0:])+"\n\n\n"+"New kontent on D'vorah Has been posted")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()


                    elif "new kontent on: jax" in comment.body.lower():
                        comment.reply("Calling All kombatants\n\n"+str(Jax_subs[0:])+"\n\n\n"+"New kontent on Jax Has been posted")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                    elif "new kontent on: geras" in comment.body.lower():
                        comment.reply("Calling All kombatants\n\n"+str(Geras_subs[0:])+"\n\n\n"+"New kontent on Geras Has been posted")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                    elif "new kontent on: kano" in comment.body.lower():
                        comment.reply("Calling All kombatants\n\n"+str(Kano_subs[0:])+"\n\n\n"+"New kontent on Kano Has been posted")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                    elif "new kontent on: nightwolf" in comment.body.lower():
                        comment.reply("Calling All kombatants\n\n"+str(Nightwolf_subs[0:])+"\n\n\n"+"New kontent on Nightwolf Has been posted")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                    elif "new kontent on: cassie cage" in comment.body.lower():
                        comment.reply("Calling All kombatants\n\n"+str(CC_subs[0:])+"\n\n\n"+"New kontent on Cassie Cage Has been posted")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                    elif "new kontent on: kotan kahn" in comment.body.lower():
                        comment.reply("Calling All kombatants\n\n"+str(KK_subs[0:])+"\n\n\n"+"New kontent on Kotan Kahn Has been posted")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                    elif "new kontent on: skarlet" in comment.body.lower():
                        comment.reply("Calling All kombatants\n\n"+str(Skarlet_subs[0:])+"\n\n\n"+"New kontent on Skarlet Has been posted")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                    elif "new kontent on: sonya blade" in comment.body.lower():
                        comment.reply("Calling All kombatants\n\n"+str(SB_subs[0:])+"\n\n\n"+"New kontent on Sonya Blade Has been posted")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                    elif "new kontent on: shang tsung" in comment.body.lower():
                        comment.reply("Calling All kombatants\n\n"+str(ST_subs[0:])+"\n\n\n"+"New kontent on Shang Tsung Has been posted")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                    elif "new kontent on: johnny cage" in comment.body.lower():
                        comment.reply("Calling All kombatants\n\n"+str(JC_subs[0:])+"\n\n\n"+"New kontent on Johnny Cage Has been posted")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                    elif "new kontent on: noob saibot" in comment.body.lower():
                        comment.reply("Calling All kombatants\n\n"+str(NS_subs[0:])+"\n\n\n"+"New kontent on Noob Saibot Has been posted")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                    elif "new kontent on: kollector" in comment.body.lower():
                        comment.reply("Calling All kombatants\n\n"+str(Kollector_subs[0:])+"\n\n\n"+"New kontent on Kollector Has been posted")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                    elif "new kontent on: jacqui briggs" in comment.body.lower():
                        comment.reply("Calling All kombatants\n\n"+str(Kollector_subs[0:])+"\n\n\n"+"New kontent on Jacqui Briggs Has been posted")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()
