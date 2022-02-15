def setup():
    size(600,400)
    background(100)
def draw():
    if mousePressed and (mouseButton == LEFT):
        fill(255,0,0)
    elif mousePressed and (mouseButton == RIGHT):
          fill(0,255,0)
    elif mousePressed and (mouseButton == CENTER):
          fill(0,0,255)
    else:
        fill(0)
    ellipse(300,200, 50,50)
