x = 0
def setup(): 
    size(600,600)
    
def draw():
    global x
    push()
    fill(x)
    rect(50,500, 50,50) #кнопка цвета
    pop()
    rect(150,500, 50,50) #кнопка размера
    push()
    strokeWeight(20)
    line(mouseX,mouseY,pmouseX,pmouseY)
    pop()
def mouseClicked():
    global x
    background(200)
    if mouseX > 50 and mouseX < 100 and mouseY > 500 and mouseY < 550:
        x = 255
