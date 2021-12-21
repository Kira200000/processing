angle = 0
def setup():
    size(600,600)
def draw():
    global angle
    ellipse(340,450, 45,45)   #нога правая
    ellipse(260,150, 35,35)   #ухо левое
    ellipse(340,150, 35,35)   #ухо правое
    ellipse(260,450, 35,35)   #нога левая
    ellipse(300,350, 150,200) #туловище
    ellipse(300,200, 100,100) #голова
    ellipse(300,350, 60,100)  #туловище2
    ellipse(300,200, 10,10)   #нос
    ellipse(280,180, 15,15)   #глаз левый
    ellipse(320,180, 15,15)   #глаз правый
    push()
    translate(230,310)

    rotate(radians(45))
    ellipse(0,0, 70,30)
    pop()
    translate(380,310)
    rotate(radians(140))
    ellipse(0,0, 70,30)


    
    
    angle = angle + 1
    
    
