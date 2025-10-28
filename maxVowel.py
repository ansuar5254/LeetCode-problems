def maxVowelnum(s, k):
    vowe ={'a','e','i','o','u'}
    countVowel = 0
    for i in s[:k]:
        if i in vowe:
            countVowel += 1
    maxVowelnums = countVowel
    print(countVowel)
    for i in range(k,len(s)):
        if s[i-k] in vowe:
            countVowel -= 1
        if s[i] in vowe:
            countVowel += 1
        maxVowelnums = max(maxVowelnums,countVowel)
    return maxVowelnums
s = "abciiidef"
k = 3
print(maxVowelnum(s,k))
   
        

