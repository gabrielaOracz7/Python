import pytest
from points import Point
from triangles import Triangle

class TestTriangles:

    @pytest.fixture
    def triangle_1(self):
        return Triangle(0, 0, 4, 0, 0, 3)
    
    @pytest.fixture
    def triangle_2(self):
        return Triangle(-1, -1, 2, 3, 4, -2)
    
    @pytest.fixture
    def triangle_3(self):
        return Triangle(-1.5, -1.0, 2.2, 3.5, 4.0, -2.5)
    
    @pytest.fixture
    def triangle_4(self):
        return Triangle(0, 3, 0, 0, 4, 0)


    def test_collinear_points(self):
        with pytest.raises(ValueError):
            collinear_points_triangle = Triangle(1, 1, 2, 2, 3, 3)


    def test_from_points(self):
        self.pt1 = Point(1, 2)
        self.pt2 = Point(1, 4)
        self.pt3 = Point(5, 6)

        triangle_from_list = Triangle.from_points([self.pt1, self.pt2, self.pt3])
        assert triangle_from_list.pt1.x == self.pt1.x
        assert triangle_from_list.pt1.y == self.pt1.y
        assert triangle_from_list.pt2.x == self.pt2.x
        assert triangle_from_list.pt2.y == self.pt2.y
        assert triangle_from_list.pt3.x == self.pt3.x
        assert triangle_from_list.pt3.y == self.pt3.y

        triangle_from_tuple = Triangle.from_points((self.pt3, self.pt2, self.pt1))
        assert triangle_from_tuple.pt1.x == self.pt3.x
        assert triangle_from_tuple.pt1.y == self.pt3.y
        assert triangle_from_tuple.pt2.x == self.pt2.x
        assert triangle_from_tuple.pt2.y == self.pt2.y
        assert triangle_from_tuple.pt3.x == self.pt1.x
        assert triangle_from_tuple.pt3.y == self.pt1.y

        with pytest.raises(TypeError):
            dict_triangle = Triangle.from_points({1:1, 2:2, 3:3})

        with pytest.raises(ValueError):
            four_points_triangle = Triangle.from_points([self.pt1, self.pt2, self.pt3, self.pt3])

        
    def test_str(self, triangle_1, triangle_2, triangle_3, triangle_4):
        assert str(triangle_1) == "[(0, 0), (4, 0), (0, 3)]"
        assert str(triangle_2) == "[(-1, -1), (2, 3), (4, -2)]"
        assert str(triangle_3) == "[(-1.5, -1.0), (2.2, 3.5), (4.0, -2.5)]"
        assert str(triangle_4) == "[(0, 3), (0, 0), (4, 0)]"
        assert str(Triangle(5, 4, 1, 3, -4, 6)) == "[(5, 4), (1, 3), (-4, 6)]"


    def test_repr(self, triangle_1, triangle_2, triangle_3, triangle_4):
        assert repr(triangle_1) == "Triangle(0, 0, 4, 0, 0, 3)"
        assert repr(triangle_2) == "Triangle(-1, -1, 2, 3, 4, -2)"
        assert repr(triangle_3) == "Triangle(-1.5, -1.0, 2.2, 3.5, 4.0, -2.5)"
        assert repr(triangle_4) == "Triangle(0, 3, 0, 0, 4, 0)"
        assert repr(Triangle(1, 2, 9, 8, 5, -5)) == "Triangle(1, 2, 9, 8, 5, -5)"

    
    def test_eq(self, triangle_1, triangle_2, triangle_3, triangle_4):
        assert triangle_1 == triangle_4
        assert triangle_2 == Triangle(-1, -1, 2, 3, 4, -2)
        assert triangle_3 == triangle_3
        assert Triangle(-1, 3, 5, -6, 2, 9) == Triangle(2, 9, -1, 3, 5, -6)

        assert not (triangle_1 == triangle_2)
        assert not (triangle_1 == triangle_3)

        with pytest.raises(ValueError):
            triangle_2 == [-1, -1, 2, 3, 4, -2]


    def test_ne(self, triangle_1, triangle_2, triangle_3, triangle_4):
        assert triangle_1 != triangle_2
        assert triangle_1 != triangle_3
        assert triangle_2 != triangle_4
        assert triangle_4 != Triangle(0, -3, 0, 0, 4, 0)
        assert Triangle(-1.1, 2.0, -4.5, 7, 9, 3) != Triangle(1.1, 2, 4.5, -7, 9, 3)

        assert not (triangle_1 != triangle_4)
        assert not (Triangle(-1, 3, 5, -6, 2, 9) != Triangle(2, 9, -1, 3, 5, -6))

        with pytest.raises(ValueError):
            triangle_2 != [1, 1, 2, 3, 4, 2]

    
    def test_area(self, triangle_1, triangle_2, triangle_3, triangle_4):
        assert triangle_1.area() == 6
        assert triangle_2.area() == 11.5
        assert triangle_3.area() == 15.15
        assert triangle_4.area() == 6
        assert Triangle(2, -4, 5, -9, 1.15, 4).area() == 9.875


    def test_move(self, triangle_1, triangle_2, triangle_3, triangle_4):
        triangle_1.move(2, -5)
        assert  triangle_1 == Triangle(2, -5, 6, -5, 2, -2)

        triangle_2.move(0, 0)
        assert triangle_2 == Triangle(-1, -1, 2, 3, 4, -2)

        triangle_4.move(-1.5, 2.75)
        assert triangle_4 == Triangle(-1.5, 5.75, -1.5, 2.75, 2.5, 2.75)

        triangle_3.move(10, -7.5)
        assert triangle_3 == Triangle(8.5, -8.5, 12.2, -4.0, 14.0, -10.0)


    def test_make4(self, triangle_1, triangle_2):
        assert triangle_1.make4() == (Triangle(0, 0, 2, 0, 0, 1.5), Triangle(2, 0, 4, 0, 2, 1.5), 
                                           Triangle(0, 1.5, 2, 1.5, 0, 3), Triangle(0, 1.5, 2, 0, 2, 1.5))        
        assert triangle_2.make4() == (Triangle(-1, -1, 0.5, 1, 1.5, -1.5), Triangle(0.5, 1, 2, 3, 3, 0.5), 
                                           Triangle(1.5, -1.5, 3, 0.5, 4, -2), Triangle(1.5, -1.5, 0.5, 1, 3, 0.5))
        assert Triangle(1.25, 4.75, 5.5, 2.5, 3.75, 8.0).make4() == (Triangle(1.25, 4.75, 3.375, 3.625, 2.5, 6.375), 
                                                                    Triangle(3.375, 3.625, 5.5, 2.5, 4.625, 5.25),
                                                                    Triangle(2.5, 6.375, 4.625, 5.25, 3.75, 8.0), 
                                                                    Triangle(2.5, 6.375, 3.375, 3.625, 4.625, 5.25))
        assert Triangle(2, 4, -6, -8.5, 10, -14.8).make4() == (Triangle(2, 4, -2, -2.25, 6, -5.4), 
                                                              Triangle(-2, -2.25, -6, -8.5, 2, -11.65),
                                                              Triangle(6, -5.4, 2, -11.65, 10, -14.8), 
                                                              Triangle(6, -5.4, -2, -2.25, 2, -11.65)) 


    def test_center(self, triangle_1, triangle_2, triangle_3, triangle_4):
        assert triangle_1.center == Point(1.333, 1)
        assert triangle_2.center == Point(1.667, 0)
        assert triangle_3.center == Point(1.567, 0)
        assert triangle_4.center == Point(1.333, 1)
        assert Triangle(-1, 4, -2.5, -7.7, 2, -15).center == Point(-0.5, -6.233)

    
    def test_top(self, triangle_1, triangle_2, triangle_3):
        assert triangle_1.top == 3
        assert triangle_2.top == 3
        assert triangle_3.top == 3.5
        assert Triangle(1, -4.5, -2, -98, 12, -2).top == -2
        assert Triangle(12, -12, 3, -12, 0, 0).top == 0


    def test_bottom(self, triangle_1, triangle_2, triangle_3, triangle_4):
        assert triangle_1.bottom == 0
        assert triangle_2.bottom == -2
        assert triangle_3.bottom == -2.5
        assert triangle_4.bottom == 0
        assert Triangle(12, 4, -213, 5, 23.8, -123.876).bottom == -123.876


    def test_left(self, triangle_1, triangle_2, triangle_3, triangle_4):
        assert triangle_1.left == 0
        assert triangle_2.left == -1
        assert triangle_3.left == -1.5
        assert triangle_4.left == 0
        assert Triangle(-123.5, 34, 98.65, 3, 12345, -89.5).left == -123.5


    def test_right(self, triangle_1, triangle_2, triangle_3):
        assert triangle_1.right == 4
        assert triangle_2.right == 4
        assert triangle_3.right == 4
        assert Triangle(-123.5, 34, 98.65, 3, 12345, -89.5).right == 12345
        assert Triangle(0, 12.5, -123.8765, 43, -12, 5).right == 0

    
    def test_height(self, triangle_1, triangle_2, triangle_3):
        assert triangle_1.height == 3
        assert triangle_2.height == 5
        assert triangle_3.height == 6
        assert Triangle(12, 4, -213, 5, 23.8, -123.876).height == 128.876
        assert Triangle(12, -12, 3, -12, 0, 0).height == 12

    
    def test_width(self, triangle_1, triangle_2, triangle_3):
        assert triangle_1.width == 4
        assert triangle_2.width == 5
        assert triangle_3.width == 5.5
        assert Triangle(-123.5, 34, 98.65, 3, 12345, -89.5).width == 12468.5
        assert Triangle(0, 12.5, -123.8765, 43, -12, 5).width == 123.8765


    def test_topleft(self, triangle_1, triangle_2, triangle_3, triangle_4):
        assert triangle_1.topleft == Point(0, 3)
        assert triangle_2.topleft == Point(-1, 3)
        assert triangle_3.topleft == Point(-1.5, 3.5)
        assert triangle_4.topleft == Point(0, 3)
        assert Triangle(-123.5, 34, 98.65, 3, 12345, -89.5).topleft == Point(-123.5, 34)
        assert Triangle(12, -45.6, 0, 4, 123.67, -567.6).topleft == Point(0, 4)

    
    def test_topright(self, triangle_1, triangle_2, triangle_3):
        assert triangle_1.topright == Point(4, 3)
        assert triangle_2.topright == Point(4, 3)
        assert triangle_3.topright == Point(4, 3.5)
        assert Triangle(-123.5, 34, 98.65, 3, 12345, -89.5).topright == Point(12345, 34)
        assert Triangle(0, 12.5, -123.8765, 43, -12, 5).topright == Point(0, 43)

    
    def test_bottomleft(self, triangle_1, triangle_2, triangle_3):
        assert triangle_1.bottomleft == Point(0, 0)
        assert triangle_2.bottomleft == Point(-1, -2)
        assert triangle_3.bottomleft == Point(-1.5, -2.5)
        assert Triangle(-123.5, 34, 98.65, 3, 12345, -89.5).bottomleft == Point(-123.5, -89.5)
        assert Triangle(12, 4, -213, 5, 23.8, -123.876).bottomleft == Point(-213, -123.876)


    def test_bottomright(self, triangle_1, triangle_2, triangle_3):
        assert triangle_1.bottomright == Point(4, 0)
        assert triangle_2.bottomright == Point(4, -2)
        assert triangle_3.bottomright == Point(4, -2.5)
        assert Triangle(12, 4, -213, 5, 23.8, -123.876).bottomright == Point(23.8, -123.876)
        assert Triangle(-123.5, 34, 98.65, 3, 12345, -89.5).bottomright == Point(12345, -89.5)
       

    def test_boundingbox(self, triangle_1, triangle_2, triangle_3):
        assert triangle_1.boundingbox == (triangle_1.topleft, triangle_1.bottomleft,
                                        triangle_1.bottomright, triangle_1.topright)
        assert triangle_2.boundingbox == (triangle_2.topleft, triangle_2.bottomleft,
                                        triangle_2.bottomright, triangle_2.topright)
        assert triangle_3.boundingbox == (triangle_3.topleft, triangle_3.bottomleft,
                                        triangle_3.bottomright, triangle_3.topright)
