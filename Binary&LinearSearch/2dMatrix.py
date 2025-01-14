
#brute force

def binarySearch(array,target):
    l=0;
    r=len(array)-1
    while(l<=r):
        m=(r+l)//2
        if array[m]==target:
            return True
        if array[m]>target:
            r = m - 1
        if array[m]<target:
            l = m + 1
    return False



def d2Matrix(matrix,target):
    array=list()
    for row in range (len(matrix)):
        for column in range(len(matrix[0])):
            array.append(matrix[row][column])
    return binarySearch(array,target)




matrix=[[1,2,4,8],[10,11,12,13],[14,20,30,40]]

print(d2Matrix(matrix,10))