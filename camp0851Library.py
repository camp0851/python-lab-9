# Imports
from gfxhat import lcd, backlight, fonts
from click import getchar
from PIL import Image, ImageFont, ImageDraw
import time
import math
import random

# Turns on the backlight
def setBacklight(r = 255, g = 255, b = 255):
    backlight.set_all(r, g, b)
    backlight.show()

# Clears the Screen
def clearScreen():
    lcd.clear()
    lcd.show()

# Displays Text
def displayText(text,lcd,x,y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show() 

# Checks to see if the given cordinates are valid

def areCordinatesValid(obj, x, y):
    width = len(obj[0])
    height = len(obj)

    if x + width < 127 and x > 0 and y + height < 63 and y > 0:
        return True
    else:
        return False

# Displays the Object on the Screen
def displayObject(obj, x, y):
    clearScreen()

    yPixel = y
    for line in obj:
        xPixel = x
        for pixel in line:
            lcd.set_pixel(xPixel, yPixel, pixel)
            xPixel = xPixel + 1
        yPixel = yPixel + 1
    lcd.show()


# Erases the Object
def erasebject(obj, x, y):

    yPixel = y
    for line in obj:
        xPixel = x
        for pixel in line:
            lcd.set_pixel(xPixel, yPixel, 0)
            xPixel = xPixel + 1
        yPixel = yPixel + 1
    lcd.show()

# Checks for Collision
def checkCollision(obj, x, y, vx, vy, Sx, Sy):
    width = len(obj[0])
    height = len(obj)
    if x + width >= Sx or x < 1:
        vx = vx - (2 * vx)
    if y + height >= Sy or y < 1:
        vy = vy - (2 * vy)
    return vx, vy

# Moves the Object
def moveObject(obj, x, y, vx, vy):
    run = 0
    while run < 200:
        x = x + vx
        y = y + vy
        vx = checkCollision(obj, x, y, vx, vy, 128, 64)[0]
        vy = checkCollision(obj, x, y, vx, vy, 128, 64)[1]
        displayObject(obj, x, y)
        run = run + 1
    return x, y

# Shut down the Program
def shutdown():
    print('Shutting down!')
    time.sleep(1)
    clearScreen()
    time.sleep(1)
    setBacklight(0, 0, 0)
    time.sleep(1)
    quit()