def insertion_sort(list):
    for i in range(1,len(list)):
        a=list[i]
        j=i-1
        while j>=0 and a<list[j]:
            list[j+1]=list[j]
            j-=1
        print(list)
        list[j+1]=a
        print(list)
    return list

list1 = [ 7, 2, 1, 6 ]
print("The unsorted list is:", list1)
print("The sorted new list is:", insertion_sort(list1))