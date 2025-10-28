
def countKConstraintSubstrings(s,k):
        n = len(s)
        count0 = count1 = 0
        l = 0
        res = 0

        for r in range(n):
            if s[r] == '0':
                count0 += 1
            else:
                count1 += 1

            # shrink the window while both exceed k
            while count0 > k and count1 > k:
                if s[l] == '0':
                    count0 -= 1
                else:
                    count1 -= 1
                l += 1

            # all substrings ending at r are valid
            res += (r - l + 1)

        return res
print(countKConstraintSubstrings("10101",1))
