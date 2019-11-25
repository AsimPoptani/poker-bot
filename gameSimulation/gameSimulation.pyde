import random
GAME_WIDTH=800
GAME_HEIGHT=515

def setup():
    size(800,515)
    
class GameItem:
    def __init__ (self,x,y,radius,xVelocity,yVelocity):
        print(x,y,radius,xVelocity,yVelocity)
        # Do some checking to see if x and y are within bounds we also need to add the radius
        if x>GAME_WIDTH or x<0:
            raise ValueError("Not in range")
        if y>GAME_HEIGHT or y<0:
            raise ValueError("Not in range")
        self.x=x
        self.y=y
        self.radius=radius
        self.xVelocity=xVelocity
        self.yVelocity=yVelocity
    
    def checkIfCollide(self,GameItem):
        pass
    
    def draw(self):
        circle(self.x,self.y,self.radius)
    
    def addVelocity(self, xVelocity,yVelocity):
        pass
    
    def update(self):
        if ((self.x+self.radius)>=GAME_WIDTH and self.xVelocity>0) or ((self.x-self.radius)<=0 and self.xVelocity<0):
            self.inverseXVelocity()
        if ((self.y+self.radius)>=GAME_HEIGHT and self.yVelocity>0) or ((self.y-self.radius)<=0 and self.yVelocity<0):
            self.inverseYVelocity()
        self.x=self.x+self.xVelocity
        self.y=self.y+self.yVelocity
        print(self.x,self.y)
    
    def inverseXVelocity(self):
        self.xVelocity=-self.xVelocity
        
    def inverseYVelocity(self):
        self.yVelocity=-self.yVelocity
balls=[]
for index in range(10):
    radius=random.randint(1,100)
    balls.append(GameItem(random.randint(0,GAME_WIDTH-radius),random.randint(0,GAME_HEIGHT-radius),radius,random.randint(0,10),random.randint(0,10)))
def draw():
    clear()
    for ball in balls:
        ball.draw()
        ball.update()
