import cv2
from CaptureFrames import *
from ColorAnalysis import *
from EvaluateResults import *
from CarDetection import *
from AnalyzeProcessOfVideo import *
class VideoProcessing(object):
   'Provide two options to process input video: 1. evaluate(return scoring) 2. analyze(return video processing details)'
   def __init__(self, inputVideo):
      self.videoName = inputVideo

   def analyze(self):
       AnalyzeProcessOfVideo.find_edge_from_video(self.videoName)

   def evaluate(self):

       captureFrames = CaptureFrames(self.videoName)
       frames = captureFrames.capitureFramesFromVideo(50)
       del captureFrames

       areaRatioListYellowLines = []
       areaRatioListWhiteLines = []
       areaRatioListHoughLines = []
       carDetectionRsults = []

       face_cascade = cv2.CascadeClassifier('files/car3.xml')
       carDetector = CarDetection(face_cascade)

       for frame in frames:
           colorProcessor = ColorAnalysis(frame)
           areaRatio = colorProcessor.findYellowLinesAreaRatio()
           areaRatioListYellowLines.append(areaRatio)

           areaRatio = colorProcessor.findWhiteLinesAreaRatio()
           areaRatioListWhiteLines.append(areaRatio)

           carDetector.detect(frame, carDetectionRsults)
           # areaRatio = findHoughLinesAreaRatio(frame)
           # areaRatioListHoughLines.append(areaRatio)
       ScoreWiteLane = EvaluateResults.evaluateDrivingBalance(areaRatioListWhiteLines)
       ScoreYellowLane = EvaluateResults.evaluateDrivingBalance(areaRatioListYellowLines)
       ScoreCarDetection = EvaluateResults.evaluateCarDistance(carDetectionRsults)

       pureName = self.videoName.split('.')[0]
       text_file = open(pureName + "_result.txt", "w")

       text_file.write("Driving balance score from white lane: " + str(ScoreWiteLane) + "\n")
       text_file.write("Driving balance score from yellow lane: " + str(ScoreYellowLane) + "\n")
       text_file.write("Driving safety score from car detection: " + str(ScoreCarDetection) + "\n")
       text_file.close()
       if ScoreWiteLane == 100 or ScoreYellowLane == 100:
           print("Driving Balance: Excellent")
       elif ScoreWiteLane > 90 or ScoreYellowLane > 90:
           print("Driving Balance: Good")
       elif ScoreWiteLane > 80 or ScoreYellowLane > 80:
           print("Driving Balance: Average")
       else:
           print("Driving Balance: Fair")

       if ScoreCarDetection == 100:
           print("Driving Safety: Excellent")
       elif ScoreCarDetection > 90:
           print("Driving Safety: Good")
       elif ScoreCarDetection > 80:
           print("Driving Safety: Average")
       else:
           print("Driving Safety: Fair")
       # print("Driving balance score from hough line: " + str(evaluateDrivingBalance(areaRatioListHoughLines)))
