
def longestCommonPrefix(strs):
        costr = ""
        if len(strs) <= 1:
            return strs[0]
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if i == len(strs[j]) or strs[0][i] != strs[j][i]:
                    return costr
            costr +=strs[0][i]
        return costr
strs = list(map(str,input("enter the word separated by space: ").split()))
print(longestCommonPrefix(strs))
        