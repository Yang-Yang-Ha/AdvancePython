import argparse

import cv2

parse = argparse.ArgumentParser()
parse.add_argument('--path', help='please input video path')
args = parse.parse_args()
print(args.path)

video = cv2.VideoCapture(args.path)
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (1080, 720))
while video.isOpened():
    ret, frame = video.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('video', gray)
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
out.release()
cv2.destroyAllWindows()
