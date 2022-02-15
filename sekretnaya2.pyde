x = 0
def setup():
    size(600,400)
    #frameRate(40)
def draw():
    global x
    
    if mousePressed == True:
        x = x + 3
        if x >= 200-0:
            x = 0
        fill(x)
        stroke(x) 
    else: 
        background(200)
        fill(200)
        stroke(200)
    ellipse(300,200, x,x)
