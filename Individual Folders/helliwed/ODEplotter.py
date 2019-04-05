from graphics import *

# Here we invite the user to specify coordinates
# todo
#   figure out whether this is the best way to make these global

#a = int(input('minimum x value?  '))
#b = int(input('maximum x value?  '))
#c = int(input('minimum y value?  '))
#d = int(input('maximum y value?  '))

a = -10
b = 10
c = -10
d = 10

# This is where the vector field is defined.
# todo
#   Make it so the user can enter the formulas  

def V(x,y):
    vectorfield = [0,0]
    vectorfield[0] = -y
    vectorfield[1] = x
    return vectorfield

# This allows us to work with points in the window using mathematician's convention
# It assumes the window will be at least 600 x 600 (or so).
# The origin is NEAR the lower left corner.

def pt(x,y):
    pythonx = x + 50
    pythony = 550 - y
    return Point(pythonx, pythony)

# This allows us to express points in terms of the user's coordinates

def userpt(x,y):
    mathx = (500/(b-a))*(x-a)
    mathy = (500/(d-c))*(y-c)
    return pt(mathx,mathy)


def main():

    # build our window

    win = GraphWin("Vector Field Plot", 800, 600)
    win.setBackground(color_rgb(0,0,0))

    # make and draw the coordinate axes

    xaxisline = Line(userpt(a,0), userpt(b,0))
    xaxisline.setFill(color_rgb(0, 255, 0))
    xaxisline.setWidth(2)
    xaxisline.draw(win)

    yaxisline = Line(userpt(0,c), userpt(0,d))
    yaxisline.setFill(color_rgb(0, 255, 0))
    yaxisline.setWidth(2)
    yaxisline.draw(win)

    # flowline = Line(userpt(a,.414*a), userpt(b,.414*b))
    # flowline.setFill(color_rgb(255, 0, 0))
    # flowline.setWidth(2)
    # flowline.draw(win)

    # flow2line = Line(userpt(a,-.414*a), userpt(b,-.414*b))
    # flow2line.setFill(color_rgb(255, 0, 0))
    # flow2line.setWidth(2)
    # flow2line.draw(win)

    # flow3line = Line(userpt(.414*c,c), userpt(.414*d,d))
    # flow3line.setFill(color_rgb(255, 0, 0))
    # flow3line.setWidth(2)
    # flow3line.draw(win)

    # flow4line = Line(userpt(-.414*c,c), userpt(-.414*d,d))
    # flow4line.setFill(color_rgb(255, 0, 0))
    # flow4line.setWidth(2)
    # flow4line.draw(win)

    # set some parameters for the vector field

    vls = .1       # vector length scale
    vgap = 2       # gap between drawn vectors

    #style = int(input('vector style? (0 for plain, 1 for thick segment, 2 for arrow)  '))
    style = 0

    # the following loops generate the vector field.
    # todo:
    #   make better use of basept and headpt (don't know how to do efficient vector computation)
    #   figure out triangle head coordinates

    for i in range(int((b-a)/vgap)+1):
        for j in range(int((d-c)/vgap)+1):
            basept = userpt(a + vgap*i,c + vgap*j)
            headpt = userpt(a + vgap*i+vls*V(a + vgap*i,c + vgap*j)[0],
                            c + vgap*j+vls*V(a + vgap*i,c + vgap*j)[1])
            vectorseg = Line(basept,headpt)
            vectorseg.setFill(color_rgb(0, 255, 255))
            if style == 1:
                vectorstyle = Line(basept,
                        userpt(a + vgap*i+vls*V(a + vgap*i,c + vgap*j)[0]/2,
                            c + vgap*j+vls*V(a + vgap*i,c + vgap*j)[1]/2))
                vectorstyle.setWidth(3)
                vectorstyle.setFill(color_rgb(0, 255, 255))
            # if style == 2:
            #     vectorstyle = Polygon(userpt(vgap*i+vls*V(vgap*i,vgap*j)[0],
            #                 vgap*j+vls*V(vgap*i,vgap*j)[1]),
            #                     pt())
            vectorseg.draw(win)
            if style > 0:
                vectorstyle.draw(win)
    
    # Use Euler's method to approximate solutions

    again = 1

    while again == 1:

        # user specifies initial point

        startx = float(input('x coordinate of initial point?  '))
        starty = float(input('y coordinate of initial point?  '))
        newpoint = [startx, starty]
        
        # user specifies step scale
        
        h = float(input('step scale? (.01 is good)  '))

        # plot the point.  Then update the point

        for k in range(1000):
            plotpt = userpt(newpoint[0],newpoint[1])
            plotpt.setFill(color_rgb(255, 255, 0))
            plotpt.draw(win)
            newpoint = [newpoint[0]+h*V(newpoint[0],newpoint[1])[0],
                            newpoint[1]+h*V(newpoint[0],newpoint[1])[1]]
        
        again = int(input('again?  (1 for yes)  '))

    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()