import cv2

import sys_logging

# Read image
img = cv2.imread('original.jpg', -1)
sys_logging.info(type(img))

while True:
    # Show image
    cv2.imshow('image', img)
    # Show until press close button
    key = cv2.waitKey(20)
    sys_logging.info(key)

    if key == 27:
        break
    elif key == ord('s'):
        cv2.imwrite('copy.jpg', img)
        break

cv2.destroyAllWindows()
