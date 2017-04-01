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
#from kivy.label import Label
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
#from plyer import accelerometer

class ArkanivyBrick(Widget):
    m=100  #650
    def var(self):
    	self.dic={'1':self.level1,'2':self.level2,'4':self.level4}
        self.po={'1':48,'2':9}
        self.im=[]
        self.p=0

    def level1(self):
        y=1
        if self.im:
            self.im=[]
        else:
            px=0
            py=300
            for x in range(13):
                for z in range(4):
                    self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=px ,y=py,size=(56, 26)))
                    py+=30
                    y+=1
                px+=60
                py=300
                y=1
            
        return self.im

    def level2(self):
        y=1
        if self.im:
            self.im=[]
        else:
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=500 ,y=300))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=556 ,y=300))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=612 ,y=300))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=444 ,y=300))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=388 ,y=300))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=332 ,y=300))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=276 ,y=300))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=220 ,y=300))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=164 ,y=300))
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
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=300 ,y=1100-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=361 ,y=1100-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=422 ,y=1100-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=483 ,y=1100-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=239 ,y=1069-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=300 ,y=1069-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=422 ,y=1069-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=483 ,y=1069-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=239 ,y=1038-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=300 ,y=1038-self.m,size=(56, 26)))       
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=361 ,y=1038-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=422 ,y=1038-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=483 ,y=1038-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=422 ,y=1007-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=483 ,y=1007-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=544 ,y=1007-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=239 ,y=976-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=300 ,y=976-self.m,size=(56, 26)))       
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=361 ,y=976-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=422 ,y=976-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=483 ,y=976-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=544 ,y=976-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=605 ,y=976-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=178 ,y=945-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=239 ,y=945-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=300 ,y=945-self.m,size=(56, 26)))       
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=361 ,y=945-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=422 ,y=945-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=483 ,y=945-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=544 ,y=945-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=605 ,y=945-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=178 ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=239 ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=300 ,y=914-self.m,size=(56, 26)))       
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=361 ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=422 ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=483 ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=544 ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=605 ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=178 ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=239 ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=300 ,y=914-self.m,size=(56, 26)))       
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=361 ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=422 ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=483 ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=544 ,y=914-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(y)+'.png' ,x=239 ,y=883-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=300 ,y=883-self.m,size=(56, 26)))       
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=361 ,y=883-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=300 ,y=852-self.m,size=(56, 26)))       
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=361 ,y=852-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=422 ,y=852-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=483 ,y=852-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=544 ,y=852-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=300 ,y=821-self.m,size=(56, 26)))       
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=361 ,y=821-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=483 ,y=821-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=544 ,y=821-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=300 ,y=790-self.m,size=(56, 26)))       
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=361 ,y=790-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=422 ,y=790-self.m,size=(56, 26)))
            self.im.append(Image(source='resorce/'+str(x)+'.png' ,x=483 ,y=790-self.m,size=(56, 26)))

        return self.im

    def bounce_ball(self,ball,index):
        
        #print self.im
        if self.im[index].collide_widget(ball):
            #print 'df'
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
    
    # def on_parent(self, widget, parent):
    #     if parent is not None:
    #         parent.bricks.append(self)


class ArkanivyPaddle(Widget):
    score = NumericProperty(0)
    level = ObjectProperty("Level 1")
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
<<<<<<< HEAD
=======
        #print 'move'



>>>>>>> 4cdc3423d4ee1d3be95f148a088aafa4f9fb7111

class ArkanivyGame(Widget):
    ball = ObjectProperty(None)
    player = ObjectProperty(None)
    #bricks =  ListProperty([])
    bricks= ArkanivyBrick()
    sw=0
    sb=0
    poi=NumericProperty(0)

    def load_level(self,l):
<<<<<<< HEAD
=======
<<<<<<< HEAD

        self.bricks.var()
        f=self.bricks.dic[l]
        f()
        for x in self.bricks.im:
	   	   self.add_widget(x)
=======
        
>>>>>>> cf4d88bb93713cac9d147997568d4ad9f5ca2891
        self.bricks.var()
        self.poi=int(self.bricks.po[l])
        f=self.bricks.dic[l]
        f()
        for x in self.bricks.im:
            self.add_widget(x)
>>>>>>> 4cdc3423d4ee1d3be95f148a088aafa4f9fb7111

<<<<<<< HEAD
=======
    def load_im(self):
        self.life=[]
        self.life.append(Image(source='resorce/vida.png',x=0,y=self.height-100))
        self.life.append(Image(source='resorce/vida.png',x=25,y=self.height-100))
        self.life.append(Image(source='resorce/vida.png',x=50,y=self.height-100))
        for x in self.life:
            self.add_widget(x)
     #   self.lifes=3;

<<<<<<< HEAD
    def serve_ball(self, vel=(0, 4)):
=======
>>>>>>> cf4d88bb93713cac9d147997568d4ad9f5ca2891
    def serve_ball(self, vel=(0, 1)):
        #print 'serve'
>>>>>>> 4cdc3423d4ee1d3be95f148a088aafa4f9fb7111
        self.ball.center_x = self.player.center_x
        self.ball.center_y = self.player.center_y+30
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()

        # bounce of paddles
        self.player.bounce_ball(self.ball)
<<<<<<< HEAD
        for x in range(len(self.bricks.im)-1):
=======
        #print len(self.bricks.im)
        for x in range(len(self.bricks.im)):
>>>>>>> 4cdc3423d4ee1d3be95f148a088aafa4f9fb7111
            #print x
            if self.bricks.bounce_ball(self.ball,x):
                self.remove_widget(self.bricks.im[x])
                self.bricks.im[x].center_x=self.bricks.im[x].center_x+10000
                self.bricks.im.pop(x)
                self.player.score+=1
                break
        #         try:
        #             self.remove_widget(brick)
        #             brick.center_x=brick.center_x+10000
        #             self.player.score+=1
        #         except:
        #             brick.center_x=brick.center_x+10000
        #             self.player.score+=1
            #self.remove_widget(self.bricks)
            #self.bricks.remove(brick)

        # bounce ball off size
        
        if self.ball.top > self.top:
            self.ball.velocity_y *= -1
        if self.ball.x < self.x or self.ball.x + self.ball.width > self.width:
            self.ball.velocity_x *= -1

        # went of to bottom
        if self.ball.y < self.y:
            self.returnBall()

<<<<<<< HEAD
        if self.player.score>=2:
            self.load_level('2')
=======
        if self.player.score>=self.poi:
            aux=self.player.level.split(' ')
            f=int(aux[1])
            f+=1
            self.load_level(str(f))
            self.player.Level="Level "+str(f)
>>>>>>> 4cdc3423d4ee1d3be95f148a088aafa4f9fb7111
            self.player.score=0

            # self.bricks[0].center_x=100
            # self.bricks[0].center_y=100
            # self.returnBall()
            # self.add_widget(self.bricks[0])
            self.returnBall()
            #return False

    def returnBall(self):
        self.sb=0
        self.ball.center_x = self.player.center_x
        self.ball.center_y = self.player.center_y+30
        self.ball.velocity = (0,0)

    def on_touch_down(self, touch):
        if self.player.collide_point(touch.x, touch.y):
            print 'aa'
        if touch.x>self.player.center_x-(self.player.width) and  touch.x<self.player.center_x+(self.player.width)  and  touch.y<self.player.center_y+(self.player.height/2) :
            self.sw=1
        if not self.sb and touch.x>self.ball.center_x-(self.ball.width) and  touch.x<self.ball.center_x+(self.ball.width) and touch.y>self.ball.center_y-(self.ball.height/2) and  touch.y<self.ball.center_y+(self.ball.height/2) :
            self.serve_ball()
            self.sb=1
    def on_touch_move(self, touch):
        if self.sw:
            self.player.center_x = touch.x
        if not self.sb:
            self.ball.center_x=touch.x
    def on_touch_up(self,touch):
        self.sw=0



class ArkanivyApp(App):
    # img=Image(source='resorce/1.png' ,x=200 ,y=512,size=(56, 26))
    # sm= ScreenManager()
    # s=Screen()

    # def on_touch_down(self,touch):
    #     if self.img.collide_point(touch.x,touch.y):
    #         self.sm.current = '2'

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
<<<<<<< HEAD

        
        game=self.level1()
        # game1=self.level2()
        # s=Screen(name='1')
        # s.add_widget(game)
        # s.add_widget(self.img)
        # s1=Screen(name='2')
        # s1.add_widget(game1)
        # self.sm.add_widget(s)
        # self.sm.add_widget(s1)

=======
<<<<<<< HEAD
        game=ArkanivyGame()
        game.load_im()
        game.load_level('4')
        Clock.schedule_interval(game.update, 1.0 / 60.0)
=======
        game=self.level1()
>>>>>>> 4cdc3423d4ee1d3be95f148a088aafa4f9fb7111
>>>>>>> cf4d88bb93713cac9d147997568d4ad9f5ca2891
        #game=self.level2()
        
        return game


if __name__ == '__main__':
    ArkanivyApp().run()