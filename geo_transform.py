# resize #
import cv2 as cv

img = cv.imread('temp.png')
res = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC) 

# make a output file
cv.imwrite('output.png', img)





# translation #
import cv2 as cv
import numpy as np

img = cv.imread('temp.png')

M = np.float32([[1, 0, 30], [0, 1, 50]]) # warpAffine only accept matrix with (rows=2, cols=3) and float32/float64
dst = cv.warpAffine(img, M, (cols, rows))

# show the output image on screen
cv.imshow('img', dst)
cv.waitKey(0)
cv.destroyAllWindows()





# rotation #
import cv2 as cv

img = cv.imread('temp.png')
rows, cols, channels = img.shape

M = cv.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0), 90, 0.5) # (centre coordinate of rotation, counter-clockwise, scale)
dst = cv.warpAffine(img, M, (cols, rows))

cv.imshow('img', dst)
cv.waitKey(0)
cv.destroyAllWindows()




# affine transformation #
import cv2 as cv
import numpy as np

img = cv.imread('temp.png')
rows, cols, channels = img.shape

pt1 = np.float32([[50, 50], [200, 50], [50, 200]])
pt2 = np.float32([[10, 100], [200, 50], [100, 250]])

M = cv.getAffineTransform(pt1, pt2) # require three points

dst = cv.warpAffine(img, M, (cols, rows))

cv.imshow('img', img)
cv.imshow('img_new', dst)
cv.waitKey(0)
cv.destroyAllWindows()




# perspective transformation #
import cv2 as cv
import numpy as np

img = cv.imread('temp.png')
rows, cols, channels = img.shape

pt1 = np.float32([[(rows-1)/4, (cols-1)/4], [(rows-1)/4*3, (cols-1)/4], [(rows-1)/4, (cols-1)/4*3], [(rows-1)/4*3, (cols-1)/4*3]])
pt2 = np.float32([[0, 0], [rows, 0], [0, cols], [rows, cols]])

M = cv.getPerspectiveTransform(pt1, pt2) # requires four points

dst = cv.warpPerspective(img, M, (cols, rows))

cv.imshow('img_new', dst)
cv.waitKey(0)
cv.destroyAllWindows()
