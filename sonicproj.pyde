add_library('minim')
import os 
import time 
import random
path=os.getcwd() 
player=Minim(this) 

class Game:
    def __init__(self):
        self.w=1024
        self.h=768
        self.g=600
        self.paused=False 
        self.state= 'menu'
        self.score=0
        self.x=0
        self.name= ' ' 
        self.p=2
        
    #creating the game
    def CreateGame(self):
        self.cnt=0 
        self.time=0
        self.y=0
        self.enemies=[]
        self.coins=[]
        self.obstacles=[]
        self.crates=[]
        self.platforms=[]
        
        #looking for highscores 
        r=open("highscores.csv","r")
        array = []
        for line in r:
            line = line.rstrip('\n')
            line = line.split(',')
            line[1] = int(line[1])
            array.append( line )
        r.close()
        
        array.sort(key=lambda x:x[1])
        array.reverse()
        self.best = array[0][1]
                
        #loading the sky,tree and ground images 
        self.b1=loadImage("sky.png") 
        self.b2=loadImage("trees.png")
        self.b4=loadImage("ground.png") 


        #background music
        self.bgMusic=player.loadFile(path+"/backgroundmusic.mp3")
        self.bgMusic.play()
        self.bgMusic.rewind() 
        
        #loading the other sounds 
        self.gameoversound=player.loadFile(path+"/Gameover.mp3")
        self.click=player.loadFile(path+"/Mouseclick.mp3")
        self.coin=player.loadFile(path+"/coin.wav")
        self.win=player.loadFile(path+"/win.mp3")  
         
         
        #displaying the crates at different locations  
        for i in range(1):
            self.crates.append(Crates(200,550,60,70,"crates.png"))
            self.crates.append(Crates(595,550,60,70,"crates.png"))
            self.crates.append(Crates(1000,550,60,70,"crates.png"))
            self.crates.append(Crates(1400,550,60,70,"crates.png"))
            self.crates.append(Crates(1800,550,60,70,"crates.png"))    
            self.crates.append(Crates(2000,550,60,70,"crates.png")) 
            self.crates.append(Crates(2400,550,60,70,"crates.png"))
            self.crates.append(Crates(2800,550,60,70,"crates.png"))
            
        #randomly generating locations for the crates from 3000-8000 pixels 
        for i in range(10):
            self.crates.append(Crates(random.randint(3000,8000),550,60,70,"crates.png"))
            
        #placing the platforms at different locations 
        for i in range(3):
            self.platforms.append(Platforms(250+i*300, 500-i*150, 200, 20, "platforms.png"))        
            self.platforms.append(Platforms(1500+i*300, 500-i*150, 200, 20, "platforms.png"))
            self.platforms.append(Platforms(3000+i*300, 500-i*150, 200, 20, "platforms.png"))        
            self.platforms.append(Platforms(4000+i*300, 500-i*150, 200, 20, "platforms.png"))
            self.platforms.append(Platforms(5000+i*300, 500-i*150, 200, 20, "platforms.png"))
            self.platforms.append(Platforms(6000+i*300, 500-i*150, 200, 20, "platforms.png"))
            self.platforms.append(Platforms(7500+i*300, 500-i*150, 200, 20, "platforms.png"))
            #self.platforms.append(Platforms(6000+i*300, 500-i*150, 200, 20, "platforms.png"))
            #self.platforms.append(Platforms(7000+i*300, 500-i*150, 200, 20, "platforms.png"))

        #placing the obstacles on the ground at different locations
        for i in range(1):
            self.obstacles.append(Obstacles(500,625,87,625,"obstacles.png",1))
            self.obstacles.append(Obstacles(800,625,87,625,"obstacles.png",1)) 
            self.obstacles.append(Obstacles(1600,625,87,625,"obstacles.png",1))
            self.obstacles.append(Obstacles(2000,625,87,625,"obstacles.png",1))
            self.obstacles.append(Obstacles(2500,625,87,625,"obstacles.png",1))
            self.obstacles.append(Obstacles(3000,625,87,625,"obstacles.png",1))
            self.obstacles.append(Obstacles(3500,625,87,625,"obstacles.png",1))
            self.obstacles.append(Obstacles(4000,625,87,625,"obstacles.png",1))
            self.obstacles.append(Obstacles(5000,625,87,625,"obstacles.png",1))
            self.obstacles.append(Obstacles(6000,625,87,625,"obstacles.png",1))
            self.obstacles.append(Obstacles(8500,625,87,625,"obstacles.png",1))

        #this is the default player 
        if self.p==2:
            self.player=Sonic(50,50,28,625,"sonicrunning.png",12,92, 56)
            
        #generating the coins at different locations 
        for i in range(10):
            self.coins.append(Coin(random.randint(100,1000),570,12,625,"coins.png",10))
            self.coins.append(Coin(random.randint(1000,2000),570,12,625,"coins.png",10))
            self.coins.append(Coin(random.randint(2500,3000),570,12,625,"coins.png",10))
            self.coins.append(Coin(random.randint(3500,5000),570,12,625,"coins.png",10))
            self.coins.append(Coin(random.randint(6000,8500),570,12,625,"coins.png",10))

        #generating the enemies 
        for i in range(3):
            self.enemies.append(Enemy(200+i*300,500-i*150,20,625,"Enemy.png",3))
            self.enemies.append(Enemy(1000+i*300,500-i*150,20,625,"Enemy.png",3))
        for i in range(2):
            self.enemies.append(Enemy(1700+i*300,500-i*150,20,625,"Enemy.png",3))    
        for i in range(4):
            self.enemies.append(Enemy(random.randint(1900,4000),570,20,625,"Enemy.png",3))
            self.enemies.append(Enemy(random.randint(4500,6000),570,20,625,"Enemy.png",3))
        for i in range(3):
            self.enemies.append(Enemy(random.randint(6500,8000),570,20,625,"Enemy.png",3))
            
        #creating the treasure that is to be found                                                             
        self.treasure = Coin(9000,625,128,625,"Treasure.png",1)                                                                                                                                                                           
                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                                                                        
    def display(self):
        #time and score
        self.cnt= (self.cnt+1)%60
        if self.cnt==0:
            self.time += 1
            self.score += 1
            
        #background image
        image(self.b1,0,0,self.w-self.x%self.w,self.h,self.x%self.w,0,self.w,self.h)
        image(self.b1,self.w-self.x%self.w,0,self.x%self.w,self.h,0,0,self.x%self.w,self.h)
        
        #displaying the trees
        image(self.b2,0,0,self.w-self.x//3%self.w,self.h,self.x//3%self.w,0,self.w,self.h)
        image(self.b2,self.w-self.x//3%self.w,0,self.x//3%self.w,self.h,0,0,self.x//3%self.w,self.h)
                      
        #displaying the ground 
        image(self.b4,0,0,self.w-self.x//4%self.w,self.h,self.x//4%self.w,0,self.w,self.h)
        image(self.b4,self.w-self.x//4%self.w,0,self.x//4%self.w,self.h,0,0,self.x//4%self.w,self.h)
            
        #displaying the score and time
        fill(0,150,255)
        textSize(30)
        text('Score: '+str(self.score), 10, 25)
        text ('Time: '+str(self.time), 10,55)
        
        #displaying the treasure 
        
        self.treasure.display() 
        
        #displaying the coins 
        for c in self.coins:
            c.display() 
            
            
        #displaying the enemies 
        for e in self.enemies:
            e.display() 
            
        #displaying the player 
        
        self.player.display()
        
        #displaying platforms 
        for p in self.platforms:
            p.display() 
            
        #displaying the obstacles 
        for o in self.obstacles:
            o.display() 
    
        #displaying the crates 
        for c in self.crates:
            c.display() 
    
class Creature:
    def __init__(self,x,y,r,g,imgName,F):
        self.x=x
        self.y=y
        self.r=r
        self.w=self.r*2
        self.h=self.r*2 
        self.g=g
        self.F=F
        self.f=0
        self.vx=0
        self.vy=0
        self.dir=1
        self.img=loadImage(imgName)
        self.jump=0  

    #adjusting the gravity
    def gravity(self): #velocity incraments y 
        if self.y+self.r < self.g: #if the lower part of the circle is above the ground
            self.vy+=0.4 # my velocity in the y accelerates 
            if self.y+self.r+self.vy > self.g: # if i add the velocity and it makes me go below the ground, then make it the small set between the circle and the ground
                self.vy = self.g-(self.y+self.r)
        else:
            self.vy= 0
            self.jump=0  

        #adjusting sonic on the platforms 
        for p in game.platforms:
            if self.y+self.r <= p.y+game.y and self.x+self.r >= p.x and self.x-self.r <= p.x+p.w:
               self.g= p.y+game.y
               break 
            else:
                self.g = 625
                
        #adjusting sonic on the crates 
            for c in game.crates:
                if self.y+self.r <= c.y+game.y and self.x+self.r >= c.x and self.x-self.r <= c.x+c.w:
                    self.g= c.y+game.y
                    break 
                else:
                    self.g=625
        
    def update(self): #the update will call the gravity , to check for velocity in y direction 
        self.gravity() 
        
        self.x+=self.vx
        self.y+=self.vy 
        
    def display(self):
        self.update() #the display calls the update     
        #changes frames as direction of player changes 
        if self.dir > 0:
            image(self.img,self.x-self.w//2-game.x,self.y-self.h//2,self.w,self.h,int(self.f)*self.w,0,(int(self.f)+1)*self.w,self.h)
        elif self.dir < 0:
            image(self.img,self.x-self.w//2-game.x,self.y-self.h//2,self.w,self.h,int(self.f+1)*self.w,0,int(self.f)*self.w,self.h)    
        if self.vx != 0:
            self.f = (self.f+0.4)%self.F
        
    
        #stroke(255)
        #noFill() 
        #ellipse(self.x,self.y,2*self.r,2*self.r)
        #stroke(0,255,0) 
        #line(self.x-self.r,self.g,self.x+self.r,self.g) 

class Sonic(Creature):
    def __init__(self,x,y,r,g,img,F,w,h):
        Creature.__init__(self,x,y,r,g,img,F) 
        self.keyHandler = {LEFT:False, RIGHT:False, UP:False}
        self.killsound=player.loadFile(path+"/kill.wav")
        self.w = w # sonic image sprites are 92 pixels wide, which is differennt from 2*self.r
        self.h = h
        # Sonic's sprite frame is 92 pixels wide, amyrose's sprite frame is 130 pixels wide
        self.jump=0 
        
    def update(self):
        self.gravity()
        
        if self.keyHandler[LEFT]:
             self.vx = -5
             self.dir = -1
       
        elif self.keyHandler[RIGHT]:
             self.vx = 5
             self.dir = 1
        
        else:
             self.vx = 0
        
       #created double jump      
        if self.keyHandler[UP] and self.jump <2 and self.vy>=0:
            self.vy = -12
            self.jump+=1
            
            
        #self.y+self.r == self.g:
        #if keyPressed and key == ' ':
        
        self.x += self.vx #same as creature
        self.y += self.vy #same as creature 

        if self.x >= game.w//2:
            game.x += self.vx
        
        #coin collecting                     
        for c in game.coins:
            if self.distance(c) <= self.r+c.r:
                game.coin.rewind()
                game.coin.play()
                game.coins.remove(c)
                del c 
                # if not game.coin.isPlaying():
                #     game.coin.play() 
                # game.score += 10
                
        #finding the treasure and winning the game 
        if self.distance(game.treasure)<=self.r+game.treasure.r:
            game.score+=3000
            game.bgMusic.pause() 
            game.win.play()
            game.state='win'
            
        #enemy collision 
        for e in game.enemies:
            if self.distance(e) <= self.r+e.r:
                game.gameoversound.play()
                game.bgMusic.pause()
                time.sleep(2)
                game.state='enterName' 
                
        #obstacle collision
        for o in game.obstacles:
            if self.distance(o)<=self.r+o.r:
                game.gameoversound.play() 
                game.bgMusic.pause()
                time.sleep(2) 
                game.state='enterName' 
        
    
    def distance(self,other):
        return ((self.x-other.x)**2 + (self.y-other.y)**2)**0.5


class Coin(Creature):
    def __init__(self,x,y,r,g,imgName,F):
        Creature.__init__(self,x,y,r,g,imgName,F)
        self.vx=0.5
        
    def update(self):
        pass 

class Obstacles(Creature):
    def __init__(self,x,y,r,g,imgName,F):
        Creature.__init__(self,x,y,r,g,imgName,F)
    
    def update(self):
        pass

class Enemy(Creature):
    def __init__(self,x,y,r,g,imgName,F):
        Creature.__init__(self,x,y,r,g,imgName,F)
        self.vx = 1
        self.x1=self.x-100
        self.x2=self.x+100
        
    def update(self):
        self.gravity()
         
        if self.x < self.x1:
            self.vx = 1
            self.dir = 1
        elif self.x > self.x2:
            self.vx=-1
            self.dir=-1

        self.x+=self.vx
        self.y+=self.vy

class Platforms:
    def __init__(self,x,y,w,h,img):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.vx = 1
        self.vy=0
        
        self.x1=self.x-150
        self.x2=self.x+150
        self.img=loadImage("platforms.png")
        
    def display(self):
        image(self.img,self.x-game.x,self.y)

        #moving the platforms 
        if self.x < self.x1:
            self.vx = 1
            self.dir = 1
            
        elif self.x > self.x2:
            self.vx=-1

        self.x+=self.vx
        self.y+=self.vy

class Crates:
    def __init__(self,x,y,w,h,img):
         self.x=x
         self.y=y
         self.w=w
         self.h=h
         self.vx = 1
         self.vy=0
        
         self.x1=self.x-150
         self.x2=self.x+150
         self.img=loadImage("crates.png")
        
    def display(self):
        image(self.img,self.x-game.x,self.y)
                                                                                                                                                                                                                                                                                                                                                                                                                                                    
game= Game() 

def setup():
    global path 
    path=os.getcwd()
    print path
    size(game.w,game.h)
    background(0)
    game.CreateGame() 

def draw():
    #starting the game
    #menu screen
    if game.state=="menu":
        img =loadImage("MenuPage.png") 
        image(img,0,0)

    #game display when transformed to the play mode 
    elif game.state=="Play":
         game.display() 
  
    #choosing the character
    elif game.state=="Choose Character":
        img=loadImage("chooseplayer.png") 
        image(img,0,0)
    
    #gameover screen
    elif game.state=="enterName":
        img=loadImage("gameover.png") 
        image(img,0,0) 
        textSize(50)
        fill(255)
        text('Your score is: ', 300, 500)
        text(game.score, 650, 500)
        textSize(30)
        text("Please enter your name:",300,390)
        fill(0,0,150)
        rect(350,400,250,50)
        fill(0,150,255)
        text(game.name,360,430)
        
    #win screen     
    elif game.state=='win':
        img=loadImage("win.png")
        image(img,0,0)
        textSize(50)
        fill(255)
        text('Your score is: ', 200, 500)
        text(game.score, 550, 500)
        textSize(30)
        text("Please enter your name:",300,390)
        fill(0,0,150)
        rect(350,400,250,50)
        fill(0,150,255)
        text(game.name,360,430)
        
    #highscore page 
    elif game.state=="stats":
        img=loadImage("statsbackground.png")
        image(img,0,0)
        
        r= open("highscores.csv","r")
        array=[]
        for line in r:
            line = line.rstrip('\n')
            line = line.split(',')
            line[1] = int(line[1])
            array.append( line )
        r.close()
        
        array.sort(key=lambda x:x[1])
        array.reverse()
        textSize(75)
        text('Highscores', 330, 80)
        
        for i in range (8):
            if i == 0:
                fill(220, 20, 20)
            else:
                fill(255)
            
            textSize(40)
            
            text(i+1, 300, (i+3)*70)
            
            text(array[i][0], 400, (i+3)*70)
            text(array[i][1], 700, (i+3)*70)
            
    elif game.state=='instructions':
        img=loadImage("instructions.png")
        image(img,0,0)

    

def keyPressed():
    if keyCode == LEFT:
        game.player.keyHandler[LEFT]=True 
    elif keyCode== RIGHT:
        game.player.keyHandler[RIGHT]=True 
    elif keyCode==UP:
        game.player.keyHandler[UP]= True

def keyReleased():

    if keyCode == LEFT:
        game.player.keyHandler[LEFT] = False
    elif keyCode == RIGHT:
        game.player.keyHandler[RIGHT] = False
    elif keyCode == UP:
        game.player.keyHandler[UP] = False
        
    if game.state=='enterName':
        print keyCode, key, type(key)
    
        if keyCode == 8:
            game.name = game.name[:len(game.name)-1]
            
        elif keyCode == 10:
            f = open("highscores.csv","a")
            f.write(game.name+','+str(game.score)+'\n')   #add score and name to file
            f.close()
            
            game.__init__()
            game.CreateGame()
            
        elif type(key) != int :
            game.name += key
        
    if game.state=='win':
         
        print keyCode, key, type(key)
    
        if keyCode == 8:
            game.name = game.name[:len(game.name)-1]
            
        elif keyCode == 10:
            f = open("highscores.csv","a")
            f.write(game.name+','+str(game.score)+'\n')   #add score and name to file
            f.close()
            
            game.__init__()
            game.CreateGame()
            
        elif type(key) != int :
            game.name += key

def mouseClicked():
    
    #starting the game 
    if game.state=="menu" and 421 <= mouseX <= 502 \
    and 632 <= mouseY <= 700:
        game.click.play()
        game.click.rewind()  
        game.state='Play' 
        
    elif game.state=="menu" and 333<= mouseX <= 400 and 632 <= mouseY <= 700:
         game.click.play()
         game.click.rewind()
         game.state= 'Choose Character' 
         
    elif game.state=="menu" and 524<= mouseX <=597 and 625 <= mouseY<= 690:
         game.click.play()
         game.click.rewind() 
         game.state='stats' 
    
    elif game.state=="menu" and 610<= mouseX <= 740 and 644 <= mouseY <=688:
        game.click.play()
        game.click.rewind() 
        game.state='instructions' 
        
    #in player (after choosing a character)  
    if game.state=='Choose Character' and 96 <= mouseX <= 450 and 321 <= mouseY <= 489 :
         game.player=Sonic(50,50,52,625,"amyrose.png",4,130,130) 
         game.click.play()
         game.state='Play'
      
    elif game.state=='Choose Character' and 539 <= mouseX <= 904 and 178 <= mouseY <= 660:
        game.click.play()
        # self.player=Sonic(50,50,28,625,"sonicrunning.png",12,92)
        game.player=Sonic(50,50,28,625,"sonicrunning.png",12,92,56)
        game.state='Play'
        
    if game.state=="stats" and 47 <= mouseX <= 143 \
    and 651 <= mouseY <= 735:    
        game.click.play()
        game.click.rewind() 
        game.state='menu' 
        
    if game.state=='instructions' and 663 <= mouseX <= 762 \
    and 640 <= mouseY <= 734:    
        game.click.play()
        game.click.rewind() 
        game.state='menu' 
        
    
