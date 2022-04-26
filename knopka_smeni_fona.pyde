x = 0
def setup():
    size(600,400)
    
def draw():
    global x
    background(x)
    fill(255)
    rect(200,100,200,100)
def mouseClicked():
    global x
    if mouseX > 200 and mouseX < 300 and mouseY > 100 and mouseY < 200:
        x = 200
