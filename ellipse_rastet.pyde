x = 0 
def setup():
    size(600,400)
    frameRate(10)
def draw():
    global x
    background(200)
    translate(300,200)
    ellipse(0,0, x,x)
    x = x - 3
    
