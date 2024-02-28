"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts
start_or_not = False


def main():
    global start_or_not
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    # Add the animation loop here!
    if not start_or_not:
        start_or_not = True
        while True:
            pause(FRAME_RATE)
            if graphics.total_brick > 0:
                if graphics.ball_hit_bottom():
                    lives -= 1
                    start_or_not = False
                    if lives > 0:
                        graphics.reset_ball()
                    else:
                        graphics.game_over()
                        break
                else:
                    if graphics.paddle_or_brick_hit():
                        graphics.paddle_and_bricks_collisions()
                    else:
                        graphics.wall_collisions()
                    graphics.move_ball()
            else:
                graphics.win()
                break


if __name__ == '__main__':
    main()
