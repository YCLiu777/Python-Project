"""
File: blur.py
Name: Chun  (之後多想想！)
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""
from simpleimage import SimpleImage


def blur(old_img):
    """
    :param old_img: SimpleImage, the original image.
    :return: SimpleImage, the updated image with blurred.
    """
    # Todo: create a new blank img that is as big as the original one
    new_img = SimpleImage.blank(old_img.width, old_img.height)
    # Loop over the picture
    for x in range(old_img.width):
        for y in range(old_img.height):
            r_sum = 0
            g_sum = 0
            b_sum = 0
            count = 0
            n_p = new_img.get_pixel(x, y)
            for i in range(-1, 2, 1):  # 九宮格x的範圍
                for j in range(-1, 2, 1):  # 九宮格y的範圍
                    pixel_x = x + i
                    pixel_y = y + j
                    if 0 <= pixel_x <= old_img.width-1:  # 判斷有沒有在圖片範圍裏面
                        if 0 <= pixel_y <= old_img.height-1:
                            pixel = old_img.get_pixel(pixel_x, pixel_y)
                            r_sum += pixel.red
                            g_sum += pixel.green
                            b_sum += pixel.blue
                            count += 1
            n_p.red = r_sum / count
            n_p.green = g_sum / count
            n_p.blue = b_sum / count
    return new_img


def main():
    """
    TODO: Let the photo blurred.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
