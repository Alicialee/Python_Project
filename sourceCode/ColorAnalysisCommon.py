import cv2
from AreaRatioDetectionCommon import *
import numpy as np

class ColorAnalysisCommon:
    'common class for color area detection'

    # static method:
    @staticmethod
    def findColorLinesAreaRatio(frame, lower_color, upper_color):
        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Threshold the HSV image to get only yellow colors
        mask = cv2.inRange(hsv, lower_color, upper_color)

        X = []
        Y = []
        for i in range(len(mask)):
            for j in range(len(mask[i])):
                if mask[i][j] != 0:
                    # print(str(mask[i][j]) + " not zero at position " + str(i) + "   " + str(j))
                    X.append(i)
                    Y.append(j)
        #print(X)
        #print(Y)
        if len(X) == 0 or len(Y) == 0:
            return 0
        else:
            m, b = np.polyfit(X, Y, 1)
            # cv2.line(mask, (0, int(b)), (1, int(m+b)), (0, 0, 255), 2)
            # print("m " + str(m))
            # print("b " + str(b))

            # Bitwise-AND mask and original image
            res = cv2.bitwise_and(frame, frame, mask=mask)

            # cv2.imshow('mask', mask)
            # cv2.imshow('res', res)
            # time.sleep(1)
            return AreaRatioDetectionCommon.calculateAreaRatio(mask, m, b)