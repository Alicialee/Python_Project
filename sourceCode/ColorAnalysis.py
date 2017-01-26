import numpy as np
from ColorAnalysisCommon import *

class ColorAnalysis:
    'Provide color detection and area ratio detection features'

    def __init__(self, frame):
        self.frame = frame

    def findYellowLinesAreaRatio(self):
        # define range of yellow color in HSV
        lower_yellow = np.array([20, 100, 100], dtype=np.uint8)
        upper_yellow = np.array([30, 255, 255], dtype=np.uint8)

        return ColorAnalysisCommon.findColorLinesAreaRatio(self.frame, lower_yellow, upper_yellow)

    def findWhiteLinesAreaRatio(self):
        # define range of yellow color in HSV
        lower_white = np.array([0, 90, 60], dtype=np.uint8)
        upper_white = np.array([10, 255, 255], dtype=np.uint8)

        return ColorAnalysisCommon.findColorLinesAreaRatio(self.frame, lower_white, upper_white)