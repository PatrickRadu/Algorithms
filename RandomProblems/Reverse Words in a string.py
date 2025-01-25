


s='the sky is blue'
word=[]
res=[]
i=0
while i < len(s):
    while i<len(s) and (s[i].isalpha() or s[i].isalnum()):
        word.append(s[i])
        i+=1
    if word:
        res.append("".join(word))
        word=[]
    i+=1

res.reverse()
res=" ".join(res)
print(res)
