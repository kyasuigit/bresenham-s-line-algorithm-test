import operator
from PIL import Image


class graphicsWindow:

    def __init__(self, width=640, height=480):
        self.__mode = 'RGB'
        self.__width = width
        self.__height = height
        self.__canvas = Image.new(self.__mode, (self.__width, self.__height))
        self.__image = self.__canvas.load()

    def drawPoint(self, point, color):
        if 0 <= point[0] < self.__width and 0 <= point[1] < self.__height:
            self.__image[point[0], point[1]] = color

    def drawLine(self, point1, point2, color):

        firstPoint = [0, 0]
        firstPoint[0] = int(point1.get(0, 0))
        firstPoint[1] = int(point1.get(1, 0))
        self.drawPoint(firstPoint, color)

        lastPoint = [0, 0]
        lastPoint[0] = int(point2.get(0, 0))
        lastPoint[1] = int(point2.get(1, 0))

        deltaX = lastPoint[0] - firstPoint[0]

        deltaY = lastPoint[1] - firstPoint[1]

        if abs(deltaY) > abs(deltaX):
            temp = firstPoint[0]
            firstPoint[0] = firstPoint[1]
            firstPoint[1] = temp

            temp2 = lastPoint[0]
            lastPoint[0] = lastPoint[1]
            lastPoint[1] = temp2

        deltaX = lastPoint[0] - firstPoint[0]
        deltaY = lastPoint[1] - firstPoint[1]

        currentpoint = firstPoint

        print(currentpoint)

        p = 0
        for i in range(firstPoint[0], lastPoint[0]):
            if i == firstPoint[0]:
                p = 2 * deltaY - deltaX
            else:
                if p < 0:
                    p = p + 2 * deltaY
                else:
                    if currentpoint[1] < lastPoint[1]:
                        currentpoint[1] += 1
                    else:
                        currentpoint[1] = currentpoint[1] - 1
                    p = p + 2 * deltaY - 2 * deltaX

                if currentpoint[0] < lastPoint[0]:
                    currentpoint[0] += 1
                else:
                    currentpoint[0] = currentpoint[0] - 1
                self.drawPoint(currentpoint, color)

        # if 0 < m < 1:
        #     for i in range(int(firstPoint[0]), int(lastPoint[0])):
        #         if i == firstPoint[0]:
        #             p = 2 * yDelta - xDelta
        #         else:
        #             if p < 0:
        #                 p = p + 2 * yDelta
        #
        #             else:
        #                 p = p + 2 * yDelta - 2 * xDelta
        #                 currentPoint[1] += 1
        #
        #             currentPoint[0] += 1
        #             self.drawPoint(currentPoint, color)
        #
        # elif m > 1 or m < -1:
        #     for i in range(int(firstPoint[0]), int(lastPoint[0])):
        #         if i == firstPoint[0]:
        #             p = 2 * xDelta - yDelta
        #         else:
        #             if p < 0:
        #                 p = p + 2 * xDelta
        #
        #             else:
        #                 p = p + 2 * xDelta - 2 * yDelta
        #                 currentPoint[0] += 1
        #
        #             currentPoint[1] += 1
        #             self.drawPoint(currentPoint, color)

    def saveImage(self, fileName):
        self.__canvas.save(fileName)

    def showImage(self):
        self.__canvas.show()

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height
