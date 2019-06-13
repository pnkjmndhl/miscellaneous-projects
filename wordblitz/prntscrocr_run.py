import pyautogui
from PIL import Image, ImageEnhance
import pytesseract
import time
import numpy as np
import pandas as pd
import os
import winsound


def change_contrast(img, level):
    factor = (259 * (level + 255)) / (255 * (259 - level))

    def contrast(c):
        return 128 + factor * (c - 128)

    return img.point(contrast)


def change_contrast_multi(img, steps):
    width, height = img.size
    canvas = Image.new('RGB', (width * len(steps), height))
    for n, level in enumerate(steps):
        img_filtered = change_contrast(img, level)
        canvas.paste(img_filtered, (width * n, 0))
    return canvas


screenshot_name = "screenshot.png"
screenshot_converted = "screenshot1.png"
screenshot_final = "screenshot2.png"

# run this program forever

while True:

    while True:

        # Take cropped screenshot
        pic = pyautogui.screenshot(region=(450, 400, 470, 450))
        pic.save(screenshot_name)
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

        # extract boxes and append all in x
        img = change_contrast(pic, 200)
        data = np.array(img)
        l = [51, 48]  # x,y of top left
        xx = 111
        yy = 110
        ltx = 40
        lty = 50
        a = []
        for j in range(4):
            for i in range(4):
                # print(l[1] + yy * j, l[1] + yy * j + lty, l[0] + xx * i, l[0] + xx * i + ltx)
                a.append(data[(l[1] + yy * j):(l[1] + yy * j + lty), (l[0] + xx * i):(l[0] + xx * i + ltx)])
        total_width = 640
        max_height = 50
        new_im = Image.new('RGB', (total_width, max_height))
        x_offset = 0
        for letter in a:
            img = Image.fromarray(letter.astype('uint8'))
            new_im.paste(img, (x_offset, 0))
            x_offset += img.size[0]

        #new_im.save('text.jpg')

        text = pytesseract.image_to_string(new_im)
        text = text.encode('ascii', 'ignore').decode('ascii')
        print "",
        if len(text) == 16:
            break
        # print "Text found: [{0}], re-running OCR".format(text)
    # text_file = open("string.txt", "w")
    # text_file.write(text)
    # text_file.close()
    print "Successful, finding words from dictionary..."

    print ("Calling wordblitz.")
    print ("python wordblitz.py {0}".format(text))
    winsound.Beep(2500, 20)
    os.system("python wordblitz.py {0}".format(text.lower()))
