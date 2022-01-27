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
        x1 = int(point1.get(0, 0))
        y1 = int(point1.get(1, 0))

        self.drawPoint([x1, y1], color)

        x2 = int(point2.get(0, 0))
        y2 = int(point2.get(1, 0))

        x_delta = x2-x1
        y_delta = y2-y1

        abs_x_delta = abs(x_delta)
        abs_y_delta = abs(y_delta)

        if abs_x_delta > abs_y_delta:
            p = 2 * abs_x_delta - abs_x_delta
            for i in range(0, abs_x_delta+1):
                if p < 0:
                    p = p + 2 * abs_y_delta
                else:
                    if y_delta < 0:
                        y1 -= 1
                    else:
                        y1 += 1
                    p = p + 2 * abs_y_delta - 2 * abs_x_delta
                if x_delta < 0:
                    x1 -= 1
                else:
                    x1 += 1
                self.drawPoint([x1, y1], color)

        else:
            p = 2 * abs_y_delta - abs_x_delta
            for i in range (0, abs_y_delta+1):
                if p < 0:
                    p = p + 2 * abs_x_delta
                else:
                    if x_delta < 0:
                        x1 -= 1
                    else:
                        x1 += 1
                    p = p + 2 * abs_x_delta - 2 * abs_y_delta

                if y_delta < 0:
                    y1 -= 1
                else:
                    y1 +=1
                self.drawPoint([x1, y1], color)

    def saveImage(self, fileName):
        self.__canvas.save(fileName)

    def showImage(self):
        self.__canvas.show()

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height
