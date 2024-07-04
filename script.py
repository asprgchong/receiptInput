import cv2 
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'
img = cv2.imread('/Users/geralynchong/receiptInput/image1.png')

# Adding custom options
custom_config = r'--oem 3 --psm 6'
print(pytesseract.image_to_string(img, config=custom_config))


