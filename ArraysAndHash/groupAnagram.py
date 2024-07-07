from collections import defaultdict


def anagramsTry(strs):
    output=[]
    for i in range(len(strs)):
        list=[]
        list.append(strs[i])
        for j in range(i+1,len(strs)):
            if(sorted(strs[i])==sorted(strs[j])):
                list.append(strs[j])
        output.append(list)
    return output

def anagrams(strs):
    grup={}
    for word in strs:
        count=[0 for i in range(26)]
        for letter in word:
            count[ord(letter)-ord('a')]+=1
        key=tuple(count)
        if key not in grup:
            grup[key]=[]
        grup[key].append(word)
    return grup.values()



# def SolvedAnagrams(strs):
#     res=defaultdict(list)
#     for s in strs:
#         count=[0]*26
#         for c in s:
#             count[ord[c]-ord("a")]+=1
#         res[tuple(count)].append(s)
#     return res.values()









#try
output=[]
print(output)
output.append([1,2,3])
print(output)
output.append([2,3,4])
print(output)

str=["cat","dog"]
for i in range(len(str)):
    print(str[i])

for word in str:
    print(word)

strs=["act","pots","tops","cat","stop","hat"]
print(anagramsTry(strs))
# print(SolvedAnagrams(strs))
count=[0 for i in range(26)]
print(count)

print(anagrams(strs))