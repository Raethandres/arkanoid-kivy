import kivy
kivy.require('1.1.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, ListProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.carousel import Carousel
from kivy.uix.image import Image
from kivy.animation import Animation

class ArkanivyBrick(Widget):
    m=650  #650  #100
    nx=130
    rx=90
    def var(self):
        self.dic={'1':self.level1,'2':self.level2,'3':self.level3,'4':self.level4}
        self.po={'1':20,'2':36,'3':12,'4':62}
        self.im=[]
        self.p=0

    def level1(self):
        y=1
        if self.im:
            self.im=[]
        else:
            px=300
            py=300
            for x in range(5):
                for z in range(4):
                    self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=px ,y=py,size=(56, 26)))
                    py+=30
                    y+=1
                px+=60
                py=300
                y=1           
        return self.im

    def level2(self):
        y=4
        x=3
        if self.im:
            self.im=[]
        else:
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=422+self.nx ,y=1100-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=361+self.nx ,y=1069-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=300+self.nx ,y=1038-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=483+self.nx ,y=1038-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=239+self.nx ,y=1007-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=361+self.nx ,y=1007-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=422+self.nx ,y=1007-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=239+self.nx ,y=976-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=361+self.nx ,y=976-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=300+self.nx ,y=945-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=544+self.nx ,y=945-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=178+self.nx ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=239+self.nx ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=300+self.nx ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=361+self.nx ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=422+self.nx ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=483+self.nx ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=605+self.nx ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=605+self.nx ,y=883-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=239+self.nx ,y=852-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=300+self.nx ,y=852-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=361+self.nx ,y=852-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=422+self.nx ,y=852-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=605+self.nx ,y=852-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=117+self.nx ,y=821-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=544+self.nx ,y=821-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=117+self.nx ,y=790-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=269+self.nx ,y=790-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=330+self.nx ,y=790-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=391+self.nx ,y=790-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=178+self.nx ,y=759-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=239+self.nx ,y=759-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=300+self.nx ,y=759-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=361+self.nx ,y=759-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=422+self.nx ,y=759-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=483+self.nx ,y=759-self.m,size=(56, 26)))
        return self.im

    def level3(self):
        y=3
        if self.im:
            self.im=[]
        else:
            px=300
            py=300
            for x in range(3):
                for z in range(4):
                    self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=px ,y=py,size=(56, 26)))
                    py+=30
                    y+=1
                px+=60
                py=300
                y=1           
        return self.im

    def level4(self):
        y=6
        x=1
        if self.im:
            self.im=[]
        else:
            # 1: amarillo  6: azul         #self.width:ancho  #self.hidn:alto  #aumento x: 61 y 31 512
            #1200 y
            #720 x
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=300+self.rx ,y=1100-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=361+self.rx ,y=1100-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=422+self.rx ,y=1100-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=483+self.rx ,y=1100-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=239+self.rx ,y=1069-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=300+self.rx ,y=1069-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=422+self.rx ,y=1069-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=483+self.rx ,y=1069-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=239+self.rx ,y=1038-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=300+self.rx ,y=1038-self.m,size=(56, 26)))       
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=361+self.rx ,y=1038-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=422+self.rx ,y=1038-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=483+self.rx ,y=1038-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=422+self.rx ,y=1007-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=483+self.rx ,y=1007-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=544+self.rx ,y=1007-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=239+self.rx ,y=976-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=300+self.rx ,y=976-self.m,size=(56, 26)))       
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=361+self.rx ,y=976-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=422+self.rx ,y=976-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=483+self.rx ,y=976-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=544+self.rx ,y=976-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=605+self.rx ,y=976-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=178+self.rx ,y=945-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=239+self.rx ,y=945-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=300+self.rx ,y=945-self.m,size=(56, 26)))       
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=361+self.rx ,y=945-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=422+self.rx ,y=945-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=483+self.rx ,y=945-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=544+self.rx ,y=945-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=605+self.rx ,y=945-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=178+self.rx ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=239+self.rx ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=300+self.rx ,y=914-self.m,size=(56, 26)))       
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=361+self.rx ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=422+self.rx ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=483+self.rx ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=544+self.rx ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=605+self.rx ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=178+self.rx ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=239+self.rx ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=300+self.rx ,y=914-self.m,size=(56, 26)))       
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=361+self.rx ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=422+self.rx ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=483+self.rx ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=544+self.rx ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=239+self.rx ,y=883-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=300+self.rx ,y=883-self.m,size=(56, 26)))       
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=361+self.rx ,y=883-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=300+self.rx ,y=852-self.m,size=(56, 26)))       
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=361+self.rx ,y=852-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=422+self.rx ,y=852-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=483+self.rx ,y=852-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=544+self.rx ,y=852-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=300+self.rx ,y=821-self.m,size=(56, 26)))       
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=361+self.rx ,y=821-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=483+self.rx ,y=821-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=544+self.rx ,y=821-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=300+self.rx ,y=790-self.m,size=(56, 26)))       
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=361+self.rx ,y=790-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=422+self.rx ,y=790-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=483+self.rx ,y=790-self.m,size=(56, 26)))

        return self.im

    def bounce_ball(self,ball,index):
        if self.im[index].collide_widget(ball):
            vx, vy = ball.velocity
            offset = 0
            bounced = Vector(vx, -1 * vy)
            vel = bounced * 1.02
            if ball.center_x>self.center_x:
                if vel.x<-0.5:
                    ball.velocity = vel.x+1, vel.y+offset
                else:
                    ball.velocity=vel.x+0.5, vel.y+offset
            elif ball.center_x<self.center_x:
                if vel.x>0.5:
                    ball.velocity = vel.x-1, vel.y+offset
                else:
                    ball.velocity = vel.x-0.5, vel.y+offset
            else:
                ball.velocity = vel.x, vel.y+offset
            return True
        return False

class ArkanivyPaddle(Widget):
    score = NumericProperty(0)
    total = NumericProperty(0)
    level = ObjectProperty("...")
    sw=0
    g=0.5
    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = 0
            bounced = Vector(vx, -1 * vy)
            vel = bounced * 1.02
            if ball.center_x>self.center_x:
                if vel.x<-0.5:
                    ball.velocity = vel.x+1, vel.y+offset
                else:
                    ball.velocity=vel.x+0.5, vel.y+offset
            elif ball.center_x<self.center_x:
                if vel.x>0.5:
                    ball.velocity = vel.x-1, vel.y+offset
                else:
                    ball.velocity = vel.x-0.5, vel.y+offset
            else:
                ball.velocity = vel.x, vel.y+offset

class ArkanivyBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class ArkanivyGame(Widget):
    ball = ObjectProperty(None)
    player = ObjectProperty(None)
    vida=3
    life=[]
    bricks= ArkanivyBrick()
    sw=0
    sb=0
    poi=NumericProperty(0)


    def manu(self):
        self.b=[]
        self.b.append(Image(source='resorce/boton1.jpg',x=0,y=100))
        self.b.append(Image(source='resorce/boton2.jpg',x=100,y=100))
        self.b.append(Image(source='resorce/boton3.jpg',x=100,y=0))
        self.b.append(Image(source='resorce/boton4.jpg',x=0,y=0))
        for x in self.b:
            self.add_widget(x)
        self.mn=1
        self.mx=0
        self.my=100

    def load_level(self,l):  
        self.bricks.var()
        self.poi=int(self.bricks.po[l])
        f=self.bricks.dic[l]
        f()
        for x in self.bricks.im:
            self.add_widget(x)

    def load_im(self):   
        self.life.append(Image(source='resorce/vida.png',x=0,y=self.height-100))
        self.life.append(Image(source='resorce/vida.png',x=25,y=self.height-100))
        self.life.append(Image(source='resorce/vida.png',x=50,y=self.height-100))
        for x in self.life:
            self.add_widget(x)

    def serve_ball(self, vel=(0, 4)):
        self.ball.center_x = self.player.center_x
        self.ball.center_y = self.player.center_y+30
        self.ball.velocity = vel

    def update(self, dt):
        if not self.mn:
            self.ball.move()
            self.player.bounce_ball(self.ball)
            for x in range(len(self.bricks.im)):
                if self.bricks.bounce_ball(self.ball,x):
                    self.remove_widget(self.bricks.im[x])
                    self.bricks.im[x].center_x=self.bricks.im[x].center_x+10000
                    self.bricks.im.pop(x)
                    self.player.score+=1
                    self.player.total+=1
                    break
            if self.ball.top > self.top:
                self.ball.velocity_y *= -1
            if self.ball.x < self.x or self.ball.x + self.ball.width > self.width:
                self.ball.velocity_x *= -1
            if self.ball.y < self.y:
                self.life[self.vida-1].center_x=self.life[self.vida-1].center_x+10000
                self.vida-=1
                self.returnBall()
            if self.player.score>=self.poi:
                aux=self.player.level.split(' ')
                f=int(aux[1])
                f+=1
                self.load_level(str(f))
                self.player.level="Level "+str(f)
                self.player.score=0
                self.returnBall()
            if self.vida==0:
                print "murio el puto"
                self.clear()
                self.manu()
                #return False
        else:
            print "aja"


    def clear(self):
    	for x in self.bricks.im:
    		self.remove_widget(x)
    	self.bricks.im[:]=[]
    	self.vida=3
    	self.score=0
    	self.total=0

    def returnBall(self):
        self.sb=0
        self.ball.center_x = self.player.center_x
        self.ball.center_y = self.player.center_y+30
        self.ball.velocity = (0,0)

    def on_touch_down(self, touch):
        if touch.x>self.player.center_x-(self.player.width) and  touch.x<self.player.center_x+(self.player.width)  and  touch.y<self.player.center_y+(self.player.height/2) :
            self.sw=1
        if not self.sb and touch.x>self.ball.center_x-(self.ball.width) and  touch.x<self.ball.center_x+(self.ball.width) and touch.y>self.ball.center_y-(self.ball.height/2) and  touch.y<self.ball.center_y+(self.ball.height/2) :
            self.serve_ball()
            self.sb=1
        g=-1
        for bt in self.b:
            g+=1
            if bt.collide_point(touch.x,touch.y):
                self.load_level(str(g+1))
                self.player.level="Level "+str(g+1)
                self.load_im()
                for t in self.b:
                    self.remove_widget(t)
                self.mn=0
                self.b[:]=[]
                break

    def on_touch_move(self, touch):
        if self.sw:
            self.player.center_x = touch.x
        if not self.sb:
            self.ball.center_x=touch.x
    def on_touch_up(self,touch):
        self.sw=0

class ArkanivyApp(App):
    def level1(self):
        game = ArkanivyGame()
        game.load_level('1')
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

    def level2(self):
        game = ArkanivyGame()
        game.load_level('2')
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

    def level3(self):
        game = ArkanivyGame()
        game.load_level('3')
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

    def level4(self):
        game = ArkanivyGame()
        game.load_level('4')
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


    def build(self):
        game=ArkanivyGame()
        game.manu()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == '__main__':
    ArkanivyApp().run()