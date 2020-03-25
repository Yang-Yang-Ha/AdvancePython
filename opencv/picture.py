import cv2

import sys_logging


def show_picture():
    # Read image
    img = cv2.imread('original.jpg', cv2.IMREAD_UNCHANGED)
    sys_logging.info(img.ndim)
    sys_logging.info(img.shape)
    sys_logging.info(img.dtype)
    while True:
        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        win = cv2.getWindowProperty('image', 0)
        # Show image
        cv2.imshow('image', img)
        # Show until press close button
        key = cv2.waitKey(20)

        if key == 27:
            break
        elif key == ord('s'):
            cv2.imwrite('copy.jpg', img)
            break
    cv2.destroyAllWindows()


if __name__ == '__main__':
    show_picture()
