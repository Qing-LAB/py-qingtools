import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../resources/02.tif', 0)

# global threshold
ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Otsu's thresholding
ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(img, (5, 5), 0)
ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# plot all the images and their histograms
images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]
titles = ['Original Noisy Image', 'Histogram', 'Global Thresholding (v=127)',
          'Original Noisy Image', 'Histogram', "Otsu's Thresholding",
          'Gaussian filtered Image', 'Histogram', "Otsu's Thresholding"]

for i in range(3):
    plt.subplot(3, 3, i * 3 + 1), plt.imshow(images[i * 3], 'gray')
    plt.title(titles[i * 3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i * 3 + 2), plt.hist(images[i * 3].ravel(), 256)
    plt.title(titles[i * 3 + 1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i * 3 + 3), plt.imshow(images[i * 3 + 2], 'gray')
    plt.title(titles[i * 3 + 2]), plt.xticks([]), plt.yticks([])
plt.show()

_, ct0, hi = cv2.findContours(img.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
ct = [cv2.approxPolyDP(cnt, 3, True) for cnt in ct0]


def update(levels):
    h, w = img.shape[:2]
    vis = np.zeros((h, w, 3), np.uint8)
    levels = levels - 3
    cv2.drawContours(vis, ct, (-1, 2)[levels <= 0], (128, 255, 255),
                     3, cv2.LINE_AA, hi, abs(levels))
    cv2.imshow('contours', vis)


update(3)
cv2.createTrackbar("levels+3", "contours", 3, 255, update)
cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
