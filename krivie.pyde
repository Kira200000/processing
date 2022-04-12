bg = 0;

def setup():
    size(600,400)
def draw():
    global bg
    background(bg)
    fill(255)
    rect(250,150,100,50) 
    ellipse(400,350,70,70)
def mouseClicked():
    global bg
    if mouseX > 250 and mouseX < 350 and mouseY > 150 and mouseY < 200:
        bg = 255
