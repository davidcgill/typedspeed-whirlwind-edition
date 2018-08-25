# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 14:12:50 2018

@author: david

type tester:
    this program shows a word
    it shows what you have typed
    it has a 30 second countdown
    hit enter to move to next word  .... i could do letters per min and say average word is 4 or limit word size from 1 to 6 letters

    words typed/0.5 to get words per minute
    display score
    allow for play agian or quick

Future add ons:
    words flying at the wall
        words flying faster with time
        difficulty level changes lives and word length
        make a scoring system
        ... doesn't help me make my end goal but does help learn animation of motion
"""
#need this every time to make a something in pygame
import pygame, random
''' colours are not deffined so to decect we need to store them as rgb values
note how i put them outside all the functions therefor they are gobal and can be accessed anywhre.. also note the are tuples'''

black=(0,0,0)#black is all colours at a min
white=(255,255,255)#white is all colours at a max
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)

display_width=800
display_hieght=600

#main does setup and calls the main loop
pygame.init()


# setting up the window (surface).. pass width and height (one single argument, tuple)
gameDisplay = pygame.display.set_mode((display_width,display_hieght))  #top left is 0,0 ... soemthimes better to make these variables
gameDisplay.fill(black)
#puts a label on the window to help the user know whats going on
pygame.display.set_caption('type speed')

#define the games clock (sync everything with this)
clock=pygame.time.Clock()

#if you want to insert images
''' background=pygame.image.load("random_backdrop.jpg")  #insert with file name.. or if somewhere else on computer use full path
 gameDisplay.blit(background,(400,300)) #blit draws, order in which you draw layers it'''

def high_score_checker(myscore):
    infile=open("whirlscores.txt","r")
    highscores=[]
    highnames=[]
    updated=0
    scores=infile.readlines()
    ypos=0
    for words in scores:
        words=words.split(" ")

        #display the highscores
        text_display(words[0], (display_width/4, 20+ypos))
        text_display(words[1], (display_width/2+display_width/4, 20+ypos))

        highnames.append(words[0])
        highscores.append(words[1])
        ypos+=30

    infile.close()
    #above this point reads the file and displays them on screen

    index=0

    for score in highscores:
        #this loop checks if we beat the high score
        if myscore>= eval(score):
            #     once a high score is beat

            text_display("please type your name to be put into the hall of records",(display_width/2, display_hieght/2+40))
            text_display("Hit enter or space to confirm",(display_width/2, display_hieght/2+80))
            score_string= "your score is "+str(myscore)
            pygame.display.update()
            done=0
            name=""
            while not done:
                #let them type thier name and then wait for enter or sapce click
                for event in pygame.event.get():
                    if (event.type == pygame.KEYDOWN):
                        name,done =key_checker(event.key,name,1)
                        gameDisplay.fill(green)
                        text_display("please type your name to be put into the hall of records",(display_width/2, display_hieght/2+40))
                        text_display("Hit enter to confirm",(display_width/2, display_hieght/2+80))
                        text_display(name, (display_width/2, display_hieght/2+120))
                        score_string= "your score is "+str(myscore)
                        text_display(score_string,(display_width/2, display_hieght/2))


                        ypos=0
                        prindex=0
                        for words in highnames:

                            #display the highscores
                            text_display(words, (display_width/4, 20+ypos))
                            text_display(highscores[prindex], (display_width/2+display_width/4, 20+ypos))

                            ypos+=30
                            prindex+=1

                pygame.display.update()

            highscores.insert(index,str(myscore)+"\n")
            highnames.insert(index,name)
            highnames.pop(-1)
            highscores.pop(-1)
            updated=1
            break
        index+=1
    if updated:
        index=0
        outfile=open("whirlscores.txt","w")
        for name in highnames:
            print (f"{name} {highscores[index]}",file=outfile,end="")
            index+=1
        outfile.close()

def get_rand_words(num_of_words):
    #adding my text file
    words=[]
    chosen_ones=[]
    wordfile=open("words.txt","r")
    multi_words_per_line=wordfile.readlines()
    for word_string in multi_words_per_line:
        words+= word_string.split()
    length=len(words)
    #let's prelaod num_of_words  for each time (they can get up to 200 wpm).. this will make it run faster
    for x in range(0,num_of_words):
        index=random.randint(0,length-1)
        chosen_ones.append( words[index] )
    wordfile.close()
    return chosen_ones



def text_display(text,location,colour=white,size=32):
    font =pygame.font.SysFont('arial',size)# type then size
    try:
       textSurface =font.render(text, True , colour )# makes a text retangle
    except TypeError:
        print("sorry we couldn't print that, make sure you are passing strings")
        return
    else:
        text_rectangle= textSurface.get_rect()
        text_rectangle.center=(location) #this centers it at location
        gameDisplay.blit(textSurface,text_rectangle)
        pygame.display.update()

def key_checker(key,type_string,swap=0):
    if(key == pygame.K_a):
        type_string +="a"
    elif(key == pygame.K_b):
        type_string+="b"
    elif(key == pygame.K_c):
        type_string+="c"
    elif(key == pygame.K_d):
        type_string+="d"
    elif(key == pygame.K_e):
        type_string+="e"
    elif(key == pygame.K_f):
        type_string+="f"
    elif(key == pygame.K_g):
        type_string+="g"
    elif(key == pygame.K_h):
        type_string+="h"
    elif(key == pygame.K_i):
        type_string+="i"
    elif(key == pygame.K_j):
        type_string+="j"
    elif(key == pygame.K_k):
        type_string+="k"
    elif(key == pygame.K_l):
        type_string+="l"
    elif(key == pygame.K_m):
        type_string+="m"
    elif(key == pygame.K_n):
        type_string+="n"
    elif(key == pygame.K_o):
        type_string+="o"
    elif(key == pygame.K_p):
        type_string+="p"
    elif(key == pygame.K_q):
        type_string+="q"
    elif(key == pygame.K_r):
        type_string+="r"
    elif(key == pygame.K_s):
        type_string+="s"
    elif(key == pygame.K_t):
        type_string+="t"
    elif(key == pygame.K_u):
        type_string+="u"
    elif(key == pygame.K_v):
        type_string+="v"
    elif(key == pygame.K_w):
        type_string+="w"
    elif(key == pygame.K_x):
        type_string+="x"
    elif(key == pygame.K_y):
        type_string+="y"
    elif(key == pygame.K_z):
        type_string+="z"
    elif(key == pygame.K_BACKSPACE):
        type_string= type_string[0:-1]
    elif(key == pygame.K_SPACE and not swap):
        return type_string,1
    elif(key == pygame.K_SPACE and swap):
        type_string+="_"
    elif(key == pygame.K_RETURN):
        return type_string,1
    return type_string,0


'''
score will be derived be time survived+correct words (can play with formula later)

increasing difficulty speed of a appearing or movement speed
    movment speed


'''
def game_logic():
    speed_shift_time=15 # shifts every 15 seconds
    correct=0
    correct_count=0
    dead= 0 #(false).. this will kick us from the main game loop evenetually
    fill_colour=blue
    done=0
    type_string=""


    words = get_rand_words(200)#list of potential words
    disp_words=[]  # words from words currently being displayed
    disp_words_x=[] # the lsit of x positions
    disp_words_y=[]  # the lsit of y positiions

    wait_time=15 # every x loops of 10th seconds new word will appear (1.5 seconds)
    wait_counter=0# when resets every wait time (if changes on time the counter it could be almost)
    textbox=pygame.Rect(0,display_hieght-50,display_width,50) #Rect(left, top, width, height) -> Rect

    text_display("hit enter or space to start and to confirm each word typed", (display_width/2, display_hieght/2))
    text_display("hit h to view highscores", (display_width/2, display_hieght/2+40))
    text_display("type speed tester: Whirlwind edition", (display_width/2, display_hieght/2-40))
    pygame.display.update()

    while not done:
         for event in pygame.event.get():
             if (event.type== pygame.QUIT):
                gameDisplay.fill(fill_colour)
                return 0,"manual"
             if (event.type == pygame.KEYDOWN):
                 type_string,done =key_checker(event.key,type_string)
                 if type_string.find("h")>=0:
                     high_score_checker(0)
                     pygame.display.update()

    gameDisplay.fill(black)
    done=0 #marker to indicate if the string done being typed
    type_string=""
    time_passed=0
    text_display(str(time_passed),(755,20))
    clock_tick_tenth= 1

    pygame.time.set_timer(clock_tick_tenth,100)#10th of a second
    sec_counter=0

    disp_words_index=0
    disp_words.append(words[disp_words_index])
    disp_words_x.append(0)
    disp_words_y.append(random.randint(50,display_hieght-70))

    lives=3
    lives_left="<3 "*lives
    life_str= f"Lives: {lives_left}"
    pygame.draw.rect(gameDisplay,blue,textbox)
    lives_left="<3 "*lives
    life_str= f"Lives: {lives_left}"
    text_display(life_str,(70,20),size=20)
    text_display(str(time_passed),(755,20))
    while ( not dead):  #same as while collision ==0 .. while not true

                        #this grabs any event that happens on the window, where is mouse click, key click.... the loop will basicallyl check this once per frame
        for event in pygame.event.get():

            #giving the user a manual way out
            if (event.type== pygame.QUIT): # pygame. quit looks for when they try to x out the window
                fill_colour=black
                gameDisplay.fill(fill_colour)
                return 0,"manual"


            if (event.type == pygame.KEYDOWN):
                type_string,done =key_checker(event.key,type_string)
                if (done):
                    count=0
                    for current_word in disp_words:
                        letter_dex=0
                        length=len(current_word)
                        for letter in type_string:
                            # check if words match .. if they do  turn it green and show next word if not turn red and show next word
                            #order in the if is veryimportant other wise we would make false indexs.. instead it reads the first part and stops

                            if (letter_dex<length and letter == current_word[letter_dex]):
                                letter_dex+=1 #leaves it one high for later comparision
                                correct=1

                            else:
                                correct=0
                                break

                        if (correct and (letter_dex== length)):

                            correct_count+=1
                            fill_colour=green
                            del disp_words[count]
                            del disp_words_x[count]
                            del disp_words_y[count]
                            break

                        else:
                            fill_colour=red
                            correct=0

                        count+=1

                    type_string=""
                gameDisplay.fill(black)
                tempdex=0
                text_display(type_string, (display_width/2, display_hieght-25))
                pygame.draw.rect(gameDisplay,fill_colour,textbox)
                text_display(life_str,(70,20),size=20)
                text_display(str(time_passed),(755,20))
                disp_len=len(disp_words)-1
                while tempdex<=disp_len:
                    if (disp_words_x[tempdex]<250):
                        text_display(disp_words[tempdex],(disp_words_x[tempdex],disp_words_y[tempdex]),green,20)
                    elif(disp_words_x[tempdex]<600):
                         text_display(disp_words[tempdex],(disp_words_x[tempdex],disp_words_y[tempdex]),yellow,20)
                    elif (disp_words_x[tempdex]<display_width-15):
                         text_display(disp_words[tempdex],(disp_words_x[tempdex],disp_words_y[tempdex]),red,20)
                    tempdex+=1
                pygame.display.update()

            if(event.type == clock_tick_tenth):
                if (sec_counter==10):
                    time_passed+=1
                    sec_counter=0

                else:
                    sec_counter+=1

                if (time_passed%speed_shift_time==0):
                    wait_counter-=1# every 15 seconds increase appearance frequency


                if (wait_time<=wait_counter):
                    wait_counter=0
                    #make a new word appear
                    disp_words_index+=1
                    disp_words.append(words[disp_words_index])
                    disp_words_x.append(0)
                    disp_words_y.append(random.randint(50,display_hieght-70))

                else:
                    wait_counter+=1
                tempdex=0
                gameDisplay.fill(black)
                text_display(type_string, (display_width/2, display_hieght-25))
                pygame.draw.rect(gameDisplay,fill_colour,textbox)
                text_display(life_str,(70,20),size=20)
                text_display(str(time_passed),(755,20))
                text_display(type_string, (display_width/2, display_hieght-25))
                disp_len=len(disp_words)-1
                while tempdex<=disp_len:
                    disp_words_x[tempdex]+=5
                    if (disp_words_x[tempdex]<250):
                        text_display(disp_words[tempdex],(disp_words_x[tempdex],disp_words_y[tempdex]),green,20)
                    elif(disp_words_x[tempdex]<600):
                         text_display(disp_words[tempdex],(disp_words_x[tempdex],disp_words_y[tempdex]),yellow,20)
                    elif (disp_words_x[tempdex]<display_width-15):
                         text_display(disp_words[tempdex],(disp_words_x[tempdex],disp_words_y[tempdex]),red,20)
                    else:
                        lives-=1
                        lives_left="<3 "*lives
                        life_str= f"Lives: {lives_left}"
                        del disp_words[tempdex]
                        del disp_words_x[tempdex]
                        del disp_words_y[tempdex]
                        disp_len-=1
                        tempdex-=1 #have to subtract becuase of del there is a new element at tempdex (+1 next line leaves stagnant)
                        if (lives==0):
                            dead=1
                            break
                    tempdex+=1
                pygame.display.update()


                    # it will update the whole window, but if a pass a parameter i will only update that

                    #is a usful line to be able to see what pygame is seeing

        #on refresh white out screen and then redraw becuase layer do erase what was there previously

        pygame.display.update()# after we finish the for loop (figuring out what happened and drawing things e.c.t) we want to actually show it on the screen
        clock.tick(60)  # in here you place frames per seconds
    type_string=""
    gameDisplay.fill(fill_colour)
    return correct_count,"timeout"


def main():
    Exit=0

    while (not Exit):

        good_words,cauuse_of_death=game_logic()# game takes place here

        if cauuse_of_death=="manual":
            Exit=1

        elif cauuse_of_death=="timeout":


            score=good_words /0.5

            score_string= "your score is "+str(score)

            text_display(score_string,(display_width/2, display_hieght/2))
            pygame.display.update()
            pygame.time.delay(4000)
            high_score_checker(score)
            #infomation gets hidden in highscore
            gameDisplay.fill(black)
            text_display(score_string,(display_width/2, display_hieght/2))
            text_display("click anywhere to try again and the x to quit",(display_width/2,display_hieght/2-40))
            high_score_checker(0)
            pygame.display.update()

            screen_click=0
            while not screen_click:
                for event in pygame.event.get():
                    if (event.type== pygame.QUIT):

                        Exit=1
                        screen_click=1


                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        screen_click=1
                        gameDisplay.fill(black)
                        pygame.display.update()

    pygame.quit()
    quit()

if __name__=="__main__":
    main()