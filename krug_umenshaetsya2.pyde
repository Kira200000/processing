x = -700
def setup():
    size(600,600)
    frameRate(20)
def draw():
    global x 
    background(255)
    fill(random(100,255))
    ellipse(300,300, x,x)
    x = x + 10
