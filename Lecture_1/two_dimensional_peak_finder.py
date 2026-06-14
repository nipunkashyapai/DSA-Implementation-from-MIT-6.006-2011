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
    
def Two_Dimensional_Peak_Finder(arr):
    column = len(arr[0])

    if column == 1:
        return global_max(arr)
    
    else:

        if column % 2 == 0:
            j = column // 2 - 1

            carr = []

            for MyArray in arr:
                carr.append(MyArray[j])

            i = global_max(carr)

            if arr[i][j] < arr[i][j - 1]:
                carr2 = []

                for CarrArray in arr:
                    carr2.append(CarrArray[:j])

                return Two_Dimensional_Peak_Finder(carr2)
            
            elif arr[i][j] < arr[i][j + 1]:
                carr2 = []

                for CarrArray in arr:
                    carr2.append(CarrArray[j + 1:])

                return Two_Dimensional_Peak_Finder(carr2)
            
            else:
                return arr[i][j]
            
        else:
            j = column // 2

            carr = []

            for MyArray in arr:
               carr.append(MyArray[j])

            i = global_max(carr)

            if arr[i][j] < arr[i][j - 1]:
                carr2 = []

                for CarrArray in arr:
                    carr2.append(CarrArray[:j])

                return Two_Dimensional_Peak_Finder(carr2)
            
            elif arr[i][j] < arr[i][j + 1]:
                carr2 = []

                for CarrArray in arr:
                    carr2.append(CarrArray[j + 1:])

                return Two_Dimensional_Peak_Finder(carr2)
            
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