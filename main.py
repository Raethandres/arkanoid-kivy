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
#from plyer import accelerometer


class ArkanivyBrick(Widget):
	color=(1,1,2,2)

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
            return True
        return False

    def on_parent(self, widget, parent):
        if parent is not None:
        	color
            parent.bricks.append(self)


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


class ArkanivyGame(Widget):
    ball = ObjectProperty(None)
    player = ObjectProperty(None)
    bricks =  ListProperty([])
    sw=0
    sb=0

    def serve_ball(self, vel=(0, 1)):
        self.ball.center_x = self.player.center_x
        self.ball.center_y = self.player.center_y+30
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()

        # bounce of paddles
        self.player.bounce_ball(self.ball)

        for brick in self.bricks:
        	if brick.bounce_ball(self.ball):
				try:
					self.remove_widget(brick)
					brick.center_x=brick.center_x+10000
					self.player.score+=1
				except:
					brick.center_x=brick.center_x+10000
					self.player.score+=1
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

        if self.player.score>=13:
        	# self.bricks[0].center_x=100
        	# self.bricks[0].center_y=100
        	# self.returnBall()
        	# self.add_widget(self.bricks[0])
        	returnBall()
        	return False

    def returnBall(self):
    	self.sb=0
        self.ball.center_x = self.player.center_x
        self.ball.center_y = self.player.center_y+30
        self.ball.velocity = (0,0)

    def on_touch_down(self, touch):
        if touch.x>self.player.center_x-(self.player.width) and  touch.x<self.player.center_x+(self.player.width) and touch.y>self.player.center_y-(self.player.height/2) and  touch.y<self.player.center_y+(self.player.height/2) :
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

class ArkanivyGame1(Widget):
    ball = ObjectProperty(None)
    player = ObjectProperty(None)
    bricks =  ListProperty([])
    sw=0
    sb=0

    def serve_ball(self, vel=(0, 1)):
        self.ball.center_x = self.player.center_x
        self.ball.center_y = self.player.center_y+30
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()

        # bounce of paddles
        self.player.bounce_ball(self.ball)

        for brick in self.bricks:
        	if brick.bounce_ball(self.ball):
				try:
					self.remove_widget(brick)
					brick.center_x=brick.center_x+10000
					self.player.score+=1
				except:
					brick.center_x=brick.center_x+10000
					self.player.score+=1
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

        if self.player.score>=13:
        	# self.bricks[0].center_x=100
        	# self.bricks[0].center_y=100
        	# self.returnBall()
        	# self.add_widget(self.bricks[0])
        	returnBall()
        	return False

    def returnBall(self):
    	self.sb=0
        self.ball.center_x = self.player.center_x
        self.ball.center_y = self.player.center_y+30
        self.ball.velocity = (0,0)

    def on_touch_down(self, touch):
        if touch.x>self.player.center_x-(self.player.width) and  touch.x<self.player.center_x+(self.player.width) and touch.y>self.player.center_y-(self.player.height/2) and  touch.y<self.player.center_y+(self.player.height/2) :
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
    def build(self):
        game = ArkanivyGame()
        gam=ArkanivyGame1()
        caro=Carousel()
        caro.add_widget(game)
        #caro.add_widget(gam)
       #game.serve_ball()
        #Builder.apply_file(game, 'level1.kv')
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        print 'ok'
        return caro


if __name__ == '__main__':
    ArkanivyApp().run()
