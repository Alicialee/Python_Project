
import sys
from VideoProcessing import *

def usage():
   print("python3 DrivingVideoAnalysis.py [evaluate|analyze] [video]")

if __name__=='__main__':
   args = sys.argv[1:]

   if (len(args) != 2):
      usage()

   ExecutionOption = args[0]
   InputVideoPath = args[1]

   videoProcessor = VideoProcessing(InputVideoPath)

   if ExecutionOption == 'evaluate':
       videoProcessor.evaluate()
   elif ExecutionOption == 'analyze':
       videoProcessor.analyze()
   else:
      usage()

   del videoProcessor