def global_max(arr):
    '''this function is made to find the globally biggest element of a list'''

    if len(arr) == 1:
        return arr[0]
    
    else:
        heighest = arr[0]

        for i in arr:
            if heighest < i:
                heighest = i
            
        return arr.index(heighest)
    
def Two_Dimensional_Peak_Finder(arr, left=0, right=None):

    if right is None:
        right = len(arr[0]) - 1

    column = right - left + 1

    if column == 1:

        carr = []

        for row in arr:
            carr.append(row[left])

        return carr[global_max(carr)]

    else:

        if column % 2 == 0:
            j = left + column // 2 - 1

        else:
            j = left + column // 2

        carr = []

        for row in arr:
            carr.append(row[j])

        i = global_max(carr)

        if j > left and arr[i][j] < arr[i][j - 1]:
            return Two_Dimensional_Peak_Finder(arr, left, j - 1)

        elif j < right and arr[i][j] < arr[i][j + 1]:
            return Two_Dimensional_Peak_Finder(arr, j + 1, right)

        else:
            return arr[i][j]
            
#test case to check whether the global maximum function works or not
print(global_max([4,8,11,10]))

#test case to check whether the two dimensional peak finder function words or not     
print(Two_Dimensional_Peak_Finder([
    [ 2,  4,  3,  1],
    [ 5,  8, 14,  9],
    [ 1, 11, 13,  7],
    [ 6, 10, 20, 12]
]))