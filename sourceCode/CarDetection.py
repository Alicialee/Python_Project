import cv2

class CarDetection:
    'Car detection based on training data from files folder car3.xml'

    def __init__(self, face_cascade):
        self.face_cascade = face_cascade

    def detect(self, frame, carDetectionRsults):
        horizontal = len(frame[0])
        vertical = len(frame)

        # car detection.
        cars = self.face_cascade.detectMultiScale(frame, 1.1, 2)

        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            # ncars = ncars + 1
            # print("x " + str(x) + " y " + str(y))
            # ncars += 1

            # filter all noises, and only keep one valid car in front of my car

            if x < 0.25 * horizontal or vertical - y < 0.3 * vertical or y < 0.2 * vertical:
                continue
            else:
                carDetectionRsults.append(y/vertical)

