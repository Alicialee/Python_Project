import numpy as np

import cv2

import sys
import time


class AnalyzeProcessOfVideo:
    'Pure analyze video and brief show how we do extract features'

    # static method:
    @staticmethod
    def find_edge_from_video(input_video):
        face_cascade = cv2.CascadeClassifier('files/car3.xml')
        video = cv2.VideoCapture(input_video)

        start = time.time()

        # read video frame by frame

        count = 0
        while (True):

            ret, frame = video.read()
            original = frame
            # define range of yellow color in HSV
            lower_yellow = np.array([20, 100, 100], dtype=np.uint8)
            upper_yellow = np.array([30, 255, 255], dtype=np.uint8)

            lower_white = np.array([0, 90, 60], dtype=np.uint8)
            upper_white = np.array([10, 255, 255], dtype=np.uint8)

            # Convert BGR to HSV
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # Threshold the HSV image to get only yellow colors
            mask_Y = cv2.inRange(hsv, lower_yellow, upper_yellow)

            mask_W = cv2.inRange(hsv, lower_white, upper_white)

            X = []
            Y = []
            for i in range(len(mask_Y)):
                for j in range(len(mask_Y[i])):
                    if mask_Y[i][j] != 0:
                        #print(str(mask_Y[i][j]) + " not zero at position " + str(i) + "   " + str(j))
                        X.append(i)
                        Y.append(j)
            m, b = np.polyfit(X, Y, 1)
            cv2.line(frame, (0, int(-b/m)), (int(b), 0), (30, 255, 255), 4)
            #print("m " + str(m))
            #print("b " + str(b))

            r = 500.0 / mask_Y.shape[1]
            dim = (500, int(mask_Y.shape[0] * r))

            # perform the actual resizing of the image and show it
            resized = cv2.resize(mask_Y, dim, interpolation=cv2.INTER_AREA)
            cv2.imshow("ColorDetection_Yellow", resized)

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # edges =cv2.Canny(gray, 100, 200)
            edges = cv2.Canny(gray, 50, 150, apertureSize=3)

            lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
            print("Frame : " + str(count))
            for line in lines:
                for rho, theta in line:
                    a = np.cos(theta)
                    b = np.sin(theta)
                    x0 = a * rho
                    y0 = b * rho
                    x1 = int(x0 + 1000 * (-b))
                    y1 = int(y0 + 1000 * (a))
                    x2 = int(x0 - 1000 * (-b))
                    y2 = int(y0 - 1000 * (a))

                    #print(str(x1) + " " + str(y1))
                    #print(str(x2) + " " + str(y2))
                    if (theta > 0.9 and theta < 1.5 and rho > 0.8*len(mask_Y)):
                        pass
                        #cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            # cv2.imwrite('houghlines3.jpg', frame)

            r = 500.0 / frame.shape[1]
            dim = (500, int(frame.shape[0] * r))

            # perform the actual resizing of the image and show it
            resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
            #cv2.imshow("frame", resized)

            #cv2.imshow('frame1', frame)

            r = 500.0 / edges.shape[1]
            dim = (500, int(edges.shape[0] * r))

            # perform the actual resizing of the image and show it
            resized = cv2.resize(edges, dim, interpolation=cv2.INTER_AREA)

            #cv2.imshow('canny', resized)

            time.sleep(1)

            horizontal = len(frame[0])
            vertical = len(frame)

            # car detection.
            cars = face_cascade.detectMultiScale(frame, 1.1, 2)

            ncars = 0
            for (x, y, w, h) in cars:
                if x < 0.25 * horizontal or vertical - y < 0.3 * vertical or y < 0.2 * vertical:
                    continue
                else:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    ncars = ncars + 1
                    #print("x " + str(x) + " y " + str(y))
            # show result
            # cv2.imwrite("Result.jpg",frame)

            r = 500.0 / frame.shape[1]
            dim = (500, int(frame.shape[0] * r))

            # perform the actual resizing of the image and show it
            resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
            cv2.imshow('Lane&CarDetection', resized)

            count = count + 1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                breaktime.sleep(2)
