x = 0
def setup():
    size(600,400)
    background(200)
def draw():
    if mousePressed:
        if mouseButton == LEFT:
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
        elif mouseButton == RIGHT:
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
    else:
         background(200)
