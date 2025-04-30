import cv2
import numpy as np

class EdgeDetectorApp:
    def __init__(self, cap):
        self.cap = cap
        self.sigma = 1.0
        self.mode = 'original'

    def apply_filters(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (0, 0), self.sigma)

        if self.mode == 'original':
            return frame
        elif self.mode == 'sobel_x':
            sobelx = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=5)
            return cv2.convertScaleAbs(sobelx)
        elif self.mode == 'sobel_y':
            sobely = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=5)
            return cv2.convertScaleAbs(sobely)
        elif self.mode == 'magnitude':
            sobelx = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=5)
            sobely = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=5)
            magnitude = cv2.magnitude(sobelx, sobely)
            return cv2.convertScaleAbs(magnitude)
        elif self.mode == 'sobel_threshold':
            sobelx = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=5)
            sobely = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=5)
            magnitude = cv2.magnitude(sobelx, sobely)
            _, thresh = cv2.threshold(magnitude, 100, 255, cv2.THRESH_BINARY)
            return cv2.convertScaleAbs(thresh)
        elif self.mode == 'laplacian':
            laplacian = cv2.Laplacian(blurred, cv2.CV_64F)
            return cv2.convertScaleAbs(laplacian)
        else:
            return frame

    def release(self):
        if self.cap is not None and self.cap.isOpened():
            self.cap.release()
