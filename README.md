# Real-Time Face Blurring with OpenCV README

## Introduction

This repository contains Python code for a real-time face blurring application using OpenCV. Two scripts are provided, each demonstrating a different level of face anonymization.
Video Demo:
```bash
https://youtu.be/wRvz-0KSUJk
```
### Code 1 - Face Detection and Outline

The first script detects faces in a webcam feed and outlines them with random-colored rectangles.

### Code 2 - Face Blurring

The second script builds upon the first by not only detecting faces but also applying a Gaussian blur to anonymize them in real-time.

## Prerequisites

- Ensure you have OpenCV installed. You can install it using:

  ```bash
  pip install opencv-python
  ```

- Download the Haar Cascade XML file for face detection and place it in the same directory as the script. You can find it [here](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml).

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/real-time-face-blurring.git
   cd real-time-face-blurring
   ```

2. Download the Haar Cascade XML file and place it in the same directory.

3. Run the desired script:

   ```bash
   python face_detection.py
   ```

   or

   ```bash
   python face_blurring.py
   ```

4. Press the spacebar to exit the application.

## Code Explanation

- Both scripts use OpenCV to capture frames from the webcam and detect faces.
- The first script outlines detected faces with random-colored rectangles.
- The second script takes face regions, applies Gaussian blur, and substitutes the original frames with blurred faces.

## Note

- Experiment with different Haar Cascade XML files for specialized object detection.
- Customize the blur parameters or color schemes to fit your requirements.
- Ensure you have the necessary permissions and adhere to legal and ethical guidelines when using or modifying this code.

Feel free to explore, modify, and integrate this code into your projects! If you have any questions or suggestions, feel free to leave a comment.

Happy coding! 🚀✨
