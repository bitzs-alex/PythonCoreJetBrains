class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, point):
        dist_x = pow(self.x - point.x, 2)
        dist_y = pow(self.y - point.y, 2)

        return pow(dist_y + dist_x, 0.5)
