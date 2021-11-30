x = 0
def setup():
    size(600,600)
    frameRate(10)
def draw():
    global x
    background(200)
    fill(x)
    triangle(300,x, x,400, 400,400)
    x = x + 1
