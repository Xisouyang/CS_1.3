#!python

# this implementation of the Set class is backed by hash tables
from hashtable import HashTable

class Set(object):

    def __init__(self, elements=None):
        # initialize a new empty set structure, and add each element if a sequence is given
        self.hash_set = HashTable()

        if elements != None:
            for item in elements:
                self.add(item)

    def size(self):
        # property that tracks the number of elements in constant time
        return self.hash_set.size

    def contains(self, element):
        # return a boolean indicating whether element is in this set
        return self.hash_set.contains(element)

    def add(self, element):
        # add element to this set, if not present already
        if self.contains(element) == False:
            self.hash_set.set(element, value=None)

    def remove(self, element):
        # remove element from this set, if present, or else raise KeyError
        return self.hash_set.delete(element)

    def union(self, other_set):
        # return a new set that is the union of this set and other_set
        tmp_hash = HashTable()
        for item in self.hash_set.keys():
            tmp_hash.set(item, None)
        for item in other_set.hash_set.keys():
            tmp_hash.set(item, None)
        self.hash_set = tmp_hash
        return self

    def intersection(self, other_set):
        # return a new set that is the intersection of this set and other_set
        pass

    def difference(self, other_set):
        # return a new set that is the difference of this set and other_set
        pass

    def is_subset(self, other_set):
        # return a boolean indicating whether other_set is a subset of this set
        pass
