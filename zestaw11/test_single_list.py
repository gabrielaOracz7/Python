import pytest
from single_list import Node, SingleList

class TestSingleList:

    @pytest.fixture
    def list_1(self):
        l1 = SingleList()
        for v in [1, 2, 3, 4, 5]:
            l1.insert_tail(Node(v))
        return l1
    
    @pytest.fixture
    def list_2(self):
        l2 = SingleList()
        for v in [89, 23, 1, -9, 56, 2, -90, 6]:
            l2.insert_tail(Node(v))
        return l2
    
    @pytest.fixture
    def list_3(self):
        l3 = SingleList()
        for v in [12, 67, -23, 89, 0, 13, 10000, -87, 12345, -8900]:
            l3.insert_tail(Node(v))
        return l3
    
    @pytest.fixture
    def empty_list(self):
        return SingleList()
    
    @staticmethod
    def add_nodes_to_list(sl: SingleList):
        values = []
        node = sl.head
        while node:
            values.append(node.data)
            node = node.next
        return values



    def test_search(self, list_1, list_2, list_3, empty_list):
        assert list_1.search(3) == Node(3)
        assert list_1.search(8) == None
        assert list_2.search(90) == None
        assert list_2.search(6) == Node(6)
        assert list_3.search(12) == Node(12)
        assert list_3.search(0) == Node(0)
        assert empty_list.search(1) == None


    def test_find_min(self, list_1, list_2, list_3, empty_list):
        assert list_1.find_min() == Node(1)
        assert list_2.find_min() == Node(-90)
        assert list_3.find_min() == Node(-8900)
        assert empty_list.find_min() == None

        list_1.insert_head(Node(0))
        assert list_1.find_min() == Node(0)

        list_2.insert_tail(Node(-123456))
        assert list_2.find_min() == Node(-123456)


    def test_find_max(self, list_1, list_2, list_3, empty_list):
        assert list_1.find_max() == Node(5)
        assert list_2.find_max() == Node(89)
        assert list_3.find_max() == Node(12345)
        assert empty_list.find_max() == None

        list_2.insert_head(Node(1002300))
        assert list_2.find_max() == Node(1002300)

        list_3.insert_tail(Node(54321))
        assert list_3.find_max() == Node(54321)

    
    def test_reverse(self, list_1, list_2, list_3, empty_list):
        empty_list.reverse()
        assert self.add_nodes_to_list(empty_list) == []
        assert empty_list.head is None
        assert empty_list.tail is None
        assert empty_list.count() == 0

        list_1.reverse()
        assert self.add_nodes_to_list(list_1) == [5, 4, 3, 2, 1]
        assert list_1.head == Node(5)
        assert list_1.tail == Node(1)

        list_2.reverse()
        assert self.add_nodes_to_list(list_2) == [6, -90, 2, 56, -9, 1, 23, 89]
        assert list_2.head == Node(6)
        assert list_2.tail == Node(89)

        list_3.reverse()
        assert self.add_nodes_to_list(list_3) == [-8900, 12345, -87, 10000, 13, 0, 89, -23, 67, 12]
        assert list_3.head == Node(-8900)       
        assert list_3.tail == Node(12)

        list_4 = SingleList()
        list_4.insert_head(Node(5))
        list_4.reverse()
        assert self.add_nodes_to_list(list_4) == [5]
        assert list_4.count() == 1
        assert list_4.head == Node(5)
        assert list_4.tail == Node(5)



