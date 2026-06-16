def insertion_sort(arr):
    '''This is a simple insertion sort'''
    i = 1
    while i < len(arr):
        j = i

        while arr[j-1] > arr[j] and j != 0:
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j -= 1

        i += 1


#Test cases
arr = [4, 2, 8, 1, 3]
insertion_sort(arr)
print(arr)
arr = [1, 2, 3, 4, 5]
insertion_sort(arr)
print(arr)
arr = [5, 4, 3, 2, 1]
insertion_sort(arr)
print(arr)
arr = [1, 2, 3, 5, 4, 6]
insertion_sort(arr)
print(arr)
