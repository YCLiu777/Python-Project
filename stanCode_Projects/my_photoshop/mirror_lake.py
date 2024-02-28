"""
File: mirror_lake.py
Name: Chun
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(original_mt):
    """
    :param original_mt: SimpleImage, the original image.
    :return: SimpleImage, the updated image with mirror image.
    """
    reflected = SimpleImage.blank(original_mt.width, original_mt.height * 2)
    for x in range(original_mt.width):
        for y in range(original_mt.height):
            o_mt_p = original_mt.get_pixel(x, y)
            # Upper White pixel
            reflected_p = reflected.get_pixel(x, y)
            reflected_p.red = o_mt_p.red
            reflected_p.green = o_mt_p.green
            reflected_p.blue = o_mt_p.blue
            # Lower White pixel
            reflected_p_2 = reflected.get_pixel(x, reflected.height - y -1)  # 用大張空白圖的height才會對
            reflected_p_2.red = o_mt_p.red
            reflected_p_2.green = o_mt_p.green
            reflected_p_2.blue = o_mt_p.blue
    return reflected


def main():
    """
    TODO: The beauty of mirror images.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect(original_mt)
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
