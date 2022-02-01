x = 0 
mode = "вправо"
def setup():
    size(600,400)
    frameRate(15)
def draw():
    global x, mode

    fill(x)
    
    rect(200,100, x,x)
    if mode == "вправо":
        x = x + 20
    if mode == "влево":
        x = x - 20
    if x >= 250:
       mode = "влево"
    if x <= 0:
       mode = "вправо"
