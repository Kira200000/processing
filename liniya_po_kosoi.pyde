x = 300
def setup():
    size(600,600)
def draw():
    global x
    background(200)
    stroke(random(100,255))
    strokeWeight(10)
    line(x,x, x,x)
    x = x + 1
