def insertion_sort(arr):
    '''This is an insertion sort with binary search involved in it'''
    i = 1
    while i < len(arr):
        j = i

        if j % 2 == 0:
            middle = j/2
            