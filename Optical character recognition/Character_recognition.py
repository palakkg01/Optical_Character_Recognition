import cv2
import pytesseract
import numpy as np



#Open the image that is to be converted to text
input_img = cv2.imread('C:\\Users\\Aka\\Desktop\\Optical character recognition\\Input images\\image3.jpg')


gray_var = cv2.cvtColor(input_img, cv2.COLOR_RGB2GRAY)
gray_var, img_bin = cv2.threshold(gray_var,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
gray_var = cv2.bitwise_not(img_bin)


s_Arr = np.ones((2, 1), np.uint8)
# It returns a new array of given shape and type, filled with ones


input_img = cv2.erode(gray_var, s_Arr, iterations=1)
#It performs erosion on the image



input_img = cv2.dilate(input_img, s_Arr, iterations=1)
#It is used to detach two connected objects etc.



pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\Aka\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'
#Path of tesseract.exe 


char_output = pytesseract.image_to_string(input_img)
#tesseract extracts the text from input image and stores in char_output as a string


print("RESULT:",char_output)
#output is displayed
    







#                                           #THANK YOU!