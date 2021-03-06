#!python

def pattern_empty(text, index_list, which):
    if which == 'contains':
        return True
    elif which == 'find_index':
        return 0
    elif which == 'find_all_indexes':
        for i in range(len(text)):
            index_list.append(i)
        return index_list

def pattern_true(index, which):
    if which == 'contains':
        return True
    elif which == 'find_index':
        return index

def pattern_false(which):
    if which == 'contains':
        return False
    elif which == 'find_index':
        return None


def string_master_func(text, pattern, which):

    index_list = []
    sub_string = ''

    if pattern == '':
        return pattern_empty(text, index_list, which)


    for i in range(len(text) - len(pattern) + 1):   # Iterate through text with limit based on length of pattern
        for j in range(i, len(pattern) + i):        # Iterate through as many characters as pattern has
            sub_string += text[j]                   # add characters to substring
        if pattern == sub_string:                   # compare

            if which == 'find_all_indexes':
                index_list.append(i)
            else:
                return pattern_true(i, which)

        sub_string = ''                             # reset substring if not found

    if which == 'find_all_indexes':
        return index_list
    else:
        return pattern_false(which)

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)

    which = 'contains'

    # if pattern == '':                               # All strings have an empty string
    #     return True
    #
    # sub_string = ''
    # for i in range(len(text) - len(pattern) + 1):   # Iterate through text with limit based on length of pattern
    #     for j in range(i, len(pattern) + i):        # Iterate through as many characters as pattern has
    #         sub_string += text[j]                   # add characters to substring
    #     if pattern == sub_string:                   # compare
    #         return True                             # pattern exists
    #     sub_string = ''                             # reset substring if not found
    # return False                                    # pattern does not exist

    return string_master_func(text, pattern, which)

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)

    which = 'find_index'

    # is_pattern = False                              # flag to determine if pattern found in text
    #
    # if pattern == '':                               # all strings have empty string pattern
    #     return 0
    #
    # for i in range(len(text) - len(pattern) + 1):   # Iterate through text with limit based on length of pattern
    #     is_pattern = True                           # reset flag to True
    #     if text[i] == pattern[0]:                   # if we find first character in pattern
    #         for j in range(len(pattern)):           # check the next few characters up to length of pattern
    #             if text[i + j] != pattern[j]:       # if any of next few characters don't match
    #                 is_pattern = False              # pattern doesn't exist
    #         if is_pattern:                          # pattern exists
    #             return i
    # return None                                     # pattern not found

    # if pattern == '':                                 # All strings have an empty string
    #     return 0
    #
    # sub_string = ''
    # for i in range(len(text) - len(pattern) + 1):   # Iterate through text with limit based on length of pattern
    #     for j in range(i, len(pattern) + i):        # Iterate through as many characters as pattern has
    #         sub_string += text[j]                   # add characters to substring
    #     if pattern == sub_string:                   # compare
    #         return i                                # pattern exists
    #     sub_string = ''                             # reset substring if not found
    # return None                                     # pattern does not exist

    return string_master_func(text, pattern, which)

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    which = 'find_all_indexes'

    # is_pattern = False                              # flag to determine if pattern found
    # list_of_indices = []                            # list to hold indices
    #
    # if pattern == '':                               # all strings have empty substrings
    #     for i in range(len(text)):                  # add all characters in text to list
    #         list_of_indices.append(i)
    #     return list_of_indices
    #
    # for i in range(len(text) - len(pattern) + 1):   # same comments as find_index function,
    #     is_pattern = True                           # except instead of returning index,
    #     if text[i] == pattern[0]:                   # we add index to a list that we return at the end
    #         for j in range(len(pattern)):
    #             if text[i + j] != pattern[j]:
    #                 is_pattern = False
    #         if is_pattern:
    #             list_of_indices.append(i)
    # return list_of_indices

    # sub_string = ''
    # list_of_indices = []
    #
    # if pattern == '':                               # all strings have empty substrings
    #     for i in range(len(text)):                  # add all characters in text to list
    #         list_of_indices.append(i)
    #     return list_of_indices
    #
    # for i in range(len(text) - len(pattern) + 1):   # Iterate through text with limit based on length of pattern
    #     for j in range(i, len(pattern) + i):        # Iterate through as many characters as pattern has
    #         sub_string += text[j]                   # add characters to substring
    #     if pattern == sub_string:                   # compare
    #         list_of_indices.append(i)               # pattern exists
    #     sub_string = ''                             # reset substring if not found
    # return list_of_indices                          # pattern does not exist

    return string_master_func(text, pattern, which)


    # TODO: Implement find_all_indexes here (iteratively and/or recursively)


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
