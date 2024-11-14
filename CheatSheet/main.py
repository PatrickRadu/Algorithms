n=0
print('n=',n)
n='abc'
print('n=',n)

n,m=0,'abc'
print(n,m)

n=n+1
n+=1
#n++ bad

#null=None
n=4
n=None
print(n)

#if
n=1
if n>2:
    n-=1
elif n==2:
    n*=2
else:
    n=1

#and and or
n,m=1,2
if((n>2) and (n!=m) or (n==m)):
    n+=1

#While Loops
n=0
while n<5:
    print(n)
    n+=1

#for 0-4
for i in range(5):
    print(i)

for i in range(2,6):
    print(i)

for i in range(5,1,-1):
    print(i)

for i in range(2,8,2):
    print(i)

print(5/2) # float
print(5//2) # integer round down
print(-3//2) #rezultat -2 pentru ca face round down

#work around
print(int(-3/2)) #rezultat -1 , transforma -1.5 la 1

print(10%3)
print(-10%3) # rez ciudat

import math
print(math.fmod(-10,3))
print(math.floor(3/2))
print(math.ceil(3/2))
print(math.sqrt(2))
print(math.pow(2,3))


#numerele infinite
float('inf')
float("-inf")


#Arrays
arr=[1,2,3] #dinamice
print(arr)
arr.append(4)
print(arr)
arr.pop()
print(arr)

arr.insert(1,7)
print(arr)

arr[0]=0
arr[3]=0
print(arr)

n=5
arr=[1]*n
print(arr)
print(len(arr))

print(arr[-1]) # ultimu element

print(arr[1:3]) # de la index 1 la 3 fara includere

a,b,c=[1,2,3]
print(a,b,c)
#parcurgeri
nums=[1,2,3]
for i in range(len(nums)):
    print(nums[i])

for val in nums:
    print(val)

#avem nevoie si de index si de valoare
for i,val in enumerate(nums):
    print(i,val)

#mai multi vectori
nums1=[1,2,5]
nums2=[2,4,6]
for n1,n2 in zip(nums1,nums2):
    print(n1,n2)
#zip grupeaza elementele din vector

#Reverse
nums=[1,3,5]
nums.reverse()
print(nums)
nums.sort()
print(nums)
nums.sort(reverse=True)

#Array de string
arr=["mama","tata","ana"]
arr.sort()
print(arr)

#Custom Sort
arr.sort(key=lambda x:len(x))
print(arr)

#List comprehansion
arr=[i for i in range(5)]
print(arr)
arr=[i+i for i in range(5)]
print(arr)

#Pentru matrice
arr=[[0]*4 for i in range(4)]
print(arr)
arr=[[i for i in range(4)] for i in range(4)]
print(arr)
#strings
s="abc"
print(s[0:2])
#imutabile
#s[0]="c" eroare


print(s)
s+="def"
print(s) #creaza un string nou
print(str(123)+str(123))
print(int("123")+int("123"))

print(ord("a")) #valoarea ascii

strings=["ab","cd","ef"]
print("".join(strings)) #face append la stringuri in unul singur

#Queue
from collections import deque
queue=deque()
queue.append(1)
queue.append(2)
print(queue)
queue.popleft()
print(queue)
queue.appendleft(1)
queue.pop()

#HashSet
mySet=set()
mySet.add(1)
mySet.add(2)
print(mySet)
print(len(mySet))
print(1 in mySet)
print(2 in mySet)

mySet.remove(2)

#list To set
mySet=set([1,2,3])
print(mySet)
mySet={i+1 for i in range(5)}
print(mySet)

#HashMap
myMap={}
myMap["alice"]=88
myMap["bob"]=77
print(myMap)
print(len(myMap))
print("alice" in myMap)
myMap.pop("alice")
myMap={"alice":70,"ceva":80}
myMap={"Element"+str(i+1):i for i in range(5)}
print(myMap)

#Loop
for key in myMap:
    print(key,myMap[key])
for values in myMap.values():
    print(values)
for key,values in myMap.items():
    print(key,values)

#Tupluri imutabile - in practica pot fi folosite ca si chei
tup=(1,2,3)

myMap={(1,2):3}
print(myMap[(1,2)])

mySet=set()
mySet.add(tup)
print(tup in mySet)

#Motivul principal este pentru ca
#array urile nu pot sa fie key pentu ca
#Nu sunt hasheable

#Heaps
import heapq
minHeap=[]
heapq.heappush(minHeap,3)
heapq.heappush(minHeap,2)
heapq.heappush(minHeap,1)
print(minHeap[0])
while len(minHeap):
    print(heapq.heappop(minHeap))

#nu sunt max Heaps
maxHeap=[]
heapq.heappush(maxHeap,-1)
heapq.heappush(maxHeap,-2)
heapq.heappush(maxHeap,-3)
print(-1*maxHeap[0])
while len(maxHeap):
    print(-heapq.heappop(maxHeap))
#din array
arr=[1,2,3,4,5]
heapq.heapify(arr)



#Functii
def myFunc(n,m):
    return n*m
print(myFunc(1,2))

#Nested
def outer(a,b):
    c="c"
    def inner():
        return a+b+c
    return inner()
print(outer("A","B"))

#modificarile merg in array uri insa nu merg in
#variabile asa ca trebuie declarate cu nonlocal
def double(arr,val):
    def helper():
        for i,n in enumerate(arr):
            arr[i]*=2
        nonlocal val
        val*=2
    helper()
    print(arr,val)
print(double([1,2],3))

class myClass:
    def __init__(self,nums):
        self.nums=nums
        self.size=len(nums)
    def getLength(self):
        return self.size
    def getDoubleLength(self):
        return 2*self.size

def incercare(numar:int)->str:
    return numar
print(incercare(1),type(incercare(1)))