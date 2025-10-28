def longestSubString(s):
    myset = set(s[0])
    count= 1
    l,r = 0,1
    longests = count
    while r < len(s):
        if s[r] not in myset:
            myset.add(s[r])
            count += 1
            r += 1
        else:
            myset.remove(s[l])
            l += 1
            count -= 1
        longests = max(longests,count)
    return longests
s = "abcabcbb"
print(longestSubString(s))



    