import cv2
from matplotlib import pyplot as plt

fname = 'lena.jpg'

img = cv2.imread(fname, cv2.IMREAD_COLOR)

# openCV use BGR, Matplotlib use RGB, so b and r switch location
b, g, r = cv2.split(img)

print("b ==>")
print(b)
print("g ==>")
print(g)
print("r ==>")
print(r)

img2 = cv2.merge([r, g, b])

plt.imshow(img2)

plt.xticks([])
plt.yticks([])
plt.show()
