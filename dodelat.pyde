x = 0
def setup():
    size(600,400)
def draw():
    if mousePressed:
        if mouseButton == LEFT:
          ellipse(250,200, 110,100)
          ellipse(350,200, 110,100)
          ellipse(300,200, 100,100)
          triangle(300,150, 290,140, 310,140)
          ellipse(280,185, 20,20)
          ellipse(320,185,20,20)
          triangle(300,210, 290,200, 310,200)
          line(290,170, 280,160)
          line(310,170, 320,160)
        elif mouseButton == RIGHT:
          background(200)
          size(600,600)
          ellipse(300,300, 100,100)
          ellipse(280,290, 20,20)
          ellipse(320,290, 20,20)
          line(290,280, 270,270)
    else:
        background(200)
