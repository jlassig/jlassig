import pygame
import random


pygame.init()
winHeight = 704
winWidth = 1200
win=pygame.display.set_mode((winWidth,winHeight))


WHITE = (255,255,255)
YELLOW = (255,233,127)
RED = (185, 50, 69)

numbers = []
big_numbers = []
signs = ['+', '-']
##ADDITION: 
easy_numbers=[1,19,2,3,6,17,7,8,9,10,11,18,15,12,13,4,5,14,16]
med_numbers=[24,6,33,67,89,13,2,71,10,8,4,100,91,32,55]
hard_numbers=[51,822,3,18,346,5,16,7,168,79,10,802,11,143,576,55,737,89,24,123,456,789]
crazy_numbers=[907,1345,6732,567,981,4321,6749,1298,45,984,1276,7834]
##SUBTRACTION:
big_numbers_easy = [865,946,865,745,956,999,785]
big_numbers_diff = [93456,92975,84890,94500,87425]
easy_sub = [1,2,3,7,6,8,9,4,5,10,11,12]
med_sub = [22,56,89,45,34,25,19,48,71,69,87,28]
hard_sub = [123,456,751,54,686,123,791,674,873,190,345,34,510,972,]
crazy_sub = [1234,7580,3456,2294,2571,3211,9874,6154,433,677,988]
##MIXED:



blackboard_background = pygame.image.load(r'C:\Users\Julia\Desktop\Python\CSE 110\Other\Abacus practice\GAMES\images\blackboard.png')
math_font = pygame.font.Font('freesansbold.ttf',30)
lineTxt = math_font.render('----------', 1, WHITE)
againTxt = math_font.render('Do you want to play again? Y or N', 1, RED)
levelTxt = math_font.render('Which level?  Easy  Medium  Hard  Crazy', 1, RED)
math_typeTxt = math_font.render('Choose:  Addition  Subtraction  Mixed', 1, RED)
timerTxt = math_font.render('Choose your timer:  Easy  Medium  Hard  Crazy  Genius', 1, RED)


got_timer = False
wait_time = 8000
running = True
play = False
math_type = 'math'
got_math_type = False

problems = [1,2,3,4]
problems2 = [5,6,7,8]
problems3= [9,10,11,12]
problems4 = [13,14,15]
turns = 0

def add_problems(problems, x_pos):
    global y_pos
    global sumAdd
    global turns
    global wait_time
    y_pos = 200
    for problem in problems:
        
        add_on = random.choice(numbers) 
        if len(str(add_on)) == 4:
            mathTxt = math_font.render(f'+  {add_on}', 1, WHITE )
        elif len(str(add_on)) == 3:
            mathTxt = math_font.render(f'+    {add_on}', 1, WHITE )
        elif len(str(add_on)) == 2:
            mathTxt = math_font.render(f'+      {add_on}', 1, WHITE )
        else:
            mathTxt = math_font.render(f'+        {add_on}', 1, WHITE )
        win.blit(mathTxt,(x_pos, y_pos))
        win.blit(lineTxt,(x_pos, (y_pos + 20)))
        y_pos += 100
        sumAdd += int(add_on)
        pygame.display.update()
        pygame.time.wait(wait_time)

        turns += 1
        print(problem)

def sub_problems(problems, x_pos):
    global y_pos
    global sub_diff
    global turns
    global wait_time

    y_pos = 200
    for problem in problems:
        sub_on = random.choice(numbers)
        if len(str(sub_on)) == 4:
            mathTxt = math_font.render(f'-  {sub_on}', 1, WHITE )
        elif len(str(sub_on)) == 3:
            mathTxt = math_font.render(f'-    {sub_on}', 1, WHITE )
        elif len(str(sub_on)) == 2:
            mathTxt = math_font.render(f'-      {sub_on}', 1, WHITE )
        else:
            mathTxt = math_font.render(f'-        {sub_on}', 1, WHITE )
        win.blit(mathTxt,(x_pos, y_pos))
        win.blit(lineTxt,(x_pos, (y_pos + 20)))
        y_pos += 100
        sub_diff -= int(sub_on)
        pygame.display.update()
        pygame.time.wait(wait_time)
        turns += 1
        print(problem)

def mix_problems(problems, x_pos):
    global y_pos
    global mix_total
    global turns
    global wait_time

    y_pos = 200
    for problem in problems:
        sign = random.choice(signs)
        sub_on = random.choice(numbers) 
        if len(str(sub_on)) == 4:
            mathTxt = math_font.render(f'{sign}  {sub_on}', 1, WHITE )
        elif len(str(sub_on)) == 3:
            mathTxt = math_font.render(f'{sign}    {sub_on}', 1, WHITE )
        elif len(str(sub_on)) == 2:
            mathTxt = math_font.render(f'{sign}      {sub_on}', 1, WHITE )
        else:
            mathTxt = math_font.render(f'{sign}        {sub_on}', 1, WHITE )
            
        if sign == '-':
            mix_total -= int(sub_on)
        elif sign == '+':
            mix_total += int(sub_on)
        
        win.blit(mathTxt,(x_pos, y_pos))
        win.blit(lineTxt,(x_pos, (y_pos + 20)))
        y_pos += 100

        pygame.display.update()
        pygame.time.wait(wait_time)        
        turns += 1
        print(problem)



while running:
    if got_math_type == False:
        win.fill(WHITE)
        win.blit(blackboard_background,(0,0))
        win.blit(math_typeTxt,(290,100))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_a:
                    math_type = 'addition'

                elif event.key == pygame.K_s:
                    math_type = 'subtraction'
 
                else:
                    math_type = 'mixed'
                got_math_type = True


    if play == False and got_math_type == True:
        win.fill(WHITE)
        win.blit(blackboard_background,(0,0))
        win.blit(levelTxt,(290,100))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_e:
                    if math_type == 'addition':
                        numbers = easy_numbers
                    elif math_type == 'subtraction' or math_type == 'mixed':
                        numbers = easy_sub
                        big_numbers = big_numbers_easy 

                elif event.key == pygame.K_h:
                    if math_type == 'addition':
                        numbers = hard_numbers
                    elif math_type == 'subtraction' or math_type == 'mixed':
                        numbers = hard_sub
                        big_numbers = big_numbers_diff 

                        big_numbers = big_numbers_easy
                elif event.key == pygame.K_c:
                    if math_type == 'addition':
                        numbers = crazy_numbers
                    elif math_type == 'subtraction' or math_type == 'mixed':
                        numbers = crazy_sub
                        big_numbers = big_numbers_diff               
                else:
                    if math_type == 'addition':
                        numbers = med_numbers
                    elif math_type == 'subtraction' or math_type == 'mixed':
                        numbers = med_sub
                        big_numbers = big_numbers_easy 
                play = True



    if play == True and got_timer == False:
        win.fill(WHITE)
        win.blit(blackboard_background,(0,0))
        win.blit(timerTxt,(190,100))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_e:
                    wait_time = 8000
                elif event.key == pygame.K_m:
                    wait_time = 6500
                elif event.key == pygame.K_h:
                    wait_time = 2000
                elif event.key == pygame.K_c:
                    wait_time = 600 
                elif event.key == pygame.K_g:
                    wait_time = 100
                else:
                    wait_time = 8000
                got_timer = True




##---------------------   ADDITION  -------------------------------------
    if play == True and math_type == 'addition' and got_timer == True: 
        if turns == 0:
            win.fill(WHITE)
            win.blit(blackboard_background,(0,0))
            add_on = random.choice(numbers)
            if len(str(add_on)) == 4:
                mathTxt = math_font.render(f'   {add_on}', 1, WHITE )
            elif len(str(add_on)) == 3:
                mathTxt = math_font.render(f'      {add_on}', 1, WHITE )
            elif len(str(add_on)) == 2:
                mathTxt = math_font.render(f'         {add_on}', 1, WHITE )
            else: 
                mathTxt = math_font.render(f'           {add_on}', 1, WHITE )
            win.blit(mathTxt,(100, 100))
            y_pos = 200
            sumAdd = add_on

            add_problems(problems, 100)

        elif turns == 4:
            add_problems(problems2, 400)

        elif turns == 8:
            add_problems(problems3, 700)

        elif turns == 12:
            add_problems(problems4, 1000)


        elif turns == 15:

            sumTxt = math_font.render(f'SUM: {sumAdd}', 1, WHITE)
            win.blit(sumTxt,(950, 500))
            win.blit(againTxt,(330, 100))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_y:
                        turns = 0
                        play = False
                        math_type = 'math'
                        got_math_type = False
                        got_timer = False
                    elif event.key == pygame.K_n:
                        running = False
                    else: running = False   
##--------------------------  SUBTRACTION  ---------------------------------------------              
                    
    if play == True and math_type == 'subtraction' and got_timer == True: 
        if turns == 0:
            win.fill(WHITE)
            win.blit(blackboard_background,(0,0))
            sub_on = random.choice(big_numbers)
            if len(str(sub_on)) == 5:
                mathTxt = math_font.render(f' {sub_on}', 1, WHITE )
            elif len(str(sub_on)) == 4:
                mathTxt = math_font.render(f'   {sub_on}', 1, WHITE )
            elif len(str(sub_on)) == 3:
                mathTxt = math_font.render(f'      {sub_on}', 1, WHITE )
            elif len(str(sub_on)) == 2:
                mathTxt = math_font.render(f'         {sub_on}', 1, WHITE )
            else: 
                mathTxt = math_font.render(f'           {sub_on}', 1, WHITE )
            win.blit(mathTxt,(100, 100))
            y_pos = 200
            sub_diff = sub_on

            sub_problems(problems, 100)

        elif turns == 4:
            sub_problems(problems2, 400)

        elif turns == 8:
            sub_problems(problems3, 700)

        elif turns == 12:
            sub_problems(problems4, 1000)


        elif turns == 15:

            subTxt = math_font.render(f'DIFF: {sub_diff}', 1, WHITE)
            win.blit(subTxt,(930, 500))
            win.blit(againTxt,(330, 100))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_y:
                        turns = 0
                        play = False
                        math_type = 'math'
                        got_math_type = False
                        got_timer = False
                    elif event.key == pygame.K_n:
                        running = False
                    else: running = False 

##----------------  MIXED ------------------------------------------------------
    if play == True and math_type == 'mixed' and got_timer == True:
        if turns == 0:
            win.fill(WHITE)
            win.blit(blackboard_background,(0,0))
            sub_on = random.choice(big_numbers)
            if len(str(sub_on)) == 5:
                mathTxt = math_font.render(f' {sub_on}', 1, WHITE )
            elif len(str(sub_on)) == 4:
                mathTxt = math_font.render(f'   {sub_on}', 1, WHITE )
            elif len(str(sub_on)) == 3:
                mathTxt = math_font.render(f'      {sub_on}', 1, WHITE )
            elif len(str(sub_on)) == 2:
                mathTxt = math_font.render(f'         {sub_on}', 1, WHITE )
            else: 
                mathTxt = math_font.render(f'           {sub_on}', 1, WHITE )
            win.blit(mathTxt,(100, 100))
            y_pos = 200
            mix_total = sub_on
            mix_problems(problems, 100)

        elif turns == 4:
            mix_problems(problems2, 400)

        elif turns == 8:
            mix_problems(problems3, 700)

        elif turns == 12:
            mix_problems(problems4, 1000)

        elif turns == 15:
            subTxt = math_font.render(f'TOTAL: {mix_total}', 1, WHITE)
            win.blit(subTxt,(900, 500))
            win.blit(againTxt,(330, 100))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_y:
                        turns = 0
                        play = False
                        math_type = 'math'
                        got_math_type = False
                        got_timer = False
                    elif event.key == pygame.K_n:
                        running = False
                    else: running = False 



    pygame.display.update()
    



    ##DONE! --play again?
    ##DONE! --add a way to either just see the sum! 
    ##or have the user ENTER the sum at the very end!!!
    ##DONE!! -- make it so there are 15 problems!
    ##DONE!! --make it so you can play on easy, medium, difficult in addition 
    ##DONE!! --choice between addition or subtraction or mixed! ! 
    ##DONE!!  --have a way for the user to put in a timer