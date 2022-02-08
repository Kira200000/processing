def setup():
    size(600,400)
    frameRate(15)
    background(0)
def draw():
    strokeWeight(random(1,10))
    stroke(random(90,255),random(90,255),random(90,255))
    point(random(0,600),random(0,400))
def mouseClicked():
    background(0)
    
