import unittest
from sets import Set
# Python 2 and 3 compatibility: unittest module renamed this assertion method
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual

class SetsTest(unittest.TestCase):

    def test_init(self):

        s = Set()
        assert s.hash_set.size == 0

    def test_size(self):

        s = Set()
        assert s.hash_set.size == 0
        s.add('A')
        assert s.hash_set.size == 1
        s.add('B')
        assert s.hash_set.size == 2

    def test_contains(self):

        s = Set(['A', 'B', 'C'])
        assert s.contains('A') == True
        assert s.contains('B') == True
        assert s.contains('C') == True
        assert s.contains('X') == False

    def test_add(self):

        s = Set()
        assert s.hash_set.size == 0
        s.add('A')
        assert s.hash_set.size == 1
        assert s.contains('A') == True
        s.add('A')
        assert s.hash_set.size == 1
        s.add('B')
        assert s.hash_set.size == 2
        assert s.contains('B') == True

    def test_remove(self):

        s = Set(['A', 'B', 'C'])
        assert s.hash_set.size == 3
        s.remove('A')
        assert s.hash_set.size == 2
        with self.assertRaises(KeyError):
            s.remove('A')

    def test_union(self):

        set_one = Set(['A', 'B', 'C'])
        set_two = Set(['X', 'Y'])
        union_set = set_one.union(set_two)
        self.assertCountEqual(union_set.hash_set.keys(), ['A', 'B', 'C', 'X', 'Y'])

        set_one = Set(['A', 'A', 'B', 'C'])
        set_two = Set(['X', 'Y', 'X'])
        union_set = set_one.union(set_two)
        assert (union_set.hash_set.size == 7) == False

    def test_intersection(self):

        set_one = Set(['A', 'B', 'C'])
        set_two = Set(['A', 'C', 'D'])
        intersection_set = set_one.intersection(set_two)
        self.assertCountEqual(intersection_set.hash_set.keys(), ['A', 'C'])

    def test_is_subset(self):

        set_one = Set(['A', 'B', 'C'])
        set_two = Set(['A', 'B'])
        is_a_subset = set_one.is_subset(set_two)
        assert is_a_subset == True

        set_one = Set(['A', 'B', 'C', 'D'])
        set_two = Set(['A', 'B', 'C', 'D', 'E'])
        is_a_subset = set_one.is_subset(set_two)
        assert is_a_subset == False

        set_one = Set(['A', 'B', 'C'])
        set_two = Set(['A', 'D'])
        is_a_subset = set_one.is_subset(set_two)
        assert is_a_subset == False

    def test_difference(self):
        
        set_one = Set(['A', 'B', 'C', 'D'])
        set_two = Set(['A', 'B', 'C', 'D', 'E'])
        new_set = set_one.difference(set_two)
        self.assertCountEqual(new_set.hash_set.keys(), [])

        set_one = Set(['A', 'B', 'C'])
        set_two = Set(['B', 'C', 'D'])
        new_set = set_one.difference(set_two)
        self.assertCountEqual(new_set.hash_set.keys(), ['A'])
