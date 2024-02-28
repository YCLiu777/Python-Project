"""
File: my_drawing.py
Name: Chun
----------------------
TODO: My minions!
"""


from campy.graphics.gobjects import GOval, GRect, GLine, GArc, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: My Minions!

    Hope those cute guys can make us complete the courses of programming perfectly.
    Bello! Nanna!
    (工廠的小小兵來啦~)
    """
    window = GWindow(1000, 650, title='My Minions! ', color='ivory')
    bello = GLabel('Bello! ')
    bello.font = 'Dialog-90-bold-italic'
    bello.color = 'red'
    window.add(bello, x=570, y=290)
    # 本體
    face = GArc(300, 350, 0, 180)
    face.color = 'YELLOW'
    face.filled = True
    face.fill_color = 'YELLOW'
    window.add(face, x=150, y=130)
    body = GRect(300, 220)
    body.color = 'YELLOW'
    body.filled = True
    body.fill_color = 'yellow'
    window.add(body, x=150, y=210)
    # 可愛的臉(護目鏡)
    glasses_1 = GOval(160, 160)
    glasses_1.color = 'gray'
    glasses_1.filled = True
    glasses_1.fill_color = 'gray'
    window.add(glasses_1, x=150, y=150)
    glasses_2 = GOval(160, 160)
    glasses_2.color = 'gray'
    glasses_2.filled = True
    glasses_2.fill_color = 'gray'
    window.add(glasses_2, x=290, y=150)
    # 左邊的眼睛/綠色
    eye_l1 = GOval(120, 120)
    eye_l1.color = 'white'
    eye_l1.filled = True
    eye_l1.fill_color = 'white'
    window.add(eye_l1, x=170, y=170)
    eye_l2 = GOval(35, 35)
    eye_l2.color = 'lawngreen'
    eye_l2.filled = True
    eye_l2.fill_color = 'lawngreen'
    window.add(eye_l2, x=225, y=210)
    eye_l3 = GOval(17, 17)
    eye_l3.color = 'maroon'
    eye_l3.filled = True
    eye_l3.fill_color = 'maroon'
    window.add(eye_l3, x=239, y=220)
    eye_l4 = GOval(5, 5)
    eye_l4.color = 'white'
    eye_l4.filled = True
    eye_l4.fill_color = 'white'
    window.add(eye_l4, x=248, y=223)
    # 右邊的眼睛/褐色
    eye_r1 = GOval(120, 120)
    eye_r1.color = 'white'
    eye_r1.filled = True
    eye_r1.fill_color = 'white'
    window.add(eye_r1, x=310, y=170)
    eye_r2 = GOval(35, 35)
    eye_r2.color = 'peru'
    eye_r2.filled = True
    eye_r2.fill_color = 'peru'
    window.add(eye_r2, x=330, y=210)
    eye_r3 = GOval(17, 17)
    eye_r3.color = 'maroon'
    eye_r3.filled = True
    eye_r3.fill_color = 'maroon'
    window.add(eye_r3, x=335, y=220)
    eye_r4 = GOval(5, 5)
    eye_r4.color = 'white'
    eye_r4.filled = True
    eye_r4.fill_color = 'white'
    window.add(eye_r4, x=343, y=223)
    # 嘴巴
    mouth = GArc(100, 100, 250, 100)
    window.add(mouth, x=280, y=290)
    # 連身褲
    cloth_1 = GArc(300, 300, 180, 180)
    cloth_1.color = 'blue'
    cloth_1.filled = True
    cloth_1.fill_color = 'blue'
    window.add(cloth_1, x=150, y=345)
    cloth_2 = GRect(200, 100)
    cloth_2.color = 'blue'
    cloth_2.filled = True
    cloth_2.fill_color = 'blue'
    window.add(cloth_2, x=200, y=365)
    # 肩帶
    strap_1 = GPolygon()
    strap_1.add_vertex((150, 320))
    strap_1.add_vertex((220, 405))
    strap_1.add_vertex((245, 405))
    strap_1.add_vertex((150, 295))
    strap_1.color = 'blue'
    strap_1.filled = True
    strap_1.fill_color = 'blue'
    window.add(strap_1)
    strap_2 = GPolygon()
    strap_2.add_vertex((450, 320))
    strap_2.add_vertex((375, 405))
    strap_2.add_vertex((350, 405))
    strap_2.add_vertex((450, 295))
    strap_2.color = 'blue'
    strap_2.filled = True
    strap_2.fill_color = 'blue'
    window.add(strap_2)
    # 口袋
    pocky_1 = GArc(100, 190, 180, 180)
    pocky_1.filled = True
    pocky_1.fill_color = 'blue'
    window.add(pocky_1, x=250, y=340)
    # stanCode專用小小兵
    logo = GLabel('S')
    logo.font = 'Helvetica-30-bold'
    logo.color = 'ivory'
    window.add(logo, x=287, y=433)
    # 兩個小褲管
    pants_1 = GRect(30, 30)
    pants_1.color = 'BLUE'
    pants_1.filled = True
    pants_1.fill_color = 'BLUE'
    pants_2 = GRect(30, 30)
    pants_2.color = 'BLUE'
    pants_2.filled = True
    pants_2.fill_color = 'BLUE'
    window.add(pants_1, x=268, y=480)
    window.add(pants_2, x=303, y=480)
    # 左邊的鞋
    shoes_l1 = GArc(80, 50, 60, 120)
    shoes_l1.filled = True
    window.add(shoes_l1, 240, 510)
    shoes_l2 = GRect(50, 13)
    shoes_l2.filled = True
    window.add(shoes_l2, 240, 520)
    shoes_l3 = GRect(30, 23)
    shoes_l3.filled = True
    window.add(shoes_l3, 268, 510)
    # 右邊的鞋
    shoes_r1 = GArc(80, 50, 0, 120)
    shoes_r1.filled = True
    window.add(shoes_r1, 300, 510)
    shoes_r2 = GRect(50, 13)
    shoes_r2.filled = True
    window.add(shoes_r2, 310, 520)
    shoes_r3 = GRect(30, 23)
    shoes_r3.filled = True
    window.add(shoes_r3, 302, 510)
    # 左邊的手
    hand_l1 = GArc(75, 100, 90, 180)
    hand_l1.color = 'YELLOW'
    hand_l1.filled = True
    hand_l1.fill_color = 'YELLOW'
    window.add(hand_l1, 130, 323)
    hand_l2 = GLine(150, 350, 150, 420)
    window.add(hand_l2)
    hand_l3 = GOval(17, 17)
    hand_l3.filled = True
    window.add(hand_l3, x=135, y=415)
    hand_l4 = GOval(25, 25)
    hand_l4.filled = True
    window.add(hand_l4, x=148, y=407)
    hand_l5 = GPolygon()
    hand_l5.add_vertex((130, 400))
    hand_l5.add_vertex((150, 390))
    hand_l5.add_vertex((173, 420))
    hand_l5.add_vertex((150, 430))
    hand_l5.filled = True
    window.add(hand_l5)
    # 右邊的手
    hand_r1 = GPolygon()
    hand_r1.add_vertex((450, 320))
    hand_r1.add_vertex((480, 250))
    hand_r1.add_vertex((505, 250))
    hand_r1.add_vertex((450, 360))
    hand_r1.color = 'yellow'
    hand_r1.filled = True
    hand_r1.fill_color = 'yellow'
    window.add(hand_r1)
    hand_r2 = GPolygon()
    hand_r2.add_vertex((470, 265))
    hand_r2.add_vertex((483, 240))
    hand_r2.add_vertex((508, 245))
    hand_r2.add_vertex((495, 275))
    hand_r2.filled = True
    window.add(hand_r2)
    hand_r3 = GOval(30, 30)
    hand_r3.filled = True
    window.add(hand_r3, x=485, y=215)
    hand_r4 = GOval(20, 20)
    hand_r4.filled = True
    window.add(hand_r4, x=470, y=225)
    hand_r5 = GOval(20, 20)
    hand_r5.filled = True
    window.add(hand_r5, x=502, y=235)


if __name__ == '__main__':
    main()
