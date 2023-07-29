#
# CS 177 - project3.py
# Alex Panayotof and Shina Wang
# This program lets the user play Guess Master 3.0. This is a graphics
# driven game in which the user must guess 4-6 letter words. The user
# has 10 incorrect letter guesses per word, and the game continues until the user
# cannot guess the given word in the required amount of guesses.
#

# import libraries

from graphics import *

import random

import math

# define main() function

def main():

    # create control window

    controlwin,newbutton,quitbutton,hintbutton,hsbutton=control()

    # initialize round, score, general, scroll option, scroll objects, and terminate counter

    k=0

    score=10

    terminate=0

    scrolloption=0

    scrolls=[]

    data=[]

    highwin=0

    g=0

    # initialize streak counter and level

    streak=0

    l=0

    # infinite while loop

    while 2 != 3:

        # if quit is clicked while game is playing, close windows

        if terminate == 1:

            controlwin.close()

            gamewin.close()

            break

        # check for click in control panel

        controlclick=controlwin.checkMouse()

        if controlclick != None:

            controlclickx=controlclick.getX()

            controlclicky=controlclick.getY()

            # new game

            if 30 < controlclickx and controlclickx < 90 and 60 < controlclicky and controlclicky < 90:

                while 2 != 3:

                    # first round

                    if k == 0:

                        # create game window

                        gamewin,circlelist,textlist,wpolygonlist,bpolygonlist,rectanglelist,playword,alphabetlist=game()

                        # call play() function

                        result=play(gamewin,circlelist,textlist,wpolygonlist,bpolygonlist,rectanglelist,playword,alphabetlist,controlwin,score,scrolloption,highwin,scrolls,data,g,streak,l)

                        k+=1

                        # if win, display win text and start new round

                        if result[0] == True:

                            streak=result[7]

                            l=result[8]

                            scrolloption,highwin,scrolls,data,g=result[2:7]

                            score=result[1]+10

                            wintext=Text(Point(210,210),'YOU WIN - BOILER UP!')

                            wintext.setFill('grey')

                            wintext.setSize(24)

                            wintext.draw(gamewin)

                            continuetext=Text(Point(210,230),'Click to continue')

                            continuetext.setFill('grey')

                            continuetext.setStyle('italic')

                            continuetext.draw(gamewin)

                            gameclick=gamewin.getMouse()

                            k+=1

                            continue

                        # if lose, display lose text, prompt user for name, save game results, and close game window

                        elif result[0] == False:

                            streak=result[7]

                            l=result[8]

                            scrolloption,highwin,scrolls,data,g=result[2:7]

                            score=result[1]

                            # initiate sudden death; if player can guess the word, player continues with half score

                            sudden=Entry(Point(260,290),11)

                            sudden.setSize(18)

                            sudden.setFill('light grey')

                            sudden.draw(gamewin)

                            sbutton=Rectangle(Point(340,275),Point(415,305))

                            sbutton.setFill('light grey')

                            sbutton.draw(gamewin)

                            stext=Text(Point(377.5,290),'GUESS')

                            stext.setSize(18)

                            stext.setStyle('bold')

                            stext.draw(gamewin)

                            gameclick=gamewin.getMouse()

                            if 340 < gameclick.getX() and gameclick.getX() < 415 and 275 < gameclick.getY() and gameclick.getY() < 305:

                                finalguess=sudden.getText()

                                finalguess=finalguess.upper()

                                if finalguess == playword:

                                    score=int(score*.5)

                                    continue

                                # if wrong guess, game continues to end

                                else:

                                    sudden.undraw()

                                    sbutton.undraw()

                                    stext.undraw()
                            
                            entry=Entry(Point(270,290),11)

                            entry.setSize(18)

                            entry.setFill('light grey')

                            entry.draw(gamewin)

                            savebutton=Rectangle(Point(350,275),Point(405,305))

                            savebutton.setFill('light grey')

                            savebutton.draw(gamewin)

                            savetext=Text(Point(377.5,290),'SAVE')

                            savetext.setSize(18)

                            savetext.setStyle('bold')

                            savetext.draw(gamewin)

                            losetext=Text(Point(210,210),'GAME OVER - YOU LOSE!')

                            losetext.setFill('red')

                            losetext.setSize(24)

                            losetext.draw(gamewin)

                            endtext=Text(Point(210,230),'Click to close')

                            endtext.setFill('red')

                            endtext.setStyle('italic')

                            endtext.draw(gamewin)

                            gameclick=gamewin.getMouse()

                            if 350 < gameclick.getX() and gameclick.getX() < 405 and 275 < gameclick.getY() and gameclick.getY() < 305:

                                name=entry.getText()

                                save(name,score,k)

                                gameclick=gamewin.getMouse()

                            gamewin.close()

                            score=10

                            k=1

                            break

                        # if click in control panel

                        # if new game, start new round

                        elif result[0] == 'new':

                            k=1

                            streak=0

                            l=0

                            scrolloption,highwin,scrolls,data,g=result[2:7]

                            score=10

                            continue

                        # if quit, terminate game

                        elif result[0] == 'quit':

                            scrolloption,highwin,scrolls,data,g=result[2:7]

                            scrolloption=0

                            if g != 0:

                                highwin.close()

                            terminate+=1

                            break

                    # rounds after first round; code is identical to k=0 case

                    elif k != 0:

                        gamewin.close()

                        # after 2 rounds, user plays bonus round; after first bonus round, bonus round occurs every 3 rounds

                        if k % 3 == 0:

                            score=bonus(score)

                        gamewin,circlelist,textlist,wpolygonlist,bpolygonlist,rectanglelist,playword,alphabetlist=game()

                        result=play(gamewin,circlelist,textlist,wpolygonlist,bpolygonlist,rectanglelist,playword,alphabetlist,controlwin,score,scrolloption,highwin,scrolls,data,g,streak,l)

                        if result[0] == True:

                            streak=result[7]

                            l=result[8]

                            scrolloption,highwin,scrolls,data,g=result[2:7]

                            score=result[1]+10

                            wintext=Text(Point(210,210),'YOU WIN - BOILER UP!')

                            wintext.setFill('grey')

                            wintext.setSize(24)

                            wintext.draw(gamewin)

                            continuetext=Text(Point(210,230),'Click to continue')

                            continuetext.setFill('grey')

                            continuetext.setStyle('italic')

                            continuetext.draw(gamewin)

                            gameclick=gamewin.getMouse()

                            k+=1

                            continue

                        elif result[0] == False:

                            scrolloption,highwin,scrolls,data,g=result[2:7]

                            l=0

                            streak=result[7]

                            score=result[1]

                            sudden=Entry(Point(260,290),11)

                            sudden.setSize(18)

                            sudden.setFill('light grey')

                            sudden.draw(gamewin)

                            sbutton=Rectangle(Point(340,275),Point(415,305))

                            sbutton.setFill('light grey')

                            sbutton.draw(gamewin)

                            stext=Text(Point(377.5,290),'GUESS')

                            stext.setSize(18)

                            stext.setStyle('bold')

                            stext.draw(gamewin)

                            gameclick=gamewin.getMouse()

                            if 340 < gameclick.getX() and gameclick.getX() < 415 and 275 < gameclick.getY() and gameclick.getY() < 305:

                                finalguess=sudden.getText()

                                finalguess=finalguess.upper()

                                if finalguess == playword:

                                    score=int(score*.5)

                                    continue

                                else:

                                    sudden.undraw()

                                    sbutton.undraw()

                                    stext.undraw()

                            entry=Entry(Point(270,290),11)

                            entry.setSize(18)

                            entry.setFill('light grey')

                            entry.draw(gamewin)

                            savebutton=Rectangle(Point(350,275),Point(405,305))

                            savebutton.setFill('light grey')

                            savebutton.draw(gamewin)

                            savetext=Text(Point(377.5,290),'SAVE')

                            savetext.setSize(18)

                            savetext.setStyle('bold')

                            savetext.draw(gamewin)

                            losetext=Text(Point(210,210),'GAME OVER - YOU LOSE!')

                            losetext.setFill('red')

                            losetext.setSize(24)

                            losetext.draw(gamewin)

                            endtext=Text(Point(210,230),'Click to close')

                            endtext.setFill('red')

                            endtext.setStyle('italic')

                            endtext.draw(gamewin)

                            gameclick=gamewin.getMouse()

                            if 350 < gameclick.getX() and gameclick.getX() < 405 and 275 < gameclick.getY() and gameclick.getY() < 305:

                                name=entry.getText()

                                save(name,score,k)

                                gameclick=gamewin.getMouse()

                            gamewin.close()

                            score=10

                            k=1

                            break
                        
                        elif result[0] == 'new':

                            k=1

                            l=0

                            streak=0

                            scrolloption,highwin,scrolls,data,g=result[2:7]

                            score=10

                            continue

                        elif result[0] == 'quit':

                            scrolloption,highwin,scrolls,data,g=result[2:7]

                            scrolloption=0

                            if g != 0:

                                highwin.close()

                            terminate+=1

                            break

            # quit game
                
            elif 210 < controlclickx and controlclickx < 270 and 60 < controlclicky and controlclicky < 90:

                if k == 0:

                    controlwin.close()

                    if g != 0:

                        highwin.close()

                elif k != 0:

                    controlwin.close()

                    gamewin.close()

                    if g != 0:

                        highwin.close()

                break

            # high scores

            elif 100 < controlclickx and controlclickx < 200 and 95 < controlclicky and controlclicky < 115:

                # check for instance of button click

                if g != 0:

                    highwin.close()

                # call scoreboard()

                scrolloption,highwin,scrolls,data,g=scoreboard(g,controlwin)

        # check for click in high score window and close

        if scrolloption == 'scroll':

            highclick=highwin.checkMouse()

            if highclick != None:

                scrolloption=0

                highwin.close()

        # call scroll() if scroll option

        if scrolloption == 'scroll':

            scroll(highwin,scrolls,data)

# define play() function that lets user play game

def play(gamewin,circlelist,textlist,wpolygonlist,bpolygonlist,rectanglelist,playword,alphabetlist,controlwin,score,scrolloption,highwin,scrolls,data,g,streak,l):

    # initialize counters

    z=0

    w=0

    # display score

    scoretext=Text(Point(210,20),'SCORE: '+str(score))

    scoretext.setStyle('bold')

    scoretext.setSize(26)

    scoretext.draw(gamewin)

    # initialize placeholder list, placeholder string, playword list, right guess list, and wrong guess list

    placeholder=[]

    placehold=''

    playwordlist=[playword[i] for i in range(len(playword))]

    wronglist=[]

    rightlist=[]

    # create placeholder string

    for b in range(len(playword)):

        placeholder.append('-')

    # check for control panel and game window clicka

    while w<10:

        controlclick=controlwin.checkMouse()

        if controlclick != None:

            controlclickx=controlclick.getX()

            controlclicky=controlclick.getY()

            # if new game, quit game, or hint is clicked

            if 30 < controlclickx and controlclickx < 90 and 60 < controlclicky and controlclicky < 90:

                return ['new',score,scrolloption,highwin,scrolls,data,g,streak,l]

            elif 210 < controlclickx and controlclickx < 270 and 60 < controlclicky and controlclicky < 90:

                return ['quit',score,scrolloption,highwin,scrolls,data,g,streak,l]

            elif 115 < controlclickx and controlclickx < 185 and 265 < controlclicky and controlclicky < 285:

                # hint only once per round

                if z == 0:

                    wronglist,w=hint(circlelist,bpolygonlist,wronglist,playword,alphabetlist,textlist,w)

                    z+=1

            # if high score button is clicked

            elif 100 < controlclickx and controlclickx < 200 and 95 < controlclicky and controlclicky < 115:

                if g != 0:

                    highwin.close()

                scrolloption,highwin,scrolls,data,g=scoreboard(g,controlwin)

        gameclick=gamewin.checkMouse()

        if gameclick != None:

            # iterate through circles and see if any were clicked

            for i in range(0,len(circlelist)):

                circle=circlelist[i]

                if click(gameclick,circle) == True:

                    # change fill and text color

                    circle.setFill('gold')

                    textlist[i].setFill('black')

                    # check guess and display correct guess

                    for r in range(len(playword)):

                        if playword[r] == alphabetlist[i]:

                            answer=Text(rectanglelist[r].getCenter(),alphabetlist[i])

                            answer.setSize(24)

                            answer.draw(gamewin)

                            placeholder[r]=playword[r]

                            # add 1 to streak

                            streak+=1

                            if alphabetlist[i] in rightlist:

                                streak-=1

                            rightlist.append(alphabetlist[i])
    
                        else:

                            placeholder=placeholder

                    # if wrong guess, animate falling block,break streak, and change score

                    if alphabetlist[i] not in playwordlist:

                        # if redundant wrong guess, check for new click

                        if alphabetlist[i] in wronglist:

                            break

                        streak=0

                        wronglist.append(alphabetlist[i])

                        drop(bpolygonlist[w])

                        w+=1

                        score-=1
    
                        scoretext.setText('SCORE: '+str(score))

                    placehold=placehold.join(placeholder)

                    # if streak greater than 3, give user 3 points

                    if streak > 3:

                        score+=3

                        scoretext.setText('SCORE: '+str(score))

                    # define win condition

                    if placehold == playword:

                        return [True,score,scrolloption,highwin,scrolls,data,g,streak,l]

                    placehold=''

        # check for click in high score window and close

        if scrolloption == 'scroll':

            highclick=highwin.checkMouse()

            if highclick != None:

                scrolloption=0

                highwin.close()

        # call scroll() if scroll option

        if scrolloption == 'scroll':

            scroll(highwin,scrolls,data)

        # if streak detected, fill streak bar with corresponding amount of rectangles (max 3); if streak broken, unfill streak bar

        if streak == 0:

            if l == 1:

                rstreak1.setFill('black')

                l=0

            elif l == 2:

                rstreak2.setFill('black')

                rstreak1.setFill('black')

                l=0

            elif l == 3:

                rstreak3.setFill('black')

                rstreak2.setFill('black')

                rstreak1.setFill('black')

                l=0

        elif streak == 1:

            rstreak1=Rectangle(Point(22,236),Point(48,288))

            rstreak1.setFill('gold')

            rstreak1.draw(gamewin)

            l=1

        elif streak == 2:

            rstreak1=Rectangle(Point(22,236),Point(48,288))

            rstreak1.setFill('gold')

            rstreak1.draw(gamewin)

            rstreak2=Rectangle(Point(22,184),Point(48,236))

            rstreak2.setFill('gold')

            rstreak2.draw(gamewin)

            l=2

        elif streak >= 3:

            rstreak1=Rectangle(Point(22,236),Point(48,288))

            rstreak1.setFill('gold')

            rstreak1.draw(gamewin)

            rstreak2=Rectangle(Point(22,184),Point(48,236))

            rstreak2.setFill('gold')

            rstreak2.draw(gamewin)

            rstreak3=Rectangle(Point(22,132),Point(48,184))

            rstreak3.setFill('gold')

            rstreak3.draw(gamewin)

            l=3
        
    # lose condition

    return [False,score,scrolloption,highwin,scrolls,data,g,streak,l]

# define bonus() function that operates bonus round

def bonus(score):

    # initialize prizes and prize

    prize=0

    prizes=[-7,0,7]

    # create bonus round graphics

    bonuswin=GraphWin('Bonus Round!',300,300)

    bonuswin.setBackground('black')

    bonustext=Text(Point(150,30),'Please Claim Your Prize!')

    bonustext.setSize(24)

    bonustext.setFill('gold')

    bonustext.setStyle('bold')

    bonustext.draw(bonuswin)

    opt1=Rectangle(Point(50,100),Point(100,200))

    opt1.setFill('gold')

    opt1.draw(bonuswin)

    opt1text=Text(Point(75,150),'Prize 1')

    opt1text.setSize(12)

    opt1text.setStyle('bold')

    opt1text.setFill('black')

    opt1text.draw(bonuswin)

    opt2=Rectangle(Point(125,100),Point(175,200))

    opt2.setFill('gold')

    opt2.draw(bonuswin)

    opt2text=Text(Point(150,150),'Prize 2')

    opt2text.setSize(12)

    opt2text.setStyle('bold')

    opt2text.setFill('black')

    opt2text.draw(bonuswin)

    opt3=Rectangle(Point(200,100),Point(250,200))

    opt3.setFill('gold')

    opt3.draw(bonuswin)

    opt3text=Text(Point(225,150),'Prize 3')

    opt3text.setSize(12)

    opt3text.setStyle('bold')

    opt3text.setFill('black')

    opt3text.draw(bonuswin)

    # wait for click; when one of the prizes is clicked, randomly select a prize and display appropriate message

    bonusclick=bonuswin.getMouse()

    if 50 < bonusclick.getX() and bonusclick.getX() < 100 and 100 < bonusclick.getY() and bonusclick.getY() < 200:

        prize=prizes[random.randint(0,2)]

        if prize == -7:

            prizetext=Text(Point(150,270),'-7 to Score: Stinks!\nClick to continue...')

            prizetext.setSize(20)

            prizetext.setStyle('bold italic')

            prizetext.setFill('gold')

            prizetext.draw(bonuswin)

        elif prize == 0:

            prizetext=Text(Point(150,270),'0 to Score: OK!\nClick to continue...')

            prizetext.setSize(20)

            prizetext.setStyle('bold italic')

            prizetext.setFill('gold')

            prizetext.draw(bonuswin)

        elif prize == 7:

            prizetext=Text(Point(150,270),'7 to Score: Great!\nClick to continue...')

            prizetext.setSize(20)

            prizetext.setStyle('bold italic')

            prizetext.setFill('gold')

            prizetext.draw(bonuswin)

    elif 125 < bonusclick.getX() and bonusclick.getX() < 175 and 100 < bonusclick.getY() and bonusclick.getY() < 200:

        prize=prizes[random.randint(0,2)]

        if prize == -7:

            prizetext=Text(Point(150,270),'-7 to Score: Stinks!\nClick to continue...')

            prizetext.setSize(20)

            prizetext.setStyle('bold italic')

            prizetext.setFill('gold')

            prizetext.draw(bonuswin)

        elif prize == 0:

            prizetext=Text(Point(150,270),'0 to Score: OK!\nClick to continue...')

            prizetext.setSize(20)

            prizetext.setStyle('bold italic')

            prizetext.setFill('gold')

            prizetext.draw(bonuswin)

        elif prize == 7:

            prizetext=Text(Point(150,270),'7 to Score: Great!\nClick to continue...')

            prizetext.setSize(20)

            prizetext.setStyle('bold italic')

            prizetext.setFill('gold')

            prizetext.draw(bonuswin)

    elif 200 < bonusclick.getX() and bonusclick.getX() < 250 and 100 < bonusclick.getY() and bonusclick.getY() < 200:

        prize=prizes[random.randint(0,2)]

        if prize == -7:

            prizetext=Text(Point(150,270),'-7 to Score: Stinks!\nClick to continue...')

            prizetext.setSize(20)

            prizetext.setStyle('bold italic')

            prizetext.setFill('gold')

            prizetext.draw(bonuswin)

        elif prize == 0:

            prizetext=Text(Point(150,270),'0 to Score: OK!\nClick to continue...')

            prizetext.setSize(20)

            prizetext.setStyle('bold italic')

            prizetext.setFill('gold')

            prizetext.draw(bonuswin)

        elif prize == 7:

            prizetext=Text(Point(150,270),'7 to Score: Great!\nClick to continue...')

            prizetext.setSize(20)

            prizetext.setStyle('bold italic')

            prizetext.setFill('gold')

            prizetext.draw(bonuswin)

    # wait for click and close window; depending on prize, add value to score and return score

    bonusclick=bonuswin.getMouse()

    if prize == 0:

        bonuswin.close()

        return score

    elif prize == -7:

        bonuswin.close()

        score+=-7

        return score

    elif prize == 7:

        bonuswin.close()

        score+=7

        return score

# define scoreboard() function that makes scoreboard

def scoreboard(g,controlwin):

    # initialize data list and text object list

    data=[]

    scrolls=[]

    # create list of data

    file=open('scores.txt','r')

    filelist=file.readlines()

    for i in range(0,len(filelist)):

        fileitem=filelist[i].split(',')

        fileitem[2]=fileitem[2][0:len(fileitem[2])-1]

        data.append(fileitem)

    file.close()

    # create high score window and general count

    highwin=GraphWin('High Scores',300,300)

    g+=1

    # create header text and border

    hsheader=Text(Point(150,10),'{0:<}\t\t{1:^}\t\t{2:>}'.format('Player','Rounds','Score'))

    hsheader.setSize(14)

    hsheader.setStyle('bold')

    scrolls.append(hsheader)

    hsheader.draw(highwin)

    border=Text(Point(150,30),'--------------------------------------------------------------')

    border.setSize(14)

    border.setStyle('bold')

    scrolls.append(border)

    border.draw(highwin)

    # create score text

    for i in range(0,min(len(data),7)):

        place=Text(Point(150,50+(20*i)),'{0:<}\t\t\t{1:^}\t\t{2:>}'.format(data[i][0],data[i][1],data[i][2]))

        place.setSize(11)

        place.setStyle('bold')

        scrolls.append(place)

        place.draw(highwin)

    # return scroll option

    return 'scroll',highwin,scrolls,data,g

# define scroll() function that scrolls the scoreboard text

def scroll(highwin,scrolls,data):

    # scroll

    scrolls[0].move(0,-2.5)

    center=scrolls[0].getAnchor()

    # if center at border, redraw at bottom

    if center.getY() < 0:

        scrolls[0].undraw()

        scrolls[0]=Text(Point(150,300),'{0:<}\t\t{1:^}\t\t{2:>}'.format('Player','Rounds','Score'))

        scrolls[0].setSize(14)

        scrolls[0].setStyle('bold')

        scrolls[0].draw(highwin)

    scrolls[1].move(0,-2.5)

    center=scrolls[1].getAnchor()

    if center.getY() < 0:

        scrolls[1].undraw()

        scrolls[1]=Text(Point(150,300),'--------------------------------------------------------------')

        scrolls[1].setSize(14)

        scrolls[1].setStyle('bold')

        scrolls[1].draw(highwin)

    scrolls[2].move(0,-2.5)

    center=scrolls[2].getAnchor()

    if center.getY() < 0:

        scrolls[2].undraw()

        scrolls[2]=Text(Point(150,300),'{0:<}\t\t\t{1:^}\t\t{2:>}'.format(data[0][0],data[0][1],data[0][2]))

        scrolls[2].setSize(11)

        scrolls[2].setStyle('bold')

        scrolls[2].draw(highwin)

    scrolls[3].move(0,-2.5)

    center=scrolls[3].getAnchor()

    if center.getY() < 0:

        scrolls[3].undraw()

        scrolls[3]=Text(Point(150,300),'{0:<}\t\t\t{1:^}\t\t{2:>}'.format(data[1][0],data[1][1],data[1][2]))

        scrolls[3].setSize(11)

        scrolls[3].setStyle('bold')

        scrolls[3].draw(highwin)

    scrolls[4].move(0,-2.5)

    center=scrolls[4].getAnchor()

    if center.getY() < 0:

        scrolls[4].undraw()

        scrolls[4]=Text(Point(150,300),'{0:<}\t\t\t{1:^}\t\t{2:>}'.format(data[2][0],data[2][1],data[2][2]))

        scrolls[4].setSize(11)

        scrolls[4].setStyle('bold')

        scrolls[4].draw(highwin)

    scrolls[5].move(0,-2.5)

    center=scrolls[5].getAnchor()

    if center.getY() < 0:

        scrolls[5].undraw()

        scrolls[5]=Text(Point(150,300),'{0:<}\t\t\t{1:^}\t\t{2:>}'.format(data[3][0],data[3][1],data[3][2]))

        scrolls[5].setSize(11)

        scrolls[5].setStyle('bold')

        scrolls[5].draw(highwin)

    scrolls[6].move(0,-2.5)

    center=scrolls[6].getAnchor()

    if center.getY() < 0:

        scrolls[6].undraw()

        scrolls[6]=Text(Point(150,300),'{0:<}\t\t\t{1:^}\t\t{2:>}'.format(data[4][0],data[4][1],data[4][2]))

        scrolls[6].setSize(11)

        scrolls[6].setStyle('bold')

        scrolls[6].draw(highwin)

    scrolls[7].move(0,-2.5)

    center=scrolls[7].getAnchor()

    if center.getY() < 0:

        scrolls[7].undraw()

        scrolls[7]=Text(Point(150,300),'{0:<}\t\t\t{1:^}\t\t{2:>}'.format(data[5][0],data[5][1],data[5][2]))

        scrolls[7].setSize(11)

        scrolls[7].setStyle('bold')

        scrolls[7].draw(highwin)

    scrolls[8].move(0,-2.5)

    center=scrolls[8].getAnchor()

    if center.getY() < 0:

        scrolls[8].undraw()

        scrolls[8]=Text(Point(150,300),'{0:<}\t\t\t{1:^}\t\t{2:>}'.format(data[6][0],data[6][1],data[6][2]))

        scrolls[8].setSize(11)

        scrolls[8].setStyle('bold')

        scrolls[8].draw(highwin)

# define save() function that saves the game statistics

def save(name,score,k):

    # initialize placeholder lists

    data=[]

    highs=[]

    # add new score data to file

    file=open('scores.txt','a')

    file.write(name+','+str(k)+','+str(score)+'\n')

    file.close()

    # read file lines

    file=open('scores.txt','r')

    filelist=file.readlines()

    for i in range(0,len(filelist)):

        fileitem=filelist[i].split(',')

        fileitem[2]=fileitem[2][0:len(fileitem[2])-1]

        data.append(fileitem)

    file.close()

    # reorder scores and save to file

    file=open('scores.txt','w')

    for j in range(0,len(data)):

        highs.append(int(data[j][2]))

    while highs != []:

        r=highs.index(max(highs))

        file.write(data[r][0]+','+data[r][1]+','+data[r][2]+'\n')

        highs.remove(highs[r])

        data.remove(data[r])

    file.close()

# define hint() function that operates the hint mechanics

def hint(circlelist,bpolygonlist,wronglist,playword,alphabetlist,textlist,w):

    # initialize counter

    y=0

    # drop polygons, and hint costs 2 turns

    while y<2:

        drop(bpolygonlist[w])

        w+=1

        y+=1

    # initialize wrong letter count

    c=0

    while c<3:

        # eliminate 3 random wrong choices

        r=random.randint(0,25)

        if alphabetlist[r] not in playword and alphabetlist[r] not in wronglist:

            circlelist[r].setFill('gold')

            textlist[r].setFill('black')

            wronglist.append(alphabetlist[r])

            c+=1

    # reutrn guess counter and list of wrong letters

    return wronglist,w

# define click() function that determines click's distance to center of circle

def click(gameclick,circle):

            # get x and y coordinates of click

            gx=gameclick.getX()

            gy=gameclick.getY()

            # get center and radius of circle

            center=circle.getCenter()

            radius=circle.getRadius()

            # get x and y coordinate of circle center

            xc=center.getX()

            yc=center.getY()

            # calculate distance

            distance=math.sqrt(((gx-xc)**2)+((gy-yc)**2))

            # if click is within radius, return True

            if distance < radius:

                return True

            else:

                return False

# define control() that creates control panel

def control():

    # create control panel window

    controlwin=GraphWin('Welcome to:',300,300)

    controlwin.setBackground('light grey')

    # create title header

    topblack=Rectangle(Point(0,0),Point(300,30))

    topblack.setFill('black')

    topblack.draw(controlwin)

    header=Text(Point(150,15),'GUESS MASTER 3.0')

    header.setStyle('bold')

    header.setSize(20)

    header.setFill('gold')

    header.draw(controlwin)

    # create new game button

    newbutton=Rectangle(Point(30,60),Point(90,90))

    newbutton.setFill('gold')

    newbutton.draw(controlwin)

    newtext=Text(Point(60,75),'NEW')

    newtext.setStyle('bold')

    newtext.setSize(16)

    newtext.draw(controlwin)

    # create quit game button

    quitbutton=Rectangle(Point(210,60),Point(270,90))

    quitbutton.setFill('black')

    quitbutton.draw(controlwin)

    quittext=Text(Point(240,75),'QUIT')

    quittext.setStyle('bold')

    quittext.setSize(16)

    quittext.setFill('gold')

    quittext.draw(controlwin)

    # create description

    midwhite=Rectangle(Point(30,120),Point(270,210))

    midwhite.setFill('white')

    midwhite.draw(controlwin)

    descript=Text(Point(150,165),'This is a game where your score is\nbased on the number of 4-6 letter\nwords you can guess within 10 tries.')

    descript.setSize(14)

    descript.draw(controlwin)

    # prompt user to click new button to start game

    prompt=Text(Point(150,240),'Click NEW to start a game...')

    prompt.setSize(18)

    prompt.draw(controlwin)

    # make hint button

    hintbutton=Rectangle(Point(115,265),Point(185,285))

    hintbutton.setFill('light grey')

    hintbutton.draw(controlwin)

    # make hint text

    hinttext=Text(Point(150,275),'HINT?')

    hinttext.setStyle('bold')

    hinttext.setSize(14)

    hinttext.draw(controlwin)

    # create high scores button

    hsbutton=Rectangle(Point(100,95),Point(200,115))

    hsbutton.setFill('light grey')

    hsbutton.draw(controlwin)

    # create high scores text

    hstext=Text(Point(150,105),'HIGH SCORES')

    hstext.setStyle('bold')

    hstext.setSize(13)

    hstext.draw(controlwin)

    # return control panel window

    return controlwin,newbutton,quitbutton,hintbutton,hsbutton

# define game() that creates game panel

def game():

    # create game panel

    gamewin=GraphWin('Save the Block P',420,420)

    gamewin.setBackground('gold')

    # initialize graphics lists

    circlelist=[]

    textlist=[]

    wpolygonlist=[]

    bpolygonlist=[]

    rectanglelist=[]

    # create letter buttons

    alphabet='A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'

    alphabetlist=alphabet.split(',')

    for i in range(0,13):

        circle=Circle(Point((i+1)*30,350),15)

        circle.setFill('black')

        circle.draw(gamewin)

        circlelist.append(circle)

        lettertext=Text(Point((i+1)*30,350),alphabetlist[i])

        lettertext.setFill('white')

        lettertext.draw(gamewin)

        textlist.append(lettertext)

    for j in range(13,26):

        circle=Circle(Point((j+1-13)*30,380),15)

        circle.setFill('black')

        circle.draw(gamewin)

        circlelist.append(circle)

        lettertext=Text(Point((j+1-13)*30,380),alphabetlist[j])

        lettertext.setFill('white')

        lettertext.draw(gamewin)

        textlist.append(lettertext)

    # create white Block P polygons

    wpolygon=Polygon(Point(82.5,320),Point(152.5,320),Point(162.5,290),Point(92.5,290))

    wpolygon.setFill('white')

    wpolygon.draw(gamewin)

    wpolygonlist.append(wpolygon)

    for i in range(0,4):

        wpolygon=Polygon(Point(97.5+(15*i),290-(45*i)),Point(157.5+(15*i),290-(45*i)),Point(172.5+(15*i),245-(45*i)),Point(112.5+(15*i),245-(45*i)))

        wpolygon.setFill('white')

        wpolygon.draw(gamewin)

        wpolygonlist.append(wpolygon)

    for i in range(0,2):

        wpolygon=Polygon(Point(202.5+(60*i),155),Point(262.5+(60*i),155),Point(277.5+(60*i),110),Point(217.5+(60*i),110))

        wpolygon.setFill('white')

        wpolygon.draw(gamewin)

        wpolygonlist.append(wpolygon)

    for i in range(0,2):

        wpolygon=Polygon(Point(247.5-(15*i),200+(45*i)),Point(307.5-(15*i),200+(45*i)),Point(322.5-(15*i),155+(45*i)),Point(262.5-(15*i),155+(45*i)))

        wpolygon.setFill('white')

        wpolygon.draw(gamewin)

        wpolygonlist.append(wpolygon)

    wpolygon=Polygon(Point(172.5,245),Point(232.5,245),Point(247.5,200),Point(187.5,200))

    wpolygon.setFill('white')

    wpolygon.draw(gamewin)

    wpolygonlist.append(wpolygon)

    # create black Block P polygons

    bpolygon=Polygon(Point(82.5,320),Point(152.5,320),Point(162.5,290),Point(92.5,290))

    bpolygon.setFill('black')

    bpolygon.draw(gamewin)

    bpolygonlist.append(bpolygon)

    for i in range(0,4):

        bpolygon=Polygon(Point(97.5+(15*i),290-(45*i)),Point(157.5+(15*i),290-(45*i)),Point(172.5+(15*i),245-(45*i)),Point(112.5+(15*i),245-(45*i)))

        bpolygon.setFill('black')

        bpolygon.draw(gamewin)

        bpolygonlist.append(bpolygon)

    for i in range(0,2):

        bpolygon=Polygon(Point(202.5+(60*i),155),Point(262.5+(60*i),155),Point(277.5+(60*i),110),Point(217.5+(60*i),110))

        bpolygon.setFill('black')

        bpolygon.draw(gamewin)

        bpolygonlist.append(bpolygon)

    for i in range(0,2):

        bpolygon=Polygon(Point(247.5-(15*i),200+(45*i)),Point(307.5-(15*i),200+(45*i)),Point(322.5-(15*i),155+(45*i)),Point(262.5-(15*i),155+(45*i)))

        bpolygon.setFill('black')

        bpolygon.draw(gamewin)

        bpolygonlist.append(bpolygon)

    bpolygon=Polygon(Point(172.5,245),Point(232.5,245),Point(247.5,200),Point(187.5,200))

    bpolygon.setFill('black')

    bpolygon.draw(gamewin)

    bpolygonlist.append(bpolygon)

    # create streak bar and text

    streakbar=Rectangle(Point(20,130),Point(50,290))

    streakbar.setFill('black')

    streakbar.draw(gamewin)

    streaktext=Text(Point(35,305),'STREAK')

    streaktext.setSize(14)

    streaktext.setStyle('bold italic')

    streaktext.draw(gamewin)

    # select random word

    file=open('words.txt','r')

    wordlist=file.readlines()

    file.close()

    x=random.randint(0,len(wordlist))

    playword=wordlist[x]

    playword=playword[0:len(playword)-1]

    # create yellow word boxes

    n=len(playword)

    m=0

    for i in range(0,n):

        if n == 4:

            m=90

        elif n == 5:

            m=60

        else:

            m=30

        wordsquare=Rectangle(Point(m+(60*i),100),Point(m+60+(60*i),40))

        wordsquare.setFill('gold')

        wordsquare.draw(gamewin)

        rectanglelist.append(wordsquare)
    
    # return game panel window and game word

    return gamewin,circlelist,textlist,wpolygonlist,bpolygonlist,rectanglelist,playword,alphabetlist

# define drop() function that animates polygon falling

def drop(polygon):

    # set fill of polygon to red

    polygon.setFill('red')

    # move red polygon outside of window

    for i in range(0,10):

        polygon.move(0,i*10)

# call main() function

main()

