
print()
#==========various choices to make: 
OPEN = ('\nYou carefully lift the lid a little and peer in. Quick as a flash a \nlittle man wearing a green tuxedo pops up, pinches your nose and laughs.')
# open_question = ('Do you reach in the box and CATCH the little man? Or do you CLOSE the lid of the box? ')
WAIT = ('\nYou decide to wait for your co-worker. She comes half an hour early and \ngets really excited when she sees the beautiful box. She quickly opens the lid \nand a little man in a green tuxedo pops up and hits her. ')
#wait_question = Do you reach out and CATCH the little man or do you HIT him?
HIT = ('\nYou bop the little man on the head and he shrinks back down in the box. You slam on the lid. \nA little voice pipes up, "Ye canna keep me trapped in here. Set me free!"')
# hit_question = Do you respond KINDLY, respond RUDELY or SHAKE the box?
CLOSE = ('\nYou smash the lid back on the little man\'s head and on top of the box. \nYou know that there is a leprechaun in there! How exciting! \nYou tell him, “I\'ve got you trapped, how can I get your gold?” \nHe responds, “Ye must correctly answer me two riddles.”  ')
# close_question = ('Do you ask for the first RIDDLE? Or do you SHAKE the box? ')
RUDELY = ('\n"Why would I set you free when you hit my friend?" you yell at the beautiful box. \n"Fine, fine, yer right. I wadna very nice. I\'ll share me gold wit ye if ye\'ll answer \ntwo riddles. The firs\'n is: "')
#rudely >> riddles
SHAKE = ('\nYou shake the box and the little voice cries out, \n“Stop, \'n I\'ll give ye sum\'ve me gold.” You stop shaking the box \nas a beautiful gold coin appears on the desk in front of you.')
# shake_question = ('Do you DEMAND more gold? or THANK him?')
DEMAND = ('\nOne coin? That\'s it? He must have more! "Give me more gold!" \nyou yell at the box. The little voice eerily whispers, \n"Ay, but the only way to get more\'ve me gold is to answer me two riddles."')
# demand_question = ('Do you ask for the first RIDDLE? Or do you SHAKE the box again?')  shake_2 is an ending
THANK = ('\nYou instantly feel bad because you were shaking the box. "Thank you for the gold," \nyou sheepishly tell the voice as you pocket the coin. You smell a burnt odor \nas the coin melts a hole in your pocket and the little voice chuckles, \n"Takin\' gold that ye wrongfully got is called stealin\'."')
# thank_question = ('Do you SHAKE the box again? or APOLOGIZE?') shake_2 is an ending
APOLOGIZE = ('\n"I\'m sorry," you say to the little man. The voice laughs and replies, \n"Do ye think me NAME is "Fooled Ye?" Dinna be \nflappin your lips if yer gonna be spoutin\' all that blarney! \nDinna yer mama never teach ye that lyin\'s jus\' as bad as stealin\'?"')
# NAME = secret name/ secret level where you guess the name!
#apologize_question = 'Do you SHAKE the box again? Or do you speak KINDLY to the box' (both are endings)
NAME = ('Since he had mentioned his name you ask, "What is your name?"  \n"Ahhhhh now we get to it...I knew ye were a tricky blighter. If ye can guess me name \nye gets all the treasure of all the Wee Folk. I\'ll give ye 10 chances. \nYe can guess a letter \'n I\'ll tell ye where it is in me name. ')
#name >> secret_name


#========various endings:
CATCH = ('\nYou reach out to catch the little man and he bites down on your finger. \nYou pull your hand back in pain and the little man leaps out of the box, \nacross the desk and out the door.')
KINDLY = ('\n"I\'ll set you free, but don\'t you come out swinging," you calmly \nwarn the little man. A very penitent voice says, "Fine, if ye\'ll let me go, \nI\'ll be nice." You open the box, and the little man jumps out, \ngleefully punches you on the nose and runs away. \nInside the box you find a large pile of gold.' )
SHAKE_2 = ('\nYou shake the box again, but you don\'t realize the lid is askew. \nThe lid pops off as the little man bounds out of the box and bops you \non the head before he and the box vanish without a trace. The rest of the day, \nyou still hear that tiny voice say with a mocking chuckle, \n"Hee hee hee, yer a right ninny-muggins."')

#========the riddles and gold endings:
RIDDLE = ('\nYou ask for the first riddle. The voice chuckles gleefully and says, "Heere is yer riddle:"')
riddle_1 = ('What kind of bow can\'t be tied? ')
riddle_1_reply = ('\n"I see that ye are smarter than ye look. But can ye answer me next riddle?"')
riddle_2 = ('What do you call a fake Irish stone? ')
GOLD = ('\nThe little man shrieks "I\'da never\'ve thought that a dunder-head like ye \nwould steal all me gold!" while piles of gold appear in front of you. The box and the \nlittle man vanish. You quit your job, take the gold and go on vacation with your family.')
riddle_wrong = ('\nThe voice squeals in peals of laughter and says, \n"I\'ve met troll dung smarter than ye!" \nThe box melts into a puddle of goo and vanishes.')
riddle_1_friend = ('\nYour co-worker pipes up, "No, the answer is rainbow!" \nThe little man groans inside the box. "It\'s almost cheatin\' but I\'ll give it to ye. \nLet\'s see if ye can answer me next riddle:"\n' )
riddle_2_friend = ('Your co-worker shakes her head and says, "Wait, the answer is shamrock!" \n"Hey now! I dinna say ye could phone a friend! Lucky for ye, she\'s a smart one."')
GOLD_2 = ('The little voice screams while huge piles of gold appear in front of you. \nThe box and the voice inside it vanish. You and your co-worker split the gold and quit your jobs.' )
# Just a note: I was at work when I was writing out the story, so the GOLD endings deal with quitting my job. lol


# ==============FUNCTIONS:

#=====Time to pretty things up:
header = '---SECRET LEVEL---' #because every good game has a secret level! ooh la la!
ending = '---THE END---' 

def the_pretty_stuff(title):
  format_spaces = '=' * 70
  print()
  #I learned how to do this formatting part from Aaron in our team:
  print(format_spaces) 
  print(title.center(70))
  print(format_spaces)

#==THANK function
def thank(gold_ending): #<--ooh! calling an argument in a function?!?! I was pretty excited to figure that out
  print(THANK)
  while True:
    thank_question = input('Do you SHAKE the box again? or APOLOGIZE? ')
    if (thank_question.upper() == 'SHAKE'):
      print(SHAKE_2)
      the_pretty_stuff(ending) #<--is that a function WITHIN a function???? yes, yes it is
    elif (thank_question.upper() == 'APOLOGIZE'):
      print(APOLOGIZE)
      while True:
        apologize_question = input('Do you SHAKE the box again? Or do you respond KINDLY? ')
        if apologize_question.upper() == 'SHAKE':
          print(SHAKE_2)
          the_pretty_stuff(ending)
        elif apologize_question.upper() == 'KINDLY':
          print(KINDLY)
          the_pretty_stuff(ending)
#==========SECRET NAME LEVEL==========
#====I really wanted this to be like the project in week 8 because I  wanted to have a "Rumpelstiltskin" moment in my game, but I couldn't for the life of me figure it out. ... YET.... Oh well. I simplified it for this week's assignment, 1 letter going through 1 string versus 1 string going through the 2nd string. Hopefully I can figure that out for week 8! 
        elif apologize_question.upper() == 'NAME':
            the_name = 'Fluffernuffer'  #oh yeah, that is a legit Leprechaun name! ha ha!
            guess = ""
            guess_counter = 0
            the_pretty_stuff(header)
            print(NAME)
            while (guess.capitalize() != the_name) and guess_counter < 10:
                letter_guess = input('What letter do ye want to guess? ')    
                for letter in the_name:
                    if letter.lower() == letter_guess.lower():
                        print(letter, end="")
                    else:
                        print('_ ', end="")
                guess = input('\nWhat\'s me name? ')
                guess_counter += 1
                if guess.capitalize() != 'Fluffernuffer':
                    print('"Yer dumber than a box o rocks. But I\'ll let ye try again."') #unfortunately, this also prints if you fail 10 times and before the game ends. 
            if (guess.capitalize() == the_name) and guess_counter < 11:
              print(f'\n"Well yer a sleeven one. It took ye {guess_counter} guesses."')  
              # According to Google, 'sleeven' means sly
              if guess_counter < 5:
                  print('"I\'m surprised ye got it so quick. Ye must be cheatin\'"')
              else:
                  print('"Yer dafter than I thought ye was."')
              print(gold_ending)
              the_pretty_stuff(ending)
            else:
              print(riddle_wrong)
              the_pretty_stuff(ending)
              continue 
            break                    
        else:
          print('Please enter only SHAKE or KINDLY.')
          continue
        break
    else:
      print('Please enter only APOLOGIZE or SHAKE.')
      continue
    break


#===RIDDLE FUNCTIONS:
def Riddle():
  print(RIDDLE)
 # ========RIDDLE 1
  riddle_1_answer = input(riddle_1)
  if (riddle_1_answer.upper()) == ('RAINBOW'):
    print(riddle_1_reply)
  #=========RIDDLE 2
    riddle_2_answer = input (riddle_2)
    if(riddle_2_answer.upper()) == ('SHAMROCK'):
      print(GOLD)
      the_pretty_stuff(ending)
    else:
      print(riddle_wrong)  
      the_pretty_stuff(ending)       
  else: 
    print(riddle_wrong)
    the_pretty_stuff(ending)


def friend_Riddle():
  # ========RIDDLE 1
  riddle_1_answer = input(riddle_1)
  if (riddle_1_answer.upper()) == ('RAINBOW'):
    print(riddle_1_reply)
  else:
    print(riddle_1_friend)
#============RIDDLE 2
  riddle_2_answer = input (riddle_2)
  if(riddle_2_answer.upper()) == ('SHAMROCK'):
    print(GOLD_2)
    the_pretty_stuff(ending)
  else:
    print(riddle_2_friend)
    print(GOLD_2)
    the_pretty_stuff(ending)




print('You arrive at work and find an ornately wrapped box at your desk. It must\'ve been \ndelivered last night! There are no names or labels on the box. Your co-worker \nwill be arriving in about an hour. Perhaps it is hers?')
while True: 
 box = input('Do you OPEN the box, or do you WAIT for your co-worker? ')
#==========OPEN:
 if (box.upper() == ('OPEN')):
  print(OPEN)
  while True:
   open_question = input('Do you reach in the box and CATCH the little man? Or do you CLOSE the lid of the box? ')
   if (open_question.upper() == ('CATCH')):
    print(CATCH)
    the_pretty_stuff(ending)
   elif (open_question.upper() == ('CLOSE')):
    print(CLOSE)
    while True:
     close_question = input('Do you ask for the first RIDDLE? Or do you SHAKE the box? ')
     if (close_question.upper() == ('RIDDLE')):
       Riddle()
     elif (close_question.upper() == ('SHAKE')):
      print(SHAKE)
      while True:
        shake_question = input('Do you DEMAND more gold? or THANK him? ')
        if (shake_question.upper() == ('DEMAND')):
          print(DEMAND)
          while True:
            demand_question = input('Do you ask for the first RIDDLE? Or do you SHAKE the box again? ')
            if (demand_question.upper() == ('RIDDLE')):
              Riddle()              
            elif (demand_question.upper() == ('SHAKE')):
              print(SHAKE_2)
              the_pretty_stuff(ending)
            else:
              print('Please enter only RIDDLE or SHAKE.')
              continue
            break
        elif (shake_question.upper() == ('THANK')):
          thank(GOLD)  # I'm very proud of my function plus argument! ooh la la! I'm learning all sorts of fun things over here!
        else:
          print('Please enter only DEMAND or THANK.')
          continue
        break
     else:
      print('Please enter only RIDDLE or SHAKE.')
      continue
     break
   else:
    print('Please only enter CATCH or CLOSE.')
    continue
   break
#==========WAIT:
 elif (box.upper() == ('WAIT')):
  print(WAIT)
  while True:  
    wait_question = input('Do you reach out and CATCH the little man or do you HIT him? ')
    if (wait_question.upper() == 'CATCH'):
      print(CATCH)
      the_pretty_stuff(ending)
    elif(wait_question.upper() == 'HIT'):
      print(HIT)
      while True: 
        hit_question = input('Do you respond KINDLY, respond RUDELY or SHAKE the box? ')
        if (hit_question.upper() == 'SHAKE'):
          print(SHAKE) 
          while True:
            shake_question = input('Do you DEMAND more gold? or THANK him? ')
            if (shake_question.upper() == ('DEMAND')):
              print(DEMAND)
              while True:
                demand_question = input('Do you ask for the first RIDDLE? Or do you SHAKE the box again? ')
                if (demand_question.upper() == ('RIDDLE')):
                  print(RIDDLE)
                  friend_Riddle()                       
                elif (demand_question.upper() == ('SHAKE')):
                  print(SHAKE_2)
                  the_pretty_stuff(ending)
                else:
                  print('Please enter only RIDDLE or SHAKE.')
                  continue
                break
            elif (shake_question.upper() == ('THANK')):
              thank(GOLD_2)
            else:
              print('Please enter only DEMAND or THANK.')
              continue
            break
        elif (hit_question.upper() == 'KINDLY'):
          print(KINDLY)
          the_pretty_stuff(ending)
        elif (hit_question.upper() == 'RUDELY'):
          print(RUDELY)
          friend_Riddle()
        else:
          print('Please only enter KINDLY, RUDELY or SHAKE.')
          continue
        break
    else:
      print('Please only enter CATCH or HIT.')
      continue
    break
 else:
  print('Please only enter OPEN or WAIT.')
  continue
 break


# Creativity: While Loops to make sure that the user only entered one of the two/three words asked for and several of the While Loops were nested, function (Riddle) to avoid repetition,  Function (Thank) with an argument,  secret level with hidden choice (NAME), FOR loop

#Extra Credit: I showed this to my adult daughter Sara and my husband Steve and had them both play through it and explained it to them. 
