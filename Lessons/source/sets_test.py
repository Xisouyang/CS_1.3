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
