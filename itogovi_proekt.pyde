x = 0
def setup():
    size(600,400)
    background(200)
def draw():
    #keyPressed key 
    if keyPressed:
        if key == "1":
            push()
            fill(255, 140, 0)
            ellipse(250,200, 110,100)
            ellipse(350,200, 110,100)
            ellipse(300,200, 100,100)
            pop()
            push()
            fill(34, 139, 34)
            triangle(300,150, 290,140, 310,140)
            pop()
            ellipse(280,185, 20,20)
            ellipse(320,185,20,20)
            triangle(300,210, 290,200, 310,200)
            line(290,170, 280,160)
            line(310,170, 320,160)
        elif key == "2":
            background(200) 
            push()
            fill(255, 228, 181)
            ellipse(350,300, 30,30)
            ellipse(250,300, 30,30)
            ellipse(300,300, 100,100)
            pop()
            ellipse(280,290, 20,20)
            ellipse(320,290, 20,20)
            line(290,280, 270,270)
            line(330,270, 310,280)
            line(280,310, 320,320)
        elif key == "3":
            background(200)
            size(600,400)
            push()
            fill(255, 222, 173)
            rect(285,240, 30,50)
            ellipse(300,200, 100,100)
            rect(250,270, 100,150)
            stroke(255, 222, 173)
            strokeWeight(5)
            line(250,270, 190,280)
            line(190,280, 130,350)
            line(350,270, 410,280)
            line(410,280, 470,350)
            pop()
            ellipse(280,190, 20,20)
            ellipse(320,190, 20,20)
            line(290,180, 265,170)
            line(330,180, 315,170)
            line(270,230, 330,230)
         
    else:
        background(200)
