def setup():
    size(600,600)
    frameRate(5)
    background(0)
    rect(230,150, 150,250)
    rect(290,400,30,200)
    stroke(178, 34, 34)
    fill(178, 34, 34)
    ellipse(300,200, 50,50)
    fill(100)
    stroke(100)
    ellipse(300,270, 50,50)
    ellipse(300,340, 50,50)
    stroke(178, 34, 34)
def draw():
    line(300,200, random(10,500),random(100,500))
    
    
    
