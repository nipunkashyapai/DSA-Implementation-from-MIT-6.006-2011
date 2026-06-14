def One_D_Peak_Finder(arr, start=0, end=None):
    if end is None:
        end = len(arr)

    n = end - start

    if n == 1:
        return arr[start]

    elif n == 2:
        if arr[start] > arr[start + 1]:
            return arr[start]
        else:
            return arr[start + 1]

    else:
        if n % 2 == 0:
            mid = start + n // 2 - 1

            if arr[mid] < arr[mid - 1]:
                return One_D_Peak_Finder(arr, start, mid)

            elif arr[mid] < arr[mid + 1]:
                return One_D_Peak_Finder(arr, mid + 1, end)

            else:
                return arr[mid]

        else:
            mid = start + (n + 1) // 2 - 1

            if arr[mid] < arr[mid - 1]:
                return One_D_Peak_Finder(arr, start, mid + 1)

            elif arr[mid] < arr[mid + 1]:
                return One_D_Peak_Finder(arr, mid + 1, end)

            else:
                return arr[mid]
            

#following are a few test cases showing that this algorithm returns a peak            
print(One_D_Peak_Finder([1,2,3,4,5]))
print(One_D_Peak_Finder([5,4,3,2,1]))
print(One_D_Peak_Finder([7,7,7,7]))
print(One_D_Peak_Finder([42]))
print(One_D_Peak_Finder([1,3,7,5,2]))
print(One_D_Peak_Finder([1,5,2,8,3,6,4]))
print(One_D_Peak_Finder([9,2,3,4,1]))