"""
File: bouncing_ball.py
Name: Chun
-------------------------
TODO: the ball is boucing, only 3 times.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked


VX = 3
DELAY = 50
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40


window = GWindow(800, 500, title='bouncing_ball.py')
point = GOval(SIZE, SIZE, x=START_X, y=START_Y)
point.filled = True
point2 = point
starting_or_not = False
time = 1


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    window.add(point)
    onmouseclicked(action)


def action(event):
    global starting_or_not, time, point2
    vx2 = VX
    new_y = window.height-(window.height-START_Y)*REDUCE  # y第一次彈跳後的高度
    if not starting_or_not:
        starting_or_not = True
        if time <= 3:
            while True:
                if point2.x <= window.width:  # 往右還有空間
                    if point2.y <= window.height:  # 往下還有空間
                        point2.move(VX, vx2)
                        vx2 = vx2 + GRAVITY  # 向下加速度
                        pause(DELAY)
                    else:
                        # 是否觸底反彈
                        while point2.y >= new_y:
                            point2.move(VX, -vx2)
                            pause(DELAY)
                        vx2 = VX
                        new_y = window.height - (window.height - new_y) * REDUCE  # 調整y每次的高度
                # 右方已無空間，重置球的狀態且次數+1
                else:
                    time += 1
                    window.remove(point2)
                    point2 = GOval(SIZE, SIZE, x=START_X, y=START_Y)
                    point2.filled = True
                    window.add(point2)
                    starting_or_not = False
                    break  # 跳出while迴圈
        # 超過次數後，球無反應
        else:
            window.add(point)


if __name__ == "__main__":
    main()
