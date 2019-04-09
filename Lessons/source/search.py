#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here

    # check if index is within array length
    if index <= len(array) - 1:
        # if we find the number
        if array[index] == item:
            return index
        else:
            return linear_search_recursive(array, item, index + 1)
    return None


    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here

    left = 0
    right = len(array) - 1

    while left <= right:

        middle_index = (left + right) // 2
        middle_value = array[middle_index]

        if item == middle_value:
            return middle_index
        elif item < middle_value:
            right = middle_index - 1
        elif item > middle_value:
            left = middle_index + 1
    return None

    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here

    # check if array is empty
        # if it is, return nil
    if len(array) == 0:
        return None

    # set left to 1st index of array
    # set right to last index of array
    if left == None:
        left = 0
        right = len(array) - 1

    # we've searched through everything
    if left > right:
        return None

    # check middle of the array
    middle_index = (left + right) // 2
    middle_value = array[middle_index]

    # if item is in middle:
        # return the index
    if item == middle_value:
        return middle_index

    # if item is greater, update left index to 1 greater than the middle index
        # call recursive function
    elif item > middle_value:
        left = middle_index + 1

    # if item is smaller, update right index to 1 less than the middle index
        # call recursive function
    elif item < middle_value:
        right = middle_index - 1

    return binary_search_recursive(array, item, left, right)

    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
