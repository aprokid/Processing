from math import sqrt 

class Distance:
    def __init__(self, point1x, point1y, point2x, point2y):
        self.point1x = point1x
        self.point1y = point1y
        self.point2x = point2x
        self.point2y = point2y
        
    def _euclidean_distance(self):
        return sqrt((self.point1x - self.point2x)**2 + (self.point1y - self.point2y)**2)
        
        
    def _city_block(self):
        return abs(self.point1x - self.point2x) + abs(self.point1y - self.point2y)
        
        
    def _chessboard_distance(self):
        if self.point1x == self.point2x:
            return abs(self.point1y - self.point2y)
        d = 0
        newx = self.point1x
        while abs(self.point2x - newx) != abs(self.point2y - self.point1y):
            if self.point1x < self.point2x:
                newx += 1
            else:
                newx -= 1
            d += 1
        d += sqrt(2)*abs(self.point2x - newx)
        return d
        
        
dis = Distance(0, 2, 4, 0)
#dis = Distance(4, 0, 0, 2)
print(dis._euclidean_distance())
print(dis._city_block())
print(dis._chessboard_distance())
