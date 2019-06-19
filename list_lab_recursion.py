def reverse_recursive(lst):
    if lst == []:
        return []
    else:
        return reverse_recursive(lst[1:]) + [lst[0]]
        
        
test = reverse_recursive([1, 2, 3, 4])


def merge(lst1, lst2):
    """Merges two sorted lists recursively.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"
    if lst1 == [] or lst2 == []:
        return lst1 + lst2
    elif lst1[0] < lst2[0]:
        return [lst1[0]] + merge(lst1[1:], lst2)
    elif lst1[0] > lst2[0]:
        return [lst2[0]] + merge(lst1, lst2[1:])
        
test2 = merge([1, 3, 5], [2, 4, 6])
