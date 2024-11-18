# TODO: Implement the following functions based on the descriptions.

def reverse_list(lst):
    """
    Reverses the given list.
    :param lst: List of integers.
    :return: A list with elements in reverse order.
    """
    pass  # Implement this

    return list(reversed(lst))

def count_occurrences(lst, element):
    """
    Counts how many times the given element appears in the list.
    :param lst: List of elements.
    :param element: Element to count.
    :return: Integer count of occurrences.
    """
    pass  # Implement this
    count = 0

    for num in lst:
        if num == 2:
            count += 1
    return count
    

def get_keys_with_value(dct, value):
    """
    Returns a list of keys that have the given value in the dictionary.
    :param dct: Dictionary to search.
    :param value: Value to find.
    :return: List of keys.
    """
    pass  # Implement this

    result = []

    for i in dct.items():
        if i[1] == value:
            result.append(i[0])
    return result


def merge_sorted_lists(lst1, lst2):
    """
    Merges two sorted lists into one sorted list.
    :param lst1: First sorted list.
    :param lst2: Second sorted list.
    :return: Merged sorted list.
    """
    pass  # Implement this
    
    result = []

    for i in lst1:
        result.append(i)

    for j in lst2:
        result.append(j)

    return sorted(result)


def find_second_largest(numbers):
    """
    Finds the second largest number in a list.
    :param numbers: List of integers.
    :return: The second largest integer.
    """
    pass  # Implement this
    
    res = []

    for i in numbers:
        large = max(numbers)

        if i < large:
            res.append(i)

    if len(res) == 0:
        return None
    else:
        return max(res)


def is_anagram(str1, str2):
    """
    Checks if two strings are anagrams.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. For example, "listen" and "silent"
    are anagrams because they use the same letters in a different order.
    
    :param str1: First string.
    :param str2: Second string.
    :return: True if the strings are anagrams, False otherwise.
    """
    pass  # Implement this
    
    for i in str1:
        if i in str2:
            return True
        return False


def flatten_list(nested_list):
    """
    Flattens a nested list into a single list.
    :param nested_list: List of lists.
    :return: A flat list with all elements.
    """
    pass  # Implement this
    res = []

    for i in nested_list:
        if type(i) == list:
            for j in i:
                res.append(j)
        else:
            res.append(i)
    return res


def remove_duplicates(lst):
    """
    Removes duplicates from the list while maintaining order.
    :param lst: List of elements.
    :return: List without duplicates.
    """
    pass  # Implement this

    result = []

    for i in lst:
        if i not in result:
            result.append(i)
    
    return result


def find_common_elements(lst1, lst2):
    """
    Finds common elements between two lists.
    :param lst1: First list.
    :param lst2: Second list.
    :return: List of common elements.
    """
    pass  # Implement this
    
    res = []

    for i in lst1:
        if i in lst2:
            res.append(i)

    return res