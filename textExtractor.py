import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
image=cv2.imread("download1.jpeg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(pytesseract.image_to_string(image,lang="eng"))