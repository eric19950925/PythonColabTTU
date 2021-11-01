import os
import cv2 as cv
import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r'd:\OCR\tesseract.exe'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

def recognize_text(image):
    #  edge preserving filter denoising 
    dst = cv.pyrMeanShiftFiltering(image, sp=10, sr=150)
    #  grayscale image 
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    #  binarization 
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    #  morphological manipulation corrosion    expansion 
    erode = cv.erode(binary, None, iterations=2)
    dilate = cv.dilate(erode, None, iterations=1)
    cv.imshow('dilate', dilate)
    #  logical operation makes the background white    the font is black for easy recognition. 
    cv.bitwise_not(dilate, dilate)
    cv.imshow('binary-image', dilate)
    #  identify 
    test_message = Image.fromarray(dilate)
    text = pytesseract.image_to_string(test_message)
    #  print(text)
    f = open('output.txt', 'w')
    print(text, file=f)
    f.close()


# src = cv.imread('thsr_captcha.png')
# https://github.com/eric19950925/PythonColabTTU/blob/main/class_pyautogui/captcha_bot.py

src = cv.imread('example.png')
cv.imshow('input image', src)
recognize_text(src)
os.startfile('output.txt')
cv.waitKey(0)
cv.destroyAllWindows()
