from points import Point


class Triangle:
       
    def __init__(self, x1, y1, x2, y2, x3, y3):
        l = (x2 -x1) * (y3 - y1)
        r = (y2 -y1) * (x3 - x1)
        if l == r:
            raise ValueError('Points cannot be collinear')
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)


    @classmethod
    def from_points(cls, points):
        if not isinstance(points, (tuple, list)):
            raise TypeError('Input must be a tuple or a list')
        if len(points) != 3:
            raise ValueError('Exactly three points are required to build a triangle')
        p1, p2, p3 = points
        return cls(p1.x, p1.y, p2.x, p2.y, p3.x, p3.y)


    def __str__(self):
        return (f'[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y}), ({self.pt3.x}, {self.pt3.y})]')


    def __repr__(self):
        return f'Triangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}, {self.pt3.x}, {self.pt3.y})'


    def __eq__(self, other):
        if not isinstance(other, Triangle):
            raise ValueError('Not a triangle')
        tr1_vertices_set = {(self.pt1.x, self.pt1.y), (self.pt2.x, self.pt2.y), (self.pt3.x, self.pt3.y)}
        tr2_vertices_set = {(other.pt1.x, other.pt1.y), (other.pt2.x, other.pt2.y), (other.pt3.x, other.pt3.y)}
        return tr1_vertices_set == tr2_vertices_set


    def __ne__(self, other):     
        return not self == other


    def area(self):
        return 1/2 * abs(self.pt1.x * (self.pt2.y - self.pt3.y) + self.pt2.x * (self.pt3.y - self.pt1.y) + self.pt3.x * (self.pt1.y - self.pt2.y))


    def move(self, x, y):
        for point_coord in [self.pt1, self.pt2, self.pt3]:
            point_coord.x += x
            point_coord.y += y


    def make4(self):
        m12 = Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)
        m23 = Point((self.pt2.x + self.pt3.x) / 2, (self.pt2.y + self.pt3.y) / 2)
        m31 = Point((self.pt1.x + self.pt3.x) / 2, (self.pt1.y + self.pt3.y) / 2)

        triangle_1 = Triangle(self.pt1.x, self.pt1.y, m12.x, m12.y, m31.x, m31.y)
        triangle_2 = Triangle(m12.x, m12.y, self.pt2.x, self.pt2.y, m23.x, m23.y)
        triangle_3 = Triangle(m31.x, m31.y, m23.x, m23.y, self.pt3.x, self.pt3.y)
        triangle_4 = Triangle(m31.x, m31.y, m12.x, m12.y, m23.x, m23.y)

        return (triangle_1, triangle_2, triangle_3, triangle_4)
        

    @property
    def center(self):
        center_x = round((self.pt1.x + self.pt2.x + self.pt3.x) / 3, 3)
        center_y = round((self.pt1.y + self.pt2.y + self.pt3.y) / 3, 3)
        return Point(center_x, center_y)


    @property
    def top(self):
        return max(self.pt1.y, self.pt2.y, self.pt3.y)


    @property
    def bottom(self):
        return min(self.pt1.y, self.pt2.y, self.pt3.y)


    @property
    def left(self):
        return min(self.pt1.x, self.pt2.x, self.pt3.x)


    @property
    def right(self):
        return max(self.pt1.x, self.pt2.x, self.pt3.x)


    @property
    def height(self):
        return self.top - self.bottom


    @property
    def width(self):
        return self.right - self.left


    @property
    def topleft(self):
        return Point(self.left, self.top)


    @property
    def topright(self):
        return Point(self.right, self.top)


    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)


    @property
    def bottomright(self):
        return Point(self.right, self.bottom)


    @property
    def boundingbox(self):
        return (self.topleft, self.bottomleft, self.bottomright, self.topright)
    

    