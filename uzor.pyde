x = 0
y = 0
def setup():
    size(700,700)
    rectMode(CENTER)
def draw():
   global x,y
   translate(width/2, height/2)
   rotate(x)
   square(0,0, y) 
   x = x + 1
   y = y + 1
