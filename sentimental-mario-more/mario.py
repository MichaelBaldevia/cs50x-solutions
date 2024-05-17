# TODO
from cs50 import get_int

while True:
    pyramid_height = get_int("How High is the pyramid ")
    if pyramid_height > 0 and pyramid_height < 9:
        break


for x in range(pyramid_height):

    #print left spaces
    spaces = pyramid_height - 1
    while spaces > x:
        print(" ", end="")
        spaces -=1

    #print left pyramid
    left_pyramid = 0
    while left_pyramid <= x:
        print("#", end="")
        left_pyramid += 1

    #print gap
    print("  ", end="")

    #print right pyramid
    right_pyramid = 0
    while right_pyramid <= x:
        print("#", end="")
        right_pyramid += 1

    #print Next Line
    print("")