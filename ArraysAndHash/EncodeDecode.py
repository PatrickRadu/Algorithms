class Solution:

    def encode(self, strs) -> str:
        output = ""
        for word in strs:
            output += str(len(word)) + "#" + word
        return output

    def decode(self, s: str):
        output=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            i=j+1
            j=i+length
            output.append(s[i:j])
            i=j
        return output