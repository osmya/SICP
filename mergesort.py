def merge(lst1, lst2):
    if lst1 == [] or lst2 == []:
        return lst1 + lst2
    elif lst1[0] <= lst2[0]:
        return [lst1[0]] + merge(lst1[1:], lst2)
    elif lst1[0] >= lst2[0]:
        return [lst2[0]] + merge(lst1, lst2[1:])


def mergesort(seq):
    """Mergesort algorithm.
    Mergesort is a type of sorting algorithm. 
    It follows a naturally recursive procedure:

    Break the input list into equally-sized halves
    Recursively sort both halves
    Merge the sorted halves.
    
    Using your merge function from the previous question,
    implement mergesort.

    >>> mergesort([4, 2, 5, 2, 1])
    [1, 2, 2, 4, 5]
    >>> mergesort([])     # sorting an empty list
    []
    >>> mergesort([1])   # sorting a one-element list
    [1]
    """
    "*** YOUR CODE HERE ***"
    if len(seq) < 2:
        return seq
    else:
        mid = len(seq)//2 # the mid of seq
        left_sorted = mergesort(seq[:mid])
        right_sorted = mergesort(seq[mid:])
        return merge(left_sorted, right_sorted)
        
        

res = mergesort([4, 2, 5, 2, 1])
