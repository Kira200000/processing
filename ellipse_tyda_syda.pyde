x = 0
mode = "вправо"
def setup():
    size(600,400)
    #frameRate(3)
def draw():
    global x,mode
    background(200)
    ellipse(x,0, 40,40)
    if mode == "вправо":
        x = x + 20
    if mode == "влево":
        x = x - 20
    if x >= 600:
       mode = "влево"
    if x <= 0:
       mode = "вправо"
