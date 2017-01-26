class EvaluateResults:
    'provide set of static methods to evaluate results from color analysis and car analysis.'

    # static method:
    @staticmethod
    def evaluateDrivingBalance(areaRatioList):
        avr = sum(areaRatioList) / float(len(areaRatioList))
        squareDiff = 0
        for areaRatio in areaRatioList:
            squareDiff += (areaRatio - avr) * (areaRatio - avr)

        squareDiff = squareDiff / len(areaRatioList)
        if squareDiff < 0.01:
            return 100
        elif squareDiff < 0.05:
            return 90
        elif squareDiff < 0.1:
            return 80
        elif squareDiff < 1:
            return 60
        else:
            return 40

    # static method:
    @staticmethod
    def evaluateCarDistance(carDetectionResults):
        numOfResults = len(carDetectionResults)
        threshold = 2
        if numOfResults/10 > 2:
            threshold = numOfResults

        count1 = 0
        count2 = 0
        count3 = 0
        # set a threshold in case of abnormal noise from one or two frames

        #In each frame, car to camera distance/camera horizontal scope
        #since camera angle is fixed and camera height is fixed
        #we assume the road is in horizontal,
        #for our iphone camera, the estimated horizontal distance is 500ft
        #If the car is 500ft*0.10= 50ft in highway, we consider it is very dangerous in highway driving
        for ratio in carDetectionResults:
            if ratio < 0.10:
                count1 += 1
                if count1 > threshold:
                    return 40
            elif ratio < 0.15:
                count2 += 1
                if count2 > threshold:
                    return 60
            elif ratio < 0.25:
                count3 += 1
                if count3 > threshold:
                    return 80
        return 100

