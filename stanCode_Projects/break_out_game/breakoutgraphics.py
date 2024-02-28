"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)
        self.brick_cols = brick_cols
        self.brick_rows = brick_rows
        self.total_brick = self.brick_cols * self.brick_rows

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window_width-paddle_width)/2, y=self.window_height-paddle_height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window_width-ball_radius*2)/2, y=(self.window_height-ball_radius*2)/2)
        self.ball_radius = ball_radius

        # Draw bricks
        for i in range(0, brick_cols+1):
            for j in range(0, brick_rows+1):
                self.brick = GRect(width=brick_width, height=brick_height)
                self.brick.filled = True
                self.brick.color = 'black'
                k = j-1
                if k // 2 == 0:
                    self.brick.fill_color = 'red'
                elif k // 2 == 1:
                    self.brick.fill_color = 'orange'
                elif k // 2 == 2:
                    self.brick.fill_color = 'yellow'
                elif k // 2 == 3:
                    self.brick.fill_color = 'green'
                else:
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick, x=0 + (i - 1) * (brick_width + brick_spacing),
                                y=0 + (j - 1) * (brick_height + brick_spacing))
        self.__dx = 0
        self.__dy = 0
        onmousemoved(self.handle_move)
        onmouseclicked(self.handle_click)

    # Initialize our mouse listeners
    def handle_move(self, event):
        """
        The controller of the paddle.  # 無法讓他邊邊完整@@
        """
        if event.x >= self.paddle.width/2 or event.x <= self.window.width - self.paddle.width/2:
            self.paddle.x = event.x - self.paddle.width/2
        elif event.x < self.paddle.width/2:
            self.paddle.x = 0
        else:
            self.paddle.x = self.window.width - self.paddle.width

    def handle_click(self, event):
        """
        The controller of game start.
        """
        if self.__dx == 0 and self.__dy == 0:
            self.set_ball_velocity()

    # Default initial velocity for the ball
    def start_ball(self):
        self.move_ball()

    def move_ball(self):
        self.ball.move(self.__dx, self.__dy)

    def set_ball_velocity(self):
        """
        Set ball's velocity, and private.
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = -INITIAL_Y_SPEED
        return self.__dx, self.__dy

    # Rebounding action
    def wall_collisions(self):
        """
        Rebounding when hit the wall.
        """
        if self.ball.x <= 0 or self.ball.x >= self.window.width - self.ball.width:
            self.__dx = - self.__dx
        if self.ball.y <= 0:
            self.__dy = - self.__dy
        return self.__dx, self.__dy

    def paddle_and_bricks_collisions(self):
        """
        Rebounding when hit bricks or the paddle.
        """
        self.__dx = self.__dx
        self.__dy = - self.__dy
        return self.__dx, self.__dy

    def paddle_or_brick_hit(self):
        """
        Hit paddle or bricks?
        """
        for i in range(0, 2):
            for j in range(0, 2):
                self.obj = self.window.get_object_at(self.ball.x + i*self.ball.width, self.ball.y + j*self.ball.height)
                if self.obj is not None:
                    if self.obj is self.paddle:
                        print('hit paddle')
                        self.paddle_and_bricks_collisions()
                        self.move_ball()
                    else:
                        print('hit brick')
                        self.brick_remove()
                        self.paddle_and_bricks_collisions()
                        self.move_ball()

    def brick_remove(self):
        """
        Removed the brick when hit.
        """
        self.window.remove(self.obj)
        self.total_brick -= 1
        print(self.total_brick)
        if self.total_brick == 0:
            self.reset_ball()

    def ball_hit_bottom(self):
        """
        Miss the ball.
        """
        ball_hit_bottom = self.ball.y >= self.window.height - self.ball.height
        return ball_hit_bottom

    def reset_ball(self):
        """
        Reset the ball.
        """
        self.set_ball_position()

    def set_ball_position(self):
        """
        Sets the ball position by initial site.
        """
        self.ball.x = (self.window_width-self.ball_radius*2)/2
        self.ball.y = (self.window_height-self.ball_radius*2)/2
        self.__dx = 0
        self.__dy = 0

    def win(self):
        """
        Win the game!
        """
        self.win = GLabel('You Win!')
        self.win.font = '-40'
        self.window.add(self.win, (self.window.width - self.win.width) / 2,
                             (self.window.height + self.win.height) / 2)
        self.window.remove(self.paddle)
        self.window.remove(self.ball)

    def game_over(self):
        """
        Lose the game.
        """
        self.game_over = GLabel('Game Over :( ')
        self.game_over.font = '-40'
        self.window.add(self.game_over, self.window.width / 2 - self.game_over.width / 2,
                            self.window.height / 2 + self.game_over.height)
        self.window.remove(self.ball)