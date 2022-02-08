x = 900 
def setup():
    size(600,400)
    frameRate(40)
def draw():
    global x
    background(200)
    translate(300,200)
    ellipse(0,0, x,x)
    x = x - 3
def mouseClicked():
    global x
    x = 900
    
