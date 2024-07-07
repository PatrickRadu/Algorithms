

array=list([9,1,2,4,3,7,6,5])

def linear_search(array,target):
    for i in range(len(array)):
        if array[i]==target:
            return i
    return -1


