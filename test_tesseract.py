import pytesseract
import cv2

# # If you don't have tesseract executable in your PATH, include the following:
# pytesseract.pytesseract.tesseract_cmd = r'D:/Programme/tesseract/tesseract'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

img2 = cv2.imread('sh.png',)
print(pytesseract.image_to_string(img2))
