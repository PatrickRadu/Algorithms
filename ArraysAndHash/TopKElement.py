from collections import defaultdict


def topKElement(nums,k):
    dictionary={(i):0 for i in range(-1000,1001)}
    output=[]
    for num in nums:
        dictionary[num]=dictionary[num]+1
    print(dictionary)
    dictSorted=dict(sorted(dictionary.items(),reverse=True,key=lambda item:item[1]))
    print(dictSorted)
    for key,value in dictSorted.items():
        if(k>0):
            output.append(key)
            k=k-1
        else:
            break
    return output


nums =[1,2,2,3,3,3]
k = 2
print(topKElement(nums,k))

# dic={"num1:":1,"num3":3,"num2":2}
# sortedDic=sorted(dic,reverse=True)
# print(dic)
# print(sortedDic)




