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
Kitana_subs_original = ['u/PlumbusProducer\n\n' 'u/LukeSkywalker1848\n\n']
Kitana_subs = ', '.join(map(str, Kitana_subs_original))

#Kitana 2 Subs
Kitana2_subs_original = ['u/Kanzuki_\n\n' 'u/Destroyer-YRU\n\n' 'u/mealzonwheelz90\n\n']
Kitana2_subs = ', '.join(map(str, Kitana2_subs_original))


#test
#Kitana 3 Subs
Kitana3_subs_original = ['u/king_ash\n\n' 'u/Deaf30\n\n' 'u/Nox_Box\n\n']
Kitana3_subs = ', '.join(map(str, Kitana3_subs_original))

#Jade Subs
Jade_subs_original = ['u/Enigmagico\n\n' 'u/jonwilsonlee\n\n']
Jade_subs = ', '.join(map(str, Jade_subs_original))

#Erron Black subs
EB_subs_original = ['u/VenomPool9\n\n' 'u/Emachine98\n\n' 'u/00110010110\n\n']
EB_subs = ', '.join(map(str, EB_subs_original))

#Erron Black 2 subs
EB2_subs_original = ['u/Enigmagico\n\n' 'u/jonwilsonlee\n\n']
EB2_subs = ', '.join(map(str, EB2_subs_original))

#Kabal Subs
Kabal_subs_original = ['u/Emachine98\n\n' 'u/Imo090\n\n' 'u/Donconario']
Kabal_subs = ', '.join(map(str, Kabal_subs_original))

#Kabal 2 Subs
Kabal2_subs_original = ['u/vegeta121212\n\n' 'u/HatMonkey7\n\n' 'u/DrTejszelet\n\n']
Kabal2_subs = ', '.join(map(str, Kabal2_subs_original))

#Kabal 3 Subs
Kabal3_subs_original = ['u/WrongOpinionDude\n\n']
Kabal3_subs = ', '.join(map(str, Kabal3_subs_original))

#Kung Lao subs
KL_subs_original = ['u/Enigmagico\n\n']
KL_subs = ', '.join(map(str, KL_subs_original))

#Sub-Zero Subs
SZ_subs_original = ['u/WrongOpinionDude\n\n' 'u/vegeta121212\n\n' 'u/tjplager32\n\n']
SZ_subs = ', '.join(map(str, SZ_subs_original))

#Scorpion Subs
Scorpion_subs_original = ['u/SpiderNoir14\n\n' 'u/vegeta121212\n\n' 'u/TardyTech4428\n\n']
Scorpion_subs = ', '.join(map(str, Scorpion_subs_original))

#Cetrion Subs
Cetrion_subs_original = ['u/HatMonkey7\n\n' 'u/SourRabbitz\n\n' 'u/Rift-Deidara\n\n']
Cetrion_subs = ', '.join(map(str, Cetrion_subs_original))

#Frost Subs
Frost_subs_original = ['u/PlumbusProducer\n\n' 'u/VenomPool9\n\n' 'u/Kanzuki_\n\n']
Frost_subs = ', '.join(map(str, Frost_subs_original))

#Frost 2 Subs
Frost2_subs_original = ['u/Tsalagi_\n\n' 'u/TardyTech4428\n\n' 'u/ZaXeroni\n\n']
Frost2_subs = ', '.join(map(str, Frost2_subs_original))

#Baraka Subs
Baraka_subs_original = ['u/SnakeSound222\n\n' 'u/gabrieluto\n\n']
Baraka_subs = ', '.join(map(str, Baraka_subs_original))

#Raiden Subs
Raiden_subs_original = ['u/TheLastPrime479\n\n' 'u/Zephyr1ne\n\n']
Raiden_subs = ', '.join(map(str, Raiden_subs_original))

#Shao Kahn Subs
SK_subs_original = ['u/theofficialdylpickle\n\n' 'u/vegeta121212\n\n' 'u/TardyTech4428\n\n']
SK_subs = ', '.join(map(str, SK_subs_original))

#Shao Kahn 2 Subs
SK2_subs_original = ['u/Dracuana\n\n' 'u/Jakedasnake28\n\n']
SK2_subs = ', '.join(map(str, SK2_subs_original))

#D'vorah Subs
DVH_subs_original = ['u/RikimaruLDR\n\n']
DVH_subs = ', '.join(map(str, DVH_subs_original))

#Jax Subs
Jax_subs_original = ['u/vegeta121212\n\n' 'u/anonamous34321\n\n']
Jax_subs = ', '.join(map(str, Jax_subs_original))

#Geras Subs
Geras_subs_original = ['u/CopyableTiger0\n\n']
Geras_subs = ', '.join(map(str, Geras_subs_original))

#Kano Subs
Kano_subs_original = ['u/Rift-Deidara\n\n' 'u/Nilyargton\n\n' 'u/vegeta121212\n\n']
Kano_subs = ', '.join(map(str, Kano_subs_original))

#Nightwolf Subs
Nightwolf_subs_original = ['u/Imo090\n\n' 'u/Rift-Deidara\n\n' 'u/Rated_R_Jobber\n\n']
Nightwolf_subs = ', '.join(map(str, Nightwolf_subs_original))

#Cassie Cage/CC Subs
CC_subs_original = ['u/Kuczera_Katze\n\n' 'u/cvrlosrivera\n\n' 'u/Nox_Box\n\n']
CC_subs = ', '.join(map(str, CC_subs_original))

#Cassie Cage2/CC2 Subs
CC2_subs_original = ['u/ZaXeroni\n\n']
CC2_subs = ', '.join(map(str, CC2_subs_original))

#Kotal Kahn Subs
KK_subs_original = ['u/RomyReptile\n\n' 'u/DrTejszelet\n\n']
KK_subs = ', '.join(map(str, KK_subs_original))

#Skarlet Subs
Skarlet_subs_original = ['u/SourRabbitz\n\n' 'u/Rift-Deidara\n\n']
Skarlet_subs = ', '.join(map(str, Skarlet_subs_original))

#Skarlet 2 Subs
Skarlet2_subs_original = ['u/DrTejszelet\n\n' 'u/mealzonwheelz90\n\n' 'u/Nox_Box\n\n']
Skarlet2_subs = ', '.join(map(str, Skarlet2_subs_original))

#Skarlet 3 Subs
Skarlet3_subs_original = ['u/gabrieluto\n\n' 'u/Steven_Chapman\n\n' 'u/necrocannibal2\n\n']
Skarlet3_subs = ', '.join(map(str, Skarlet3_subs_original))

#Sonya Blade Subs
SB_subs_original = ['u/Kuczera_Katze\n\n']
SB_subs = ', '.join(map(str, SB_subs_original))

#Shang Tsung Subs
ST_subs_original = ['u/WrongOpinionDude\n\n' 'u/Steven_Chapman\n\n']
ST_subs = ', '.join(map(str, ST_subs_original))

#Johnny Cage
JC_subs_original = ['u/nerksthetoastedtoast\n\n' 'u/Deaf30\n\n']
JC_subs = ', '.join(map(str, JC_subs_original))

#Noob Saibot Subs
NS_subs_original = ['u/fuzed_hostage\n\n' 'u/vegeta121212\n\n' 'u/TardyTech4428\n\n']
NS_subs = ', '.join(map(str, NS_subs_original))

#Noob Saibot 2 Subs
NS2_subs_original = ['u/Dracuana\n\n' 'u/tjplager32\n\n' 'u/gabrieluto\n\n']
NS2_subs = ', '.join(map(str, NS2_subs_original))

#Kollector Subs
Kollector_subs_original = ['u/Tsalagi_\n\n']
Kollector_subs = ', '.join(map(str, Kollector_subs_original))

#Jacqui Briggs Subs
JB_subs_original = ['u/king_ash\n\n']
JB_subs = ', '.join(map(str, JB_subs_original))

#Liu Kang 1 Subs
LK_subs_original = ['u/RomyReptile\n\n' 'u/thunderboyac\n\n' 'u/l3goManiac10\n\n']
LK_subs = ', '.join(map(str, LK_subs_original))

#Liu Kang 2 Subs
LK2_subs_original = ['u/kroona-4\n\n' 'u/Destroyer-YRU\n\n' 'u/jgraves0808\n\n']
LK2_subs = ', '.join(map(str, LK2_subs_original))

#Liu Kang 3 Subs
LK3_subs_original = ['u/JanSnow7290\n\n' 'u/nerksthetoastedtoast\n\n' 'u/Dracuana\n\n']
LK3_subs = ', '.join(map(str, LK3_subs_original))

#Liu Kang 4 Subs
LK4_subs_original = ['u/king_ash\n\n']
LK4_subs = ', '.join(map(str, LK4_subs_original))

#Terminator Subs
TRM_subs_original = ['u/swordclash117\n\n' 'u/WrongOpinionDude\n\n' 'u/gabrieluto\n\n']
TRM_subs = ', '.join(map(str, TRM_subs_original))

#Terminator2 Subs
TRM2_subs_original = ['u/CopyableTiger0\n\n' 'u/Helloisthisfood\n\n' 'u/Steel_Gazebo\n\n']
TRM2_subs = ', '.join(map(str, TRM2_subs_original))

#Terminator3 Subs
TRM3_subs_original = ['u/necrocannibal2\n\n']
TRM3_subs = ', '.join(map(str, TRM3_subs_original))
start_time = time.time()

def main():
    print("Informer systems booting up... Stand by...")
    time.sleep(2)
    comments_already_seen = []
    subreddit = reddit.subreddit('MK11PremiumStore') #The subreddit that it searches for the comments
    runNow = False
    #init setup. lets the user know that the bot isn't ready until it loops back to newer comments
    for comment in subreddit.stream.comments():
        comment_as_str = str(comment.body)
        if runNow == False:
            clear()
            print("Initialization Complete.")
            time.sleep(3)
            clear()
            print("Searching komments on", subreddit)
            runNow = True
        #if comment.distinguished:
        if comment.distinguished and comment.created_utc > start_time:#Looks for comments that are, mod distinguished and were created after the bot was started
            if comment.stickied: #If comment is stickied, performs the bot's action

                if 'kitana' in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(Kitana_subs[0:])+"\n\n\n"+"New kontent for Kitana Kahn is available")
                        comment.reply("Calling kombatants\n\n"+str(Kitana2_subs[0:])+"\n\n\n"+"New kontent for that blue female ninja is available")
                        comment.reply("Calling kombatants\n\n"+str(Kitana3_subs[0:])+"\n\n\n"+"New kontent for Kitana is available. Why she called Kitana when she uses fans??")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif 'jade' in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(Jade_subs[0:])+"\n\n\n"+"New kontent for Jade is available")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif 'kabal' in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(Kabal_subs[0:])+"\n\n\n"+"New kontent for Kabal is available")
                        comment.reply("Calling kombatants\n\n"+str(Kabal2_subs[0:])+"\n\n\n"+"New kontent for Speedy Gonzalez is available")
                        comment.reply("Calling kombatants\n\n"+str(Kabal3_subs[0:])+"\n\n\n"+"New kontent for Flash is available")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif 'kung lao' in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(KL_subs[0:])+"\n\n\n"+"New kontent for Kung Lao is available")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif 'sub zero' in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(SZ_subs[0:])+"\n\n\n"+"New kontent for Sub-Zero is available")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif 'sub-zero' in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(SZ_subs[0:])+"\n\n\n"+"New kontent for Sub-Zero is available")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif 'scorpion' in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(Scorpion_subs[0:])+"\n\n\n"+"New kontent for Scorpion is available")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif 'cetrion' in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(Cetrion_subs[0:])+"\n\n\n"+"New kontent for Cetrion is available")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif 'frost' in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(Frost_subs[0:])+"\n\n\n"+"New kontent for Frost is available. Tell her I love her.")
                        comment.reply("Calling kombatants\n\n"+str(Frost2_subs[0:])+"\n\n\n"+"New kontent for Frost is available. Isn't she beautiful?")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif 'baraka' in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(Baraka_subs[0:])+"\n\n\n"+"New kontent for Baraka is available")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif 'raiden' in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(Raiden_subs[0:])+"\n\n\n"+"New kontent for Raiden is available")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif 'shao kahn' in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(SK_subs[0:])+"\n\n\n"+"New kontent for Shao Kahn is available. Finally, a real man.")
                        comment.reply("Calling kombatants\n\n"+str(SK2_subs[0:])+"\n\n\n"+"New kontent for Shao Kahn is available. Stop - Hammer time.")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif "dvorah" in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(DVH_subs[0:])+"\n\n\n"+"New kontent for D'vorah is available")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif "jax" in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(Jax_subs[0:])+"\n\n\n"+"New kontent for Jax is available")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif "geras" in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(Geras_subs[0:])+"\n\n\n"+"New kontent for Geras is available")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif "kano" in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(Kano_subs[0:])+"\n\n\n"+"New kontent for Kano is available. Remember the Kanos cereal?")
                        comment.reply("Calling kombatants\n\n"+str(Kano2_subs[0:])+"\n\n\n"+"New kontent for Kano is available. Does he use Stark Industries tech?")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif "nightwolf" in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(Nightwolf_subs[0:])+"\n\n\n"+"New kontent for Nightwolf is available")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif "cassie cage" in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(CC_subs[0:])+"\n\n\n"+"New kontent for Cassie Cage is available")
                        comment.reply("Calling kombatants\n\n"+str(CC2_subs[0:])+"\n\n\n"+"New kontent for Calamity Cage is available")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif "cassie" in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(CC_subs[0:])+"\n\n\n"+"New kontent for Cassie Cage is available")
                        comment.reply("Calling kombatants\n\n"+str(CC2_subs[0:])+"\n\n\n"+"New kontent for Calamity Cage is available")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif "kotal kahn" in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(KK_subs[0:])+"\n\n\n"+"New kontent for Kotal Kahn is available")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif "kotal" in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(KK_subs[0:])+"\n\n\n"+"New kontent for Kotal Kahn is available")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif "skarlet" in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(Skarlet_subs[0:])+"\n\n\n"+"New kontent for Skarlet is available. Bloody hell...")
                        comment.reply("Calling kombatants\n\n"+str(Skarlet2_subs[0:])+"\n\n\n"+"New kontent for Skarlet is available. Blood for the Blood God!")
                        comment.reply("Calling kombatants\n\n"+str(Skarlet3_subs[0:])+"\n\n\n"+"New kontent for that female red ninja is available.")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif "sonya blade" in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(SB_subs[0:])+"\n\n\n"+"New kontent for Sonya Blade is available")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif "sonya" in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(SB_subs[0:])+"\n\n\n"+"New kontent for Sonya Blade is available")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif "shang tsung" in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(ST_subs[0:])+"\n\n\n"+"New kontent for Shang Tsung is available")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif "shang" in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(ST_subs[0:])+"\n\n\n"+"New kontent for Shang Tsung is available")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif "johnny cage" in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(JC_subs[0:])+"\n\n\n"+"New kontent for Johnny Cage is available. This guy isn't serious, is he?")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif "johnny" in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(JC_subs[0:])+"\n\n\n"+"New kontent for Johnny Cage is available. This guy isn't serious, is he?")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif "noob saibot" in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(NS_subs[0:])+"\n\n\n"+"New kontent for Noob Saibot is available. I refuse to stop making fun of your edgy boi.")
                        comment.reply("Calling kombatants\n\n"+str(NS2_subs[0:])+"\n\n\n"+"New kontent for Boob Saibot is available")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif "noob" in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(NS_subs[0:])+"\n\n\n"+"New kontent for Noob Saibot is available. I refuse to stop making fun of your edgy boi.")
                        comment.reply("Calling kombatants\n\n"+str(NS2_subs[0:])+"\n\n\n"+"New kontent for Boob Saibot is available")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif "kollector" in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(Kollector_subs[0:])+"\n\n\n"+"New kontent for Kollector is available")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif "jacqui briggs" in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(JB_subs[0:])+"\n\n\n"+"New kontent for Jacqui Briggs is available")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif "jacqui" in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(JB_subs[0:])+"\n\n\n"+"New kontent for Jacqui Briggs is available")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif "liu kang" in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(LK_subs[0:])+"\n\n\n"+"New kontent for The Chosen One is available")
                        comment.reply("Calling kombatants\n\n"+str(LK2_subs[0:])+"\n\n\n"+"New kontent for The Dragon is available")
                        comment.reply("Calling kombatants\n\n"+str(LK3_subs[0:])+"\n\n\n"+"New kontent for the man with the dragon tatoo is available")
                        comment.reply("Calling kombatants\n\n"+str(LK4_subs[0:])+"\n\n\n"+"New kontent for Liu Kang is available")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif "erron black" in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(EB_subs[0:])+"\n\n\n"+"New kontent for Erron Black is available. Yeehaw.")
                        comment.reply("Calling kombatants\n\n"+str(EB2_subs[0:])+"\n\n\n"+"New kontent for Broke-Black-Mountain is available.")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif "erron" in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(EB_subs[0:])+"\n\n\n"+"New kontent for Erron Black is available. Yeehaw.")
                        comment.reply("Calling kombatants\n\n"+str(EB2_subs[0:])+"\n\n\n"+"New kontent for Broke-Black-Mountain is available.")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()

                elif "terminator" in comment.body.lower():
                    if comment.id not in comments_already_seen:
                        comment.reply("Calling kombatants\n\n"+str(TRM_subs[0:])+"\n\n\n"+"New kontent for the Terminator is available. Your Krystals...give them to me...now!")
                        comment.reply("Calling kombatants\n\n"+str(TRM2_subs[0:])+"\n\n\n"+"New kontent for the Terminator is available. UZI Nine Milimetah...")
                        comment.reply("Calling kombatants\n\n"+str(TRM3_subs[0:])+"\n\n\n"+"New kontent for the Terminator is terminable.")
                        comments_already_seen.append(comment.id)
                        print("Replied to", comment.body)
                        time.sleep(3)
                        clear()
