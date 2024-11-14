def isPalindrome(s):
    justLetters="".join(letter for letter in s if letter.isalnum())
    justLetters=justLetters.lower()
    i=0
    j=len(justLetters)
    while(i>j):
        if justLetters[i]!=justLetters[j]:
            return False
        i=i+1
        j=j-1
    return True
s="Was it a car or a cat I saw?"
# justLetters=''.join(x for x in s if x.isalnum())
# print(justLetters)
# finalString=justLetters.lower()
# print(finalString)
#
print(isPalindrome(s))
# print(isPalindrome("0P"))


#implementare isalnum