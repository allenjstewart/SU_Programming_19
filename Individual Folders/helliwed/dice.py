#an attempt at making some dice that look nice and work

from random import *
from graphics import *

def pipbuild(a,b):
    pipcirc = Circle(Point(a,b),7)
    pipcirc.setFill(color_rgb(0,0,0))
    return(pipcirc)


def main():
    #again = 1
    #while (again == 1):
        win = GraphWin("dice", 380, 230)
        win.setBackground(color_rgb(40,255,150))
        dicerolls = [randint(1,6),randint(1,6)]
        dicecorners = [[50,70],[220,70]]
        dice = [Rectangle(Point(dicecorners[0][0],dicecorners[0][1]),
                        Point(dicecorners[0][0]+80,dicecorners[0][1]+80)),
                Rectangle(Point(dicecorners[1][0],dicecorners[1][1]),
                        Point(dicecorners[1][0]+80,dicecorners[1][1]+80))]
        dice[0].setFill(color_rgb(255,255,255))
        dice[1].setFill(color_rgb(200,0,0))
        for i in range(2):
                dice[i].setWidth(5)
                dice[i].draw(win)
                if (dicerolls[i]%2 == 1):
                        pip = pipbuild(dicecorners[i][0]+40,dicecorners[i][1]+40)
                        pip.draw(win)
                if (dicerolls[i] > 1):
                        pip = pipbuild(dicecorners[i][0]+60,dicecorners[i][1]+20)
                        pip.draw(win)
                        pip = pipbuild(dicecorners[i][0]+20,dicecorners[i][1]+60)
                        pip.draw(win)
                if (dicerolls[i] > 3):
                        pip = pipbuild(dicecorners[i][0]+20,dicecorners[i][1]+20)
                        pip.draw(win)
                        pip = pipbuild(dicecorners[i][0]+60,dicecorners[i][1]+60)
                        pip.draw(win)
                if (dicerolls[i] == 6):
                        pip = pipbuild(dicecorners[i][0]+20,dicecorners[i][1]+40)
                        pip.draw(win)
                        pip = pipbuild(dicecorners[i][0]+60,dicecorners[i][1]+40)
                        pip.draw(win)
        # seconddie = Rectangle(Point(170,200),Point(270,300))
        # seconddie.setFill(color_rgb(255,255,255))
        # seconddie.setWidth(0)
        #seconddie.setOutline(color_rgb(200,200,200))
        #seconddie.draw(win)

        win.getMouse() # Pause to view result
        win.close()    # Close window when done
        #again = int(input("again? \n"))

        #print(dicerolls)

main()