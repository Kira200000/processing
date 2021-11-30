x = 0
def setup():
    size(600,600)
    frameRate(20)
    colorMode(HSB)
def draw():
    global x
    background(200)
    fill(x)
    ellipse(300,300, 30,30)
    x = x + 1
