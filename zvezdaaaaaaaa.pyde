def setup():
    size(600,600)
    background(200)
def draw():
    push()
    stroke(255)
    translate(0,-100)
    triangle(300,200, 250,300, 350,300)
    triangle(450,350, 350,300, 350,400)
    triangle(350,400, 250,400, 300,500)
    triangle(250,400, 250,300, 150,350)
    pop()
    stroke(255)
    ellipse(300,250, 140,140)
    
