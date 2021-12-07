x = 0
def setup():
    size(600,600)
    rectMode(CENTER)
def draw():
    global x
    background(200)
    translate(300,200)
    rotate(radians(225))
    ellipse(45,0, 90,90)
    ellipse(0,45,90,90)
    rect(0,0, 90,90)
    x = x + 1
