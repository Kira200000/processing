razmer = 0
x1 = 250 
y1 = 250
x2 = 250
y2 = 250
x3 = 250
y3 = 250
x4 = 250
y4 = 250
def setup():
    size(500,500)
def draw():
    #background (200)
    global x1,x2,x3,x4
    global y1,y2,y3,y4
    fill(random(255),random(255),random(255),random(255))
    stroke(random(255),random(255),random(255),random(255))
    #strokeWeight(random(50))
    razmer = random(5,50)
    ellipse(x1,y1,razmer,razmer)
    ellipse(x2,y2,razmer,razmer)
    ellipse(x3,y3,razmer,razmer)
    ellipse(x4,y4,razmer,razmer)
    x1 = x1 + 1
    y1 = y1 + 1
    x2 = x2 - 1
    y2 = y2 + 1
    x3 = x3 + 1
    y3 = y3 - 1
    x4 = x4 - 1
    y4 = y4 - 1
