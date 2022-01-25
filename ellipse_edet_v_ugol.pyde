x = 0
def setup():
    size(600,600)
    #frameRate(3)
def draw():
    global x
    background(200)
    ellipse(x,x, 40,40)
    x = x + 5
    if x >= 600-10:
        x = 0
