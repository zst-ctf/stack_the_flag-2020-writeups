from PIL import Image
import os
import matplotlib.pyplot as plt
import numpy as np
import time

 # RGBA colors
black = (0, 0, 0, 255)
white = (255, 255, 255, 255)
red = (255, 0, 0, 255)
green = (0, 255, 0, 255)
blue = (0, 0, 255, 255)

def put_1bit_color(im, x, y, bool_color):
    im.putpixel((x, y), white if bool_color else black)

def insert_format(im, fmt):
    '''top left vertical'''
    put_1bit_color(im, 8, 0, fmt[0] == '1')
    put_1bit_color(im, 8, 1, fmt[1] == '1')
    put_1bit_color(im, 8, 2, fmt[2] == '1')
    put_1bit_color(im, 8, 3, fmt[3] == '1')
    put_1bit_color(im, 8, 4, fmt[4] == '1')
    put_1bit_color(im, 8, 5, fmt[5] == '1')
    #
    put_1bit_color(im, 8, 7, fmt[6] == '1')
    put_1bit_color(im, 8, 8, fmt[7] == '1')

    '''top left horizontal'''
    put_1bit_color(im, 0, 8, fmt[14] == '1')
    put_1bit_color(im, 1, 8, fmt[13] == '1')
    put_1bit_color(im, 2, 8, fmt[12] == '1')
    put_1bit_color(im, 3, 8, fmt[11] == '1')
    put_1bit_color(im, 4, 8, fmt[10] == '1')
    put_1bit_color(im, 5, 8, fmt[9] == '1')
    #
    put_1bit_color(im, 7, 8, fmt[8] == '1')

    '''top right vertical'''
    put_1bit_color(im, 28, 8, fmt[0] == '1')
    put_1bit_color(im, 27, 8, fmt[1] == '1')
    put_1bit_color(im, 26, 8, fmt[2] == '1')
    put_1bit_color(im, 25, 8, fmt[3] == '1')
    put_1bit_color(im, 24, 8, fmt[4] == '1')
    put_1bit_color(im, 23, 8, fmt[5] == '1')
    put_1bit_color(im, 22, 8, fmt[6] == '1')
    put_1bit_color(im, 21, 8, fmt[7] == '1')

    '''bottom left vertical'''
    put_1bit_color(im, 8, 28, fmt[14] == '1')
    put_1bit_color(im, 8, 27, fmt[13] == '1')
    put_1bit_color(im, 8, 26, fmt[12] == '1')
    put_1bit_color(im, 8, 25, fmt[11] == '1')
    put_1bit_color(im, 8, 24, fmt[10] == '1')
    put_1bit_color(im, 8, 23, fmt[9] == '1')
    put_1bit_color(im, 8, 22, fmt[8] == '1')

fmt_list = '''
111011111000100
111001011110011
111110110101010
111100010011101
110011000101111
110001100011000
110110001000001
110100101110110
101010000010010
101000100100101
101111001111100
101101101001011
100010111111001
100000011001110
100111110010111
100101010100000
011010101011111
011000001101000
011111100110001
011101000000110
010010010110100
010000110000011
010111011011010
010101111101101
001011010001001
001001110111110
001110011100111
001100111010000
000011101100010
000001001010101
000110100001100
000100000111011
'''.strip().splitlines()

def main_fmtloop():
    from pyzbar import pyzbar
    # pip3 install -t .pip pyzbar
    # sudo apt install zbar-tools -y

    imagePath = 'qr.png'
    im = Image.open(imagePath)

    # loop through all formats
    for i, fmt in enumerate(fmt_list):
        print(f'{i+1} of {len(fmt_list)}:', fmt)
        insert_format(im, fmt)

        #im_array = np.asarray(im)
        #plt.imshow(im_array)
        #plt.show()

        results = pyzbar.decode(im)
        if len(results):
            print(count, results)


def main_bruteforce():
    from pyzbar import pyzbar
    # pip3 install -t .pip pyzbar
    # sudo apt install zbar-tools -y

    imagePath = 'qr2.png'
    im = Image.open(imagePath)
    width, height = im.size
    #results = pyzbar.decode(im)

    red_pixels = []
    cnt = 0;
    width, height = im.size

    for x in range(width):
        for y in range(height):
            color = im.getpixel((x, y))
            if color == red:
                red_pixels.append((x,y))

    print("red_pixels:", len(red_pixels))

    numb_pixels = len(red_pixels)
    for count in range(2**numb_pixels):
        #print("Count:", count)
        for pi, px in enumerate(red_pixels):
            bool_color = count  & (1 << pi)
            im.putpixel(
                px, 
                white if bool_color else black
            )
        
        results = pyzbar.decode(im)
        if len(results):
            print(count, results)

    print("Done")


def main_makemask6():
    imagePath = 'qr.png'
    convert_im = Image.open(imagePath)
    mask_im = Image.open(imagePath)
    width, height = convert_im.size

    for x in range(width):
        for y in range(height):
            mask6 = (((x*y) % 2) + ((x*y) % 3)) % 2 == 0
            
            mask_im.putpixel(
                (x, y), 
                white if not mask6 else black
            )

            is_white = convert_im.getpixel((x, y)) != black
            if is_white:
                xor_mask = white if mask6 else black
            else:
                xor_mask = white if not mask6 else black
            convert_im.putpixel(
                (x, y),
                xor_mask
            )

    mask_im.save('mask6.png')
    convert_im.save('qr_mask6.png')


def main_decodedata():
    imagePath = 'qr.png'
    orig_im = Image.open(imagePath)

    imagePath = 'qr_mask6.png'
    im = Image.open(imagePath)

    imagePath = 'donttouch.png'
    donttouch_im = Image.open(imagePath)

    width, height = im.size


    # initial position,
    # skip the first 8 bits of encoding info
    y = 22
    x = 28
    direction = True # true is up
    weightage = 128
    had_processed = False

    data = [0x20]
    while True:
        # Process current ---------------------------------
        is_red_zone = donttouch_im.getpixel((x, y)) == red
        is_black = im.getpixel((x, y)) == black
        is_white = not is_black

        # matplotlib visuals
        if is_red_zone:
            orig_im.putpixel((x, y), red)
        elif is_black:
            orig_im.putpixel((x, y), blue)
        elif is_white:
            orig_im.putpixel((x, y), green)
        else:
            orig_im.putpixel((x, y), white)
        im_array = np.asarray(orig_im)

        progress = ''.join(map(chr, data))
        plt.clf()
        plt.title(progress)
        plt.imshow(im_array)
        plt.show(block=False)
        plt.pause(0.00001)


        if is_red_zone: #red_zone
            # do nothing
            had_processed = False

        else:
            if weightage == 128:
                print(f"({x},{y}) = {hex(data[-1])} = {chr(data[-1]).encode()}")
                data.append(0)
                # im_array = np.asarray(im)
                # plt.imshow(im_array)
                # plt.show()
            
            if is_black:
                pass
            else:
                data[-1] |= weightage

            #print(f"Index {x} {y} = {hex(data[-1])} = {chr(data[-1]).encode()}")

            had_processed = True
        
        # Next position -----------------------------------

        if direction == True:
            # if even column, next position is left 
            # if odd column, next position for up & right
            if (x % 2) == 0:
                next_x = x - 1
                next_y = y
            else:
                next_x = x + 1
                next_y = y - 1
        else:
            # if even column, next position is left 
            # if odd column, next position is down & right
            if (x % 2) == 0:
                next_x = x - 1
                next_y = y
            else:
                next_x = x + 1
                next_y = y + 1

        # ensure next position is valid
        if (next_y < 0):
            assert direction == True # up

            # change x to nearest even number
            if (next_x % 2 == 0):
                next_x -= 2
            else:
                next_x -= 1

            # bring y back into bounds
            next_y = 0

            # change direction
            direction = False # down

        elif (next_y >= height):
            assert direction == False # down

            # change x to nearest even number
            if (next_x % 2 == 0):
                next_x -= 2
            else:
                next_x -= 1

            # bring y back into bounds
            next_y = height - 1 

            # change direction 
            direction = True # up

        x = next_x
        y = next_y

        if had_processed:
            # next position is smaller weightage
            weightage //= 2
            if weightage < 1:
                weightage = 128
        else:
            # reached a red zone, no processing done
            # so don't change weightage
            pass

        if (x < 14):
            break

    print(progress)

if __name__ == '__main__':
    # main_fmtloop() # bruteforce format info
    # main_bruteforce() # bruteforce red part in qr2.png
    
    main_makemask6() # remove mask6 from qr.png
    main_decodedata() # decode data bits after removal of mask
