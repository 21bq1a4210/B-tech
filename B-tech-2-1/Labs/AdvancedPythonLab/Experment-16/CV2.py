import sys
import cv2 as cv
img = cv.imread(r"F:\Betch-2\Betch-2-1\Labs\AdvancedPythonLab\Experment-15\result.png")
if img is None:
 sys.exit("Could not read the image.")
cv.imshow("Image",img)
cv.waitKey(10000)
cv.destroyAllWindows()