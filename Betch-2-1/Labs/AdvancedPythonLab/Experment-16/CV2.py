import sys
img_path=input("enter img path:")
img = cv.imread(img_path)
if img is None:
 sys.exit("Could not read the image.")
cv.imshow("Image",img)
cv.waitKey(10000)
cv.destroyAllWindows()
