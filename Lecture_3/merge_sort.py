def merge_sort(arr):
    '''simple merge sort algorithm is implemented here'''
    if len(arr) <= 1:
        return arr
    
    middle = len(arr)//2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

#test cases
arr = [4,1,2,0]
print(merge_sort(arr))
arr = [5]
print(merge_sort(arr))
arr = [1, 2, 3, 4, 5]
print(merge_sort(arr))
arr = [5, 4, 3, 2, 1]
print(merge_sort(arr))
arr = [38, 27, 43, 3, 9, 2, 82, 10]
print(merge_sort(arr))