import cv2
from PIL import Image
from utils import get_limits

class ColorDetector:
    def __init__(self, color):
        self.color = color
        self.cap = cv2.VideoCapture(1)

    def detect(self):
        while True:
            ret, frame = self.cap.read()

            hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            lowerLimit, upperLimit = get_limits(color=yellow)

            mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

            mask_ = Image.fromarray(mask)

            bbox = mask_.getbbox()

            if bbox is not None:
                x1, y1, x2, y2 = bbox
                
                # rectangle
                frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    yellow = [0, 255, 255]  # yellow in BGR colorspace
    detector = ColorDetector(yellow)
    detector.detect()
