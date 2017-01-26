# Python_Project

Introduction:

This project introduces a new approach to evaluate driving performance from video images captured in moving vehicles. It used a divide-and-conquer strategy to divide the system into multi-tasks. Based on the results from different tasks, combine them together and evaluate the final driving performance. Canny edge detection algorithms, color analysis are used to find candidate edges in video frames. 2D features analyze in 3D frame by frame system. To compare the performance of the driver, it evaluates the consistency of driving, stable of driving, distance to the surrounded vehicles, different actions are being made in different situations (e.g. Traffic Sign ahead)
Input: driving video (process/analyze frame by frame)
Output: perfomance rating score

Set up Python3.5 environment for the OpenCV Compilation on MacOSX:

1. Install Xcode
2. Setup Homebrew
3. Install Python3
4. Install virtualenv and virtualenwrapper:use pip3 install then create cv3 virtual environment that OpenCv will use to compile python3.5 bindings against.
5. Install OpenCV prerequisites: use command brew install cmake pkg-config to compile OpenCV from source
6. Compile OpenCV 3.1: use git clone https://github.com/Itseez/opencv.git then cd openCV, git checkout 3.1.0
7. create build directory
8. use CMake to configure the build

