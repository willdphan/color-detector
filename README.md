# Color Detector

The provided code uses `OpenCV` and the `PIL` library to detect a specified color in real-time through the camera feed.

It captures the video, transforms it into the HSV colorspace, and detects regions with the target color, marking them with a bounding box.

## Features

**Color Detector Class**

Organized for easier reuse and integration into other projects.

Detects a specified color and draws a bounding box around it.

Modular design for better adaptability.

[Module](face-detector-module.py)
<br/>

**Simple Script**

A streamlined version for direct color detection on the video feed without the class structure.

[Script](face-detector.py)
<br/>

**Usage**

Install the required libraries:

`pip install opencv-python Pillow`

To use the ColorDetector class:

`python color-detector-module.py`

For the simple script:

`python color-detector-script.py`

---

## Note

Ensure you have a working camera and that the necessary permissions are granted to access the camera feed. Adjust the `cap = cv2.VideoCapture(1)` parameter depending on which camera you want to use. Modify the yellow variable or pass other BGR color values to detect different colors.

---

## License

This script is open-source and licensed under the MIT License. For more details, check the [LICENSE](LICENSE) file.
