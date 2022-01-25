x = 0 
def setup():
    size(600,400)
    #frameRate(40)
def draw():
    global x
    background(200)
    fill(x)
    stroke(x)
    ellipse(300,200, x,x)
    x = x + 3
    if x >= 200-0:
        x = 0
