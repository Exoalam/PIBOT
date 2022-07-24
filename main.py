# import the necessary packages
from imutils import paths
import numpy as np
import imutils
import cv2


cap = cv2.VideoCapture("http://10.42.0.173:4747/video")
def find_marker(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)
    edged = cv2.Canny(gray, 35, 200)
    cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key = cv2.contourArea)
    return cv2.minAreaRect(c)


def distance_to_camera(knownWidth, focalLength, perWidth):
	return (knownWidth * focalLength) / perWidth


if __name__ == '__main__':
    ret, image = cap.read()
    KNOWN_DISTANCE = 12.0
    KNOWN_WIDTH = 4.0
    marker = find_marker(image)
    focalLength = 600
    while True:
        ret, image = cap.read()
        marker = find_marker(image)
        inches = distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])
        # draw a bounding box around the image and display it
        box = cv2.cv.BoxPoints(marker) if imutils.is_cv2() else cv2.boxPoints(marker)
        box = np.int0(box)
        cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
        cv2.putText(image, "%.2fft" % (inches/12),
                    (image.shape[1] - 200, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
                    2.0, (0, 255, 0), 3)
        cv2.imshow("image", image)
        if cv2.waitKey(1) == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
