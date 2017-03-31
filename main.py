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
#from plyer import accelerometer


class ArkanivyBrick(Widget):
    

    def var(self):
        self.dic={'1':self.level1,'2':self.level2}
        self.im=[]
        self.p=0

    def level1(self):
        y=1
        if self.im:
            self.im=[]
        else:
            self.im.append(Image(source='/resorce/'+str(y)+'.png' ,x=500 ,y=300,size=(56, 26)))
            self.im.append(Image(source='/resorce/'+str(y)+'.png' ,x=556 ,y=300,size=(56, 26)))
            # self.im.append(Image(source=str(y)+'.png' ,x=612 ,y=300,size=(56, 26)))
            # self.im.append(Image(source=str(y)+'.png' ,x=444 ,y=300,size=(56, 26)))
            # self.im.append(Image(source=str(y)+'.png' ,x=388 ,y=300,size=(56, 26)))
            # self.im.append(Image(source=str(y)+'.png' ,x=332 ,y=300,size=(56, 26)))
            # self.im.append(Image(source=str(y)+'.png' ,x=276 ,y=300,size=(56, 26)))
            # self.im.append(Image(source=str(y)+'.png' ,x=220 ,y=300,size=(56, 26)))
            self.im.append(Image(source='/resorce/'+str(y)+'.png' ,x=164 ,y=300,size=(56, 26)))
        return self.im

    def level2(self):
        y=1
        if self.im:
            self.im=[]
        else:
            self.im.append(Image(source='/resorce/'+str(y)+'.png' ,x=500 ,y=300))
            self.im.append(Image(source='/resorce/'+str(y)+'.png' ,x=556 ,y=300))
            self.im.append(Image(source='/resorce/'+str(y)+'.png' ,x=612 ,y=300))
            self.im.append(Image(source='/resorce/'+str(y)+'.png' ,x=444 ,y=300))
            self.im.append(Image(source='/resorce/'+str(y)+'.png' ,x=388 ,y=300))
            self.im.append(Image(source='/resorce/'+str(y)+'.png' ,x=332 ,y=300))
            self.im.append(Image(source='/resorce/'+str(y)+'.png' ,x=276 ,y=300))
            self.im.append(Image(source='/resorce/'+str(y)+'.png' ,x=220 ,y=300))
            self.im.append(Image(source='/resorce/'+str(y)+'.png' ,x=164 ,y=300))
        return self.im

    def bounce_ball(self,ball,index):
        

        if self.im[index].collide_widget(ball):
            #print 'df'
            vx, vy = ball.velocity
            offset = 0
            bounced = Vector(vx, -1 * vy)
            vel = bounced * 1.1
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
    sw=0
    g=0.5
    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = 0
            bounced = Vector(vx, -1 * vy)
            vel = bounced * 1.1
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
        print 'move'




class ArkanivyGame(Widget):
    ball = ObjectProperty(None)
    player = ObjectProperty(None)
    #bricks =  ListProperty([])
    bricks= ArkanivyBrick()
    sw=0
    sb=0

    def load_level(self,l):
        self.bricks.var()
        f=self.bricks.dic[l]
        f()
        for x in self.bricks.im:
            #print 'aja'
            self.add_widget(x)


    def serve_ball(self, vel=(0, 1)):
        print 'serve'
        self.ball.center_x = self.player.center_x
        self.ball.center_y = self.player.center_y+30
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()

        # bounce of paddles
        self.player.bounce_ball(self.ball)

        for x in range(len(self.bricks.im)-1):
            #print x
            if self.bricks.bounce_ball(self.ball,x):
                self.remove_widget(self.bricks.im[x])
                self.bricks.im[x].center_x=self.bricks.im[x].center_x+10000
                self.bricks.im.pop(x)
                self.player.score+=1
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

        if self.player.score>=2:
            #self.load_level('2')
            # self.bricks[0].center_x=100
            # self.bricks[0].center_y=100
            # self.returnBall()
            # self.add_widget(self.bricks[0])
            self.returnBall()
            return False

    def returnBall(self):
        self.sb=0
        self.ball.center_x = self.player.center_x
        self.ball.center_y = self.player.center_y+30
        self.ball.velocity = (0,0)

    def on_touch_down(self, touch):
        if touch.x>self.player.center_x-(self.player.width) and  touch.x<self.player.center_x+(self.player.width)  and  touch.y<self.player.center_y+(self.player.height/2) :
            self.sw=1
        if touch.x>self.ball.center_x-(self.ball.width) and  touch.x<self.ball.center_x+(self.ball.width) and touch.y>self.ball.center_y-(self.ball.height/2) and  touch.y<self.ball.center_y+(self.ball.height/2) :
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
    def build(self):
        game=self.level1()
        #game=self.level2()
        
        return game


if __name__ == '__main__':
    ArkanivyApp().run()
