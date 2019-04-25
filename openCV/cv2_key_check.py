import cv2

fname = 'lena.jpg'

img = cv2.imread(fname, cv2.IMREAD_COLOR)

cv2.imshow('Original', img)

k = cv2.waitKey(0)
if k == ord('a') :  # if input 'a' key
    print("a")

print("key = %s" % str(k))
print("ascii = %s" % unichr(k))

cv2.destroyAllWindows()
