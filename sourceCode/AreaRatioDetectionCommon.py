class AreaRatioDetectionCommon:
    'common class for calculating area ratio'

    # static method:
    @staticmethod
    def calculateAreaRatio(mask, m, b):

        areaRatio = 1

        x = len(mask)
        y = len(mask[0])

        if b < 0:
            if -b / m < 0:
                raise RuntimeError("couldn't find area ratio because line regression is wrong")
            else:
                if (y - b) / m <= x:
                    area = y * (-b / m + (y - b) / m) / 2
                    areaRatio = area / (x * y)
        elif b < y:
            if -b / m < 0:
                if (y - b) / m <= x:
                    area = (y - b) * (y - b) / (2 * m)
                    areaRatio = area / (x * y)
                else:
                    area = ((y - b) + (y - m * x - b)) * x / 2
                    areaRatio = area / (x * y)
                    # print(" ar" + str(area) + " " + str(y -m*x - b))
            else:
                if -b / m < x:
                    area = b * (-b / m) / 2
                    areaRatio = 1 - area / (x * y)
                else:
                    area = (m * x + b + b) * x / 2
                    areaRatio = 1 - area / (x * y)
        else:
            if -b / m < x:
                area = ((y - b) / m - b / m) * y / 2
                areaRatio = 1 - area / (x * y)
            else:
                area = (x - (y - b) / m) * (y - (m * x + b)) / 2
                areaRatio = area / (x * y)
        if areaRatio < 0 or areaRatio > 1:
            print("x " + str(x) + " y " + str(y) + " -b/m " + str(-b / m) + " y-b/m " + str((y - b) / m))
            print(areaRatio)
            raise RuntimeError("Error in calculating area ratio")
        return areaRatio
