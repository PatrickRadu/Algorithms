def isPalindrome(s):
    justLetters = ''.join(x for x in s if x.isalnum())
    finalString = justLetters.lower()
    i=0
    j=len(finalString)-1
    while i<j:
        if finalString[i]!=finalString[j]:
            return False
        i+=1
        j-=1
    return True

s="Was it a car or a cat I saw?"
justLetters=''.join(x for x in s if x.isalnum())
print(justLetters)
finalString=justLetters.lower()
print(finalString)

print(isPalindrome(s))
print(isPalindrome("0P"))


#implementare isalnum