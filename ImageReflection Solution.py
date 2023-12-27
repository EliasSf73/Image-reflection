#QUESTION,1: REFLECT HUBO AT CENTER
from cs1media import *


def reflect_image(image):
    """
    Center point reflection of image

    Args:
        image: An image to be reflected

    Returns:
        The reflection of input image with respect to the center point
    """
    # -----
    # TODO: Write your code here

    w, h = image.size()
    result = create_picture(w, h)
    for x in range(w):
        for y in range(h):
            result.set(x, y, image.get(w - x - 1, h - y - 1))
    return result

    # for y in range(h//2):
    #     for x in range(w):
    #         pu= image.get(x,y)
    #         pd= image.get(x,h-y-1)
    #         image.set(x,y,pd)
    #         image.set(x,h-y-1,pu)

    # for y in range(h):
    #     for x in range(w//2):
    #         pl= image.get(x,y)
    #         pr= image.get(w-x-1,y)
    #         image.set(x,y,pr)
    #         image.set(w-x-1,y,pl)
    # return image
    # # -----


def main():
    # -----
    # You can try any of the following images.
    image_path = './images/minion.png'
    # image_path = './images/neobjuggi.png'
    # -----

    image = load_picture(image_path)
    reflected_image = reflect_image(image)
    reflected_image.show()


if __name__ == '__main__':
    main()




# QUESTION2: REFLECTING HUBO AT RANDOM POINT
from cs1media import *


def reflect_image(image, a, b):
    """
    Point reflection of image with respect to reference point (a, b)

    Args:
        image: An image to be reflected
        a: x-coordinate of the reference point
        b: y-coordinate of the reference point

    Returns:
        The reflection of input image with respect to the (a, b)th pixel
    """
    # -----
    # TODO: Write your code here

    w, h = image.size()
    print(w, h)
    result = create_picture(w, h, "red")
    for x in range(w):
        for y in range(h):
            if 0 <= 2 * a - x < w and 0 <= 2 * b - y < h:  # Range correction
                result.set(x, y, image.get(2 * a - x, 2 * b - y))
    return result

    # for i in range (w//2+1):
    #     for j in range(h//2+1):
    #         if a-i in range(w) and a+i in range(w):
    #             if b-j in range(h) and b+j in range(h):
    #                 result.set(a-i,b+j,image.get(a+i,b-j))
    #                 result.set(a+i,b-j,image.get(a-i,b+j))
    #                 result.set(a-i,b-j,image.get(a+i,b+j))
    #                 result.set(a+i,b+j,image.get(a-i,b-j))
    # return result


def main():
    # -----
    # You can try any of the following images.
    image_path = './images/minion.png'
    # image_path = './images/neobjuggi.png'
    # -----

    image = load_picture(image_path)

    # -----
    # You can try any other integer values for a and b.

    a, b = 70, 90

    # -----

    reflected_image = reflect_image(image, a, b)
    reflected_image.show()


if __name__ == '__main__':
    main()

# #### MOving hubo to a reflecting point
from cs1robots import *
import cs1robots

# ----------------------------------------
# Do not modify here!
_world = cs1robots._world
hubo = None
x = 0


# -----------------------------------------

# Hubo named `hubo` is already created in main(). You must not create a robot again!

# You can define your own function here to be used in reflect_hubo()
def line_movement():
    global x
    while hubo.front_is_clear():
        if hubo.on_beeper():
            x = 1
            break

        hubo.move()


def turn_right():
    for x in range(3):
        hubo.turn_left()


def edge_movement1():
    global x
    turn_right()
    if hubo.on_beeper():
        x = 1
    hubo.move()
    if hubo.on_beeper():
        x = 1
    turn_right()


def edge_movement2():
    global x
    hubo.turn_left()
    if hubo.on_beeper():
        x = 1
    hubo.move()
    if hubo.on_beeper():
        x = 1
    hubo.turn_left()


def one_round():  # Move in zigzag until hubo is on beeper
    global x
    while True:
        line_movement()
        if (x == 1):
            break
        if not hubo.right_is_clear():
            break
        edge_movement1()
        if (x == 1):
            break
        line_movement()
        if (x == 1):
            break
        if not hubo.left_is_clear():
            break
        edge_movement2()
        if (x == 1):
            break


def goto(x, y):
    initial_x, initial_y = (1, 1)
    if initial_x > x:
        hubo.turn_left()
        for i in range(initial_x - x):
            hubo.move()
        turn_right()
        hubo.turn_left()
    elif initial_x < x:
        turn_right()
        for i in range(x - initial_x):
            hubo.move()
        hubo.turn_left()
    if initial_y < y:
        for i in range(y - initial_y):
            hubo.move()
    elif initial_y > y:
        for i in range(2):
            hubo.turn_left()
        for i in range(initial_y - y):
            hubo.move()
        for i in range(2):
            hubo.turn_left()


def condition():  # when hubo is on beeper, stop there and give a location of beeper
    while not hubo.facing_north():
        hubo.turn_left()
    hubo.turn_left()
    count1 = 0
    while hubo.front_is_clear():
        hubo.move()
        count1 += 1

    hubo.turn_left()
    count2 = 0
    while hubo.front_is_clear():
        hubo.move()
        count2 += 1

    return count1, count2


def size():  # Get the size of the world(w,h)
    while not hubo.facing_north():
        hubo.turn_left()
    count3 = 0
    while hubo.front_is_clear():
        hubo.move()
        count3 += 1
    turn_right()
    count4 = 0
    while hubo.front_is_clear():
        hubo.move()
        count4 += 1
    while not hubo.facing_north():
        hubo.turn_left()
    for i in range(2):
        hubo.turn_left()
        while hubo.front_is_clear():
            hubo.move()
    print(count4, count3)
    return count4, count3


def reflect_hubo():
    hubo.set_trace('blue')
    hubo.set_pause(0)

    hubo.turn_left()
    one_round()
    x, y = condition()
    count4, count3 = size()

    while not hubo.facing_north():
        hubo.turn_left()

    if 2 * x + 1 <= count4 + 1 and 2 * y + 1 <= count3 + 1:
        goto(2 * x + 1, 2 * y + 1)
    else:
        goto(count4 + 1, count3 + 1)

    while not hubo.facing_north():
        hubo.turn_left()

    hubo.turn_left()
    print('w:', count4 + 1, 'h:', count3 + 1)


###################################
# Implement here

#####################################


# ----------------------------------------
# Do not modify main()!!
def main():
    if cs1robots._world == None:
        load_world('worlds/world4.wld')  # you can modify this to test another world
    global hubo
    hubo = Robot(avenue=1, street=1, orientation='E')
    reflect_hubo()


if __name__ == "__main__":
    main()
# ------------------------------------------













