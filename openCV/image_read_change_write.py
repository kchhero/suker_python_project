import cv2

fname = 'lena.jpg'

gray = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)

cv2.imshow('Gray', gray)
cv2.imwrite('lena_gray.jpg', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
