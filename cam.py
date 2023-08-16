import cv2
from PIL import Image

from utils import get_limits

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Continuous display; press 'q' to exit
        break

cap.release()

cv2.destroyAllWindows()
