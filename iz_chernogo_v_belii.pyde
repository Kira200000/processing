x = 0 
def setup():
    size(600,400)
    frameRate(40)
def draw():
    global x
    background(200)
    fill(x)
    ellipse(300,200, 100,100)
    x = x + 3
    if x >= 250-0:
        x = 0
