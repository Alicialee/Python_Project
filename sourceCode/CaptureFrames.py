import cv2

class CaptureFrames:
    'Capture frames from videos'

    def __init__(self, inputVideo):
        self.videoName = inputVideo

    def capitureFramesFromVideo(self, skipNumFrames):
        frames = []
        video = cv2.VideoCapture(self.videoName)
        # start = time.time()
        count = 0
        while (True):
            ret, frame = video.read()
            if ret == True:
                if count % skipNumFrames == 0:
                    frames.append(frame)
                    print("Analyzing frame: " + str(count))
                count += 1
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
        return frames