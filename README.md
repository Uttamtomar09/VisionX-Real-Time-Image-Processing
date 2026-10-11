# VisionX — Real-Time Image Processing

A Python and OpenCV project that performs real-time image processing using a webcam.

## Features
- Live webcam access
- Original image display
- Grayscale conversion
- Gaussian blur
- Canny edge detection
- Face detection with bounding boxes and face count
- Save captured images

## Technologies Used
- Python
- OpenCV
- NumPy

## How to Run
1. Install Python.
2. Install the required packages:
   `pip install opencv-python numpy`
3. Run the application:
   `python main.py`
4. Use the keyboard controls shown in the camera window.

## Keyboard Controls
- `1` — Original image
- `2` — Grayscale
- `3` — Blur
- `4` — Edge detection
- `5` — Face detection
- `S` — Save image
- `Q` — Exit

**Note:** A working webcam is required. Face detection also requires the Haar Cascade XML file if it is loaded from a local path.
