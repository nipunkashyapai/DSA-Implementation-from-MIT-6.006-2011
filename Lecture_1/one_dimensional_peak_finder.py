def One_D_Peak_Finder(arr):
    '''This is a one-dimensional pek finder function'''

    if len(arr) == 1:
        return arr[0]
    
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0]

        else:
            return arr[1]    
    else:
        if len(arr) % 2 == 0:
            if arr[len(arr)//2 - 1] < arr[len(arr)//2 - 2]:
                return One_D_Peak_Finder(arr[:len(arr)//2 - 1])
                
            elif arr[len(arr)//2 - 1] < arr[len(arr)//2]:
                return One_D_Peak_Finder(arr[len(arr)//2:])

            else:
                return arr[len(arr)//2 - 1]
            
        else:
            if arr[(len(arr) + 1)//2 - 1] < arr[(len(arr) + 1)//2 - 2]:
                return One_D_Peak_Finder(arr[:(len(arr) + 1)//2])
            
            elif arr[(len(arr) + 1)//2 - 1] < arr[(len(arr) + 1)//2]:
                return One_D_Peak_Finder(arr[(len(arr) + 1)//2:])
            
            else:
                return arr[(len(arr) + 1)//2 - 1]
            

#following are a few test cases showing that this algorithm returns a peak            
print(One_D_Peak_Finder([1,2,3,4,5]))
print(One_D_Peak_Finder([5,4,3,2,1]))
print(One_D_Peak_Finder([7,7,7,7]))
print(One_D_Peak_Finder([42]))
print(One_D_Peak_Finder([1,3,7,5,2]))
print(One_D_Peak_Finder([1,5,2,8,3,6,4]))
print(One_D_Peak_Finder([9,2,3,4,1]))