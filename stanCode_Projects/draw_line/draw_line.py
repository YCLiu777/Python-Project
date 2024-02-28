"""
File: draw_line.py
Name: Chun
-------------------------
TODO: let points 2 a line.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


# This constant controls the size of the GOval
SIZE = 6  # 題目說常數是半徑，使用時要記得*2

window = GWindow()
time = 0
p1x = 0  # 奇數點x座標
p1y = 0  # 奇數點y座標
point = 0  # 紀錄奇數點


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(event):
    global time, p1x, p1y, point
    if time == 0 or time % 2 == 0:
        point = GOval(2 * SIZE, 2 * SIZE, x=event.x - 2 * SIZE / 2, y=event.y - 2 * SIZE / 2)
        window.add(point)
        p1x = event.x
        p1y = event.y
        point = point
    else:
        # point2 = GOval(2 * SIZE, 2 * SIZE, x=event.x - 2 * SIZE / 2, y=event.y - 2 * SIZE / 2)
        # point2.filled = False  # True判斷偶數點/False判斷畫線是否在圓心
        # window.add(point2)  # 這三行用來檢查偶數點擊是否判斷正確
        line = GLine(p1x, p1y, event.x, event.y)
        window.add(line)
        window.remove(point)
    time += 1


if __name__ == "__main__":
    main()
