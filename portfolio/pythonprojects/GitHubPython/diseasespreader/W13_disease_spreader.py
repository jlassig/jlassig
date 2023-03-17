import random
import pygame
import math

##adding buttons onto my menu and my resolution screen. see REFERENCE #8. I 
class Button:
   def __init__(self, text):
      HOSPITALIZED_RED = (255,0,0)
      button_font = pygame.font.SysFont("arial_black", 40)
      self.text = button_font.render(text,1, HOSPITALIZED_RED)
      self.size = self.text.get_size()
      self.surface = pygame.Surface((self.size))
      self.surface.blit(self.text, (0,0))

#to see if the people-dots collide or not: (see REFERENCE #3)
def is_Collision(x,y,x2,y2):    
  distance = math.sqrt((math.pow(x-x2,2))+(math.pow(y-y2,2)))
  if distance < 6:
    return True
  else:
    return False

#this is the percentage of the population that are completely immune to the disease.
def get_starting_immunity(user_immunity, starting_infecters, population):
     ##percentage of population that is just naturally immune: 
    starting_immunity = starting_infecters + (round(user_immunity * population))
    return starting_immunity

 #drawing each person in the population:   (see REFERENCE #1)
def draw_person(x, y, health_status, screen):
  #drawing a circle in pygame (see REFERENCE #7)
  pygame.draw.circle(screen, health_status, (x, y), 5) 

#this is the percentage on the end screen, total percentage of the population that died. 
def get_percent_dead(population, dead_counter):
  percent_dead = (dead_counter/population) * 100
  return percent_dead

#this is the percentage on the end screen, total percentage of the population that lived. 
def get_percent_living(population, dead_counter):
  living = (population-dead_counter)
  percent_living = (living/population) * 100
  return percent_living

def main():
 #initialize the pygame:
 pygame.init()

#  screen_width = 1200
#  screen_height = 710
##laptop:
 screen_width=1100
 screen_height=600
 screen = pygame.display.set_mode((screen_width, screen_height))
 #left to right is width or X
 #top to bottom is height or Y
 #upper left corner is 0,0

 #Title and Icon (these are on the top of the game "window")
 pygame.display.set_caption("Disease Spreader Simulation")
 ##some basic fonts to use: 
 button_font = pygame.font.SysFont("arial_black", 40)
 label_font = pygame.font.SysFont("arial_black", 30)
 key_font = pygame.font.SysFont("arial_black",20)
 #setting up a clock to count the time: (REFERENCE #5)
 clock = pygame.time.Clock()

 #I can't handle looking at a white screen, so:
 OFF_WHITE = (221,221,221)

 #colors used for the people circles in the simulation: 
 HEALTHY_PINK = (255,150,255)
 SICKLY_GREEN = (93,113,65)
 DEAD_BLACK = (0,0,0)
 RECOVERED_PURPLE = (177,104,255)
 HOSPITALIZED_RED = (255,0,0)

 #counter to go with each color:
 #healthy_counter is listed elsewhere
 infected_counter = 2
 dead_counter = 0
 recovered_counter = 0
 hospitalized_counter = 0
 total_hospitalized_counter = 0


 health_status = HEALTHY_PINK #starting off as pink for healthy) 
 #this color changes when the circle gets hit by another circle (infected-sickly green)
 #when time has passed after being sick (strong -recovered-purple)
 #when the patient dies. (immunity level was low and they got sick-black)
 #hospitalized (medium immunity, got sick, -red, then change to recovered or dead)

#the label headers for the menu screens:
#for the welcome screen: 
 welcome_label = label_font.render("Welcome to the", 1, DEAD_BLACK)
 game_name_label = label_font.render("Disease Spreader Simulation", 1, DEAD_BLACK)
 #a dummy label so I can get the width of "Begin"
 begin_label = label_font.render("Begin",1,DEAD_BLACK)
#for the population screen:
 label = label_font.render("Choose the population size:", 1, DEAD_BLACK)
#for the naturally immune screen:
 immunity_label = label_font.render("Choose the percentage of people", 1, DEAD_BLACK)
 immunity_label2 = label_font.render("that are naturally immune:",1, DEAD_BLACK)

#The Buttons:
#button for the welcome screen:
 begin_button = Button("Begin")
#the buttons for the population menu screen:
 small_town_button = Button("Small Town")
 large_town_button = Button("Large Town")
 city_button = Button("City")
 metropolis_button = Button("Metropolis")
#the buttons for the naturally immune screen:
 one_percent_button = Button("1%")
 five_percent_button = Button("5%")
 ten_percent_button = Button("10%")
 fifteen_person_button = Button("15%")
 #buttons for the resolution screen:
 yes_button = Button("Yes")
 no_button = Button("No")

#button coordinates for drawing the buttons: 
 first_columnX = screen_width/4
 second_columnX = screen_width/1.8
 top_rowY = 200
 bottom_rowY = 400


 ##setting up a global population variable:
 population = 0
 #this gets changed when the user chooses a population size:
 got_population = False 
 ##how many people started the sickness on day 0:
 starting_infecters = 2 
 #this gets changed when the user chooses the percentage of the population that are naturally immune. 
 got_user_immunity = False
 #how long each person is infections (in milliseconds)
 infectious_time = 7000
 #how long each person is in the hospital (in milliseconds)
 hospitalized_time = 9000
 #for the welcome screen, this gets changed after the user hits "Begin":
 welcomed = False

 ##we don't want to draw people OFF the screen or halfway off! Keep them on the screen!
 max_x_location = (screen_width-5)
 max_y_location = (screen_height-50)


 #we got a lot of lists here. I have no doubt that creating a person class would've been easier. Hopefully I learn how to do that in CSE 210
 def append_the_lists(population, starting_immunity):
  for i in range(population):
    # #the location of each person:
    #choosing a random number on the width of the screen
    personX.append(random.randint(5,max_x_location)) 
    #choosing a random number on the height of the screen 
    personY.append(random.randint(5,max_y_location))  
    ##get some random changes for the X and Y to move the person (see REFERENCE #2)
    personX_change.append(random.uniform(neg_speed, speed))
    personY_change.append(random.uniform(neg_speed, speed))
    #giving each individual a time and appending it to the list, see REFERENCE #5
    current_time = pygame.time.get_ticks()
    times_list.append(current_time)

    #these are the two people who escaped out of the Wuhan Institute of Virology lab: 
    if i < starting_infecters:
      health_status_list.append("infected")
      #I needed to assign some health level here, so I put their immune system at medium so they wouldn't be invincible (strong) or die off before the disease could spread (weak)
      immunity_list.append("medium")
      #this is for the percentage of the population that just doesn't seem to ever get sick. My husband is one of those. I will be at death's door with the flu and he maybe gets a "sniffle". 
    elif i >= starting_infecters and i < starting_immunity: 
      health_status_list.append("healthy")
      immunity_list.append("complete_immunity")
      #the rest of the population: 
    elif i > starting_infecters and i>= starting_immunity:
      health_status_list.append("healthy")
      #now we are going to randomly assign random immune system levels to the rest of the population. 
      random_immunity = ["weak", "medium", "strong"]
      immunity_list.append(random.choice(random_immunity)) 
  

 #keep the picture on the screen: 
 running = True
 
 while running: 
  if welcomed == False:
    #fill the screen with the Off-white color:
    screen.fill(OFF_WHITE)
    #create the welcome screen:
    screen.blit(welcome_label, (screen_width/2 - welcome_label.get_width()/2, 200))
    screen.blit(game_name_label,(screen_width/2-game_name_label.get_width()/2, 250))
    #get the width of the begin_label 
    begin_width = begin_label.get_width()/2
    #add a begin button and use the dummy label to get the width to center it:
    screen.blit(begin_button.surface,(screen_width/2-begin_width, screen_height/2))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      if event.type == pygame.MOUSEBUTTONDOWN:
        #get the current position of the mouse click:
        welcome_current_spot = pygame.mouse.get_pos()

        #compare the x and y coordinates of "current_spot" to where the buttons are located: 
        #small town:
        if (welcome_current_spot[0] > screen_width/2-begin_width and welcome_current_spot[0] < screen_width/2-begin_width + 120) and(welcome_current_spot[1] > screen_height/2 and welcome_current_spot[1]< screen_height/2 + 60):
          welcomed = True



  if got_population == False and welcomed:
     #create a list of the random people's X and Y coordinates:
    personX = []
    personY=[]
    #create a list of when the people change 
    personX_change = []
    personY_change = []
    #create a list of everybody's health status:
    health_status_list=[]
    #create a list of each person's immune system health level
    immunity_list=[]
    #a list for the times of each person:
    times_list=[]
    
  #fill the screen size that we've already defined as "screen" with the color off-white. 
    screen.fill(OFF_WHITE)
    #drawing the header label on the screen:
    screen.blit(label, (screen_width/2 - label.get_width()/2, 100))

    #drawing the buttons on the screen:    
    screen.blit(small_town_button.surface, (first_columnX, top_rowY))
    screen.blit(large_town_button.surface,(first_columnX, bottom_rowY))
    screen.blit(city_button.surface, (second_columnX, top_rowY))
    screen.blit(metropolis_button.surface,(second_columnX, bottom_rowY))

   
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      if event.type == pygame.MOUSEBUTTONDOWN:
        #get the current position of the mouse click:
        current_spot = pygame.mouse.get_pos()

        #compare the x and y coordinates of "current_spot" to where the buttons are located: 
        #small town:
        if (current_spot[0] > first_columnX and current_spot[0] < first_columnX + 250) and(current_spot[1] > top_rowY and current_spot[1]< top_rowY + 60):
          population = 150
          speed = 2
          neg_speed = -speed
          got_population = True
          healthy_counter = population - starting_infecters 
          

        #large town:
        elif (current_spot[0] > first_columnX and current_spot[0] < first_columnX + 250) and (current_spot[1] > bottom_rowY and current_spot[1] < bottom_rowY + 60):
          population = 300
          speed = 4
          neg_speed = -speed
          got_population = True
          healthy_counter = population - starting_infecters 

        #city:
        elif (current_spot[0] > second_columnX and current_spot[0] < second_columnX + 85) and (current_spot[1] > top_rowY and current_spot[1] < top_rowY + 60):
          population = 500
          speed = 8
          neg_speed = -speed
          got_population = True
          healthy_counter = population - starting_infecters 

        #metropolis:
        elif (current_spot[0] > second_columnX and current_spot[0] < second_columnX + 250) and (current_spot[1] > bottom_rowY and current_spot[1] < bottom_rowY + 60):
          population = 800
          speed = 15
          neg_speed = -speed
          got_population = True
          healthy_counter = population - starting_infecters 
 

  
  if got_population:

    screen.fill(OFF_WHITE)

    #drawing the labels for the immunity screen:
    screen.blit(immunity_label, (screen_width/2 - immunity_label.get_width()/2, 80))
    screen.blit(immunity_label2, (screen_width/2-immunity_label2.get_width()/2, 120))
    #drawing the buttons:

    screen.blit(one_percent_button.surface, (first_columnX, top_rowY))
    screen.blit(five_percent_button.surface,(first_columnX, bottom_rowY))
    screen.blit(ten_percent_button.surface, (second_columnX, top_rowY))
    screen.blit(fifteen_person_button.surface,(second_columnX, bottom_rowY))

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      if event.type == pygame.MOUSEBUTTONDOWN:
          #get the current position of the mouse click:
        immunity_current_spot = pygame.mouse.get_pos()

      #compare the x and y coordinates of "current_spot" to where the buttons are located:
       
        #one percent: 
        if (immunity_current_spot[0] > first_columnX and immunity_current_spot[0] < first_columnX + 65) and(immunity_current_spot[1] > top_rowY and immunity_current_spot[1]< top_rowY + 60):  
          ##1%:        
          user_immunity = .01
          got_user_immunity=True
          starting_immunity_num = get_starting_immunity(user_immunity, starting_infecters, population)
          
        #five percent:
        elif (immunity_current_spot[0] > first_columnX and immunity_current_spot[0] < first_columnX + 65) and(immunity_current_spot[1] > bottom_rowY and immunity_current_spot[1]< bottom_rowY + 60):
          ##5%:
          user_immunity = .05
          got_user_immunity=True
          starting_immunity_num = get_starting_immunity(user_immunity, starting_infecters, population)

        #ten percent:
        elif (immunity_current_spot[0] > second_columnX and immunity_current_spot[0] < second_columnX + 90) and(immunity_current_spot[1] > top_rowY and immunity_current_spot[1]< top_rowY + 60): 
          ##10%
          user_immunity = .10 
          got_user_immunity=True
          starting_immunity_num = get_starting_immunity(user_immunity, starting_infecters, population)

        #fifteen percent:
        elif (immunity_current_spot[0] > second_columnX and immunity_current_spot[0] < second_columnX + 90) and(immunity_current_spot[1] > bottom_rowY and immunity_current_spot[1]< bottom_rowY + 60): 
          ##15%:
          user_immunity = .15
          got_user_immunity=True
          starting_immunity_num = get_starting_immunity(user_immunity, starting_infecters, population)
      

  if got_population and got_user_immunity:

    #draw the screen:
    screen.fill(OFF_WHITE)

    #draw the key at the bottom of the screen:
    key_label = key_font.render(f"Key: infected = {infected_counter}", 1, SICKLY_GREEN)
    key_label2 = key_font.render(f"recovered = {recovered_counter}", 1, RECOVERED_PURPLE) 
    key_label3 = key_font.render(f"dead = {dead_counter}", 1, DEAD_BLACK)
    key_label4 = key_font.render(f"healthy = {healthy_counter}", 1, HEALTHY_PINK)   
    key_label5 = key_font.render(f"hospitalized = {total_hospitalized_counter}", 1, HOSPITALIZED_RED)   
    screen.blit(key_label, (30, screen_height-40 ))
    screen.blit(key_label2, (260, screen_height-40))
    screen.blit(key_label3, (460, screen_height-40))
    screen.blit(key_label4, (600, screen_height-40))
    screen.blit(key_label5, (780, screen_height-40))
    ##draw a line above the key: #see Reference 7
    pygame.draw.line(screen,DEAD_BLACK,(0,screen_height-43),(max_x_location,screen_height-43), width=3)


    ##fill in the info about each person:
    append_the_lists(population, starting_immunity_num)
  #so the user can exit out at any time: 
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      #this gives each person a health-status, draws each person and moves them: (see REFERENCE #1)
    for i in range(population):
        #the color to color the dots: 
      if health_status_list[i] == "infected":
        health_status = SICKLY_GREEN
      elif health_status_list[i] == "healthy":
        health_status = HEALTHY_PINK
      elif health_status_list[i] =="recovered":
        health_status = RECOVERED_PURPLE
      elif health_status_list[i] == "hospitalized":
        health_status = HOSPITALIZED_RED
      elif health_status_list[i] == "dead":
        health_status = DEAD_BLACK

      #draw each person dot
      draw_person(personX[i], personY[i], health_status, screen)

      #moving the people dots
      if personX[i] <= 5:
        personX_change[i] = speed
      elif personX[i] >= max_x_location:
        personX_change[i] = neg_speed
      if personY[i] <=5:
        personY_change[i] = speed
      elif personY[i] >= max_y_location:
        personY_change[i] = neg_speed

      #now to check for collisions: 
      for j in range(population):
        collision = is_Collision(personX[i], personY[i], personX[j], personY[j])
        ##if collision = true and person[i] is sick:
        if collision and health_status_list[i] == "infected" and health_status_list[j] == "healthy":
            #if person[j] is immune then just keep them pink
            if immunity_list[j] == "complete_immunity":
              draw_person(personX[j], personY[j], HEALTHY_PINK, screen)
            else:
            #otherwise: person[j] is sick!
              #update the time in the times list if someone gets infected, see Reference #5
              current_time = pygame.time.get_ticks()
              times_list[j] = current_time
              draw_person(personX[j], personY[j], SICKLY_GREEN, screen)
              #update person[j]'s health-status to show being sick. 
              health_status_list[j]="infected"
              infected_counter += 1
              healthy_counter -= 1
            # if i < starting_infecters:
            #   immunity_list[i] = "weak"

      #get the new time: see REFERENCE #5
      new_current_time = pygame.time.get_ticks()
      #people with strong immunities get recovered
      #how long since the person got infected: 
      if new_current_time-times_list[i]>infectious_time and health_status_list[i]=="infected" and immunity_list[i] == "strong":
        #if more than "infectious time", make the person "recovered"
        draw_person(personX[i], personY[i], RECOVERED_PURPLE, screen)
        health_status_list[i] ="recovered"
        recovered_counter += 1
        infected_counter -= 1

      #people with medium immunities get hospitalized
      if new_current_time-times_list[i]>infectious_time and health_status_list[i]=="infected" and immunity_list[i] == "medium":
        ##get the time they were hospitalized at: see REFERENCE #5
        get_hospitalized_time = pygame.time.get_ticks()        
        #if more than "infectious time", make the person "hospitalized"
        draw_person(personX[i], personY[i], HOSPITALIZED_RED, screen)
        health_status_list[i] ="hospitalized"
        hospitalized_counter += 1
        infected_counter -= 1
        total_hospitalized_counter += 1
        #the people then either die or recover: 
        new_immunity_list = ["strong", "weak"]
        immunity_list[i] = random.choice(new_immunity_list)
      if health_status_list[i] == "hospitalized" and get_hospitalized_time-times_list[i] > hospitalized_time and immunity_list[i] == "strong":
        #if the person has a strong immune system and they've been in the hospital long enough, make them "recovered"
        draw_person(personX[i], personY[i], RECOVERED_PURPLE, screen)
        health_status_list[i] ="recovered"
        recovered_counter += 1
        # infected_counter -= 1
      elif health_status_list[i] == "hospitalized" and get_hospitalized_time-times_list[i] > hospitalized_time and immunity_list[i] == "weak":
        #if more than "hospitalized time", and the person has a weak immune system,  make the person "dead"
        draw_person(personX[i], personY[i], DEAD_BLACK, screen)
        health_status_list[i] ="dead"
        dead_counter += 1
        # infected_counter -= 1

      ##people with low immunities die. 
      if new_current_time-times_list[i]>infectious_time and health_status_list[i]=="infected" and immunity_list[i] == "weak":
        #if more than "infectious time", make the person "dead"
        draw_person(personX[i], personY[i], DEAD_BLACK, screen)
        health_status_list[i] ="dead"
        dead_counter += 1
        infected_counter -= 1

      #dead people don't move, unless they are zombies. This isn't a zombie game, soooo....:
      if health_status_list[i] == "dead":
        personX_change[i] = 0
        personY_change[i]= 0
      personX[i] += personX_change[i]
      personY[i] += personY_change[i]
  
      #a resolution "screen". I want the percentages to show up at the top, the percentage of who lived and died, and I want all the people dots to move down to make room for this label. 
      #this happens when there are no more infected people: 
      if infected_counter == 0:
        #make everybody STOP. 
        personX_change[i]=0
        personY_change[i] = 0
        #if any of the dots are up at the top where I want to put my resolution label, move them down.
        if personY[i] < 55:
          personY[i] = 56
        #get the percentages for the living and the dead:
        living_percent = get_percent_living(population,dead_counter)
        dead_percent = get_percent_dead(population, dead_counter)
        #create a label with the info:
        resolution_label = key_font.render(f"Percentage of population that lived: {living_percent:.1f}%.       Percentage of population that died: {dead_percent:.1f}%.", 1, DEAD_BLACK)
        #print the label at the top of the screen. 
        # screen.blit(resolution_label,(30,0))
        screen.blit(resolution_label, (screen_width/2-resolution_label.get_width()/2, 5))
        #drawing a line below the percentages, see Reference 7
        pygame.draw.line(screen,DEAD_BLACK,(0,50),(max_x_location,50), width=3)
        #Professor Thayne suggested "Do you want to re-run the simulation" instead of "Do you want to play again?"That makes sense: 
        play_again_label = button_font.render(f"Do you want to re-run the simulation?", 1, DEAD_BLACK)
        screen.blit(play_again_label, (screen_width/2 - play_again_label.get_width()/2, 100))
        #putting a yes and no button on the screen
        screen.blit(yes_button.surface, (first_columnX, top_rowY))
        screen.blit(no_button.surface,(second_columnX, top_rowY))

        #get the position of the mouse for the Y or No buttons
        YorN_current_spot = pygame.mouse.get_pos()


        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            running = False
          if event.type == pygame.MOUSEBUTTONDOWN:
            #compare the x and y coordinates of "YorN_current_spot" to where the buttons are located:  
                 
            ## YES: 
            if (YorN_current_spot[0] > first_columnX and YorN_current_spot[0] < first_columnX + 75) and(YorN_current_spot[1] > top_rowY and YorN_current_spot[1]< top_rowY + 60): 
              #reset the booleans: 
              running = True
              got_population = False
              got_user_immunity = False
              ##reset the counters:
              infected_counter = 2
              dead_counter = 0
              recovered_counter = 0
              hospitalized_counter = 0
              total_hospitalized_counter = 0

            ## NO: 
            elif (YorN_current_spot[0] > second_columnX and YorN_current_spot[0] < second_columnX+45) and (YorN_current_spot[1] > top_rowY and YorN_current_spot[1] < top_rowY + 60):
              running = False


  #updates the contents of the entire pygame display screen 
  pygame.display.flip()
  #measures that we have 60 fps (frames per second)
  clock.tick(60)



if __name__ == "__main__":
 main()



# Lesson 13 Rubric
# Time—50%: Did you spend at least six hours on your Python program or test functions during the current lesson?   YES! I spent eight hours this week.  

# Description—10%: 

# The function names in my program:  main, draw_person, append_the_lists, is_Collision, and get_starting_immunity, get_percent_dead, get_percent_living

# The test function names in my test code: test_is_Collision, test_get_starting_immunity, test_get_percent_dead, test_get_percent_living


# #### REFERENCE LIST  ######
# 1.  https://www.youtube.com/watch?v=FfWpgLFMI7w&t=4283s  A space invaders type game that showed
# # simple movements of enemy sprites. I used a similar code for the movement and collision of my people-dots.

# 2.  I needed to slow down the animation. So, I decided to make my X and Y change be a smaller
# #random float number. If out how to do that here: https://pynative.com/python-get-random-float-numbers/#:~:text=The%20random.,Or%20from%2050.50%20to%2075.5.

# 3.  The distance formula from is_Collision came from: https://www.cuemath.com/geometry/distance-between-two-points/

# 4. The idea for code behind the disease simulation:
# # ####https://towardsdatascience.com/simulating-epidemics-using-go-and-python-101557991b20

# 5. getting the time: pygame.time.get_ticks()
# #https://www.pygame.org/docs/ref/time.html
#https://www.geeksforgeeks.org/pygame-time/
	
# 6: writing a test file:
# # https://video.byui.edu/media/t/1_9ickss60

# 7: How to draw lines and circles in pygame: 
##https://www.pygame.org/docs/ref/draw.html#pygame.draw.line

# 8: How to add a button, this one was a combination of the following:
######https://pythonprogramming.altervista.org/buttons-in-pygame/
##https://www.pygame.org/docs/ref/mouse.html#pygame.mouse.get_pressed
##https://stackoverflow.com/questions/48913087/get-just-the-x-or-y-pos-with-pygame-mouse-get-pos
 ## . 

# A description or list of the work that you finished on your program:

#This week I was able to add buttons to the menus at the start and to the resolution screen using MOUSEBUTTONDOWN instead of KEYDOWN. I was pretty excited about that, because it seemed more natural than having to press a certain key. I added a welcome screen with a "Begin" button and a resolution screen that shows the percentage of people that lived and the percentage the died. The resolution screen also has a "replay" with yes or no buttons. I added a key to the bottom of the screen with counters so the user could tell what the dots mean and watch as the people get infected, hospitalized, etc. With the help of Brother Thayne, I was also to get pytest working and test my functions. I am so proud of my little program. It looks and functions how I envisioned and as a bonus, I used a class for the Buttons! I'm pretty excited about that. 

