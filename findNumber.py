def findNumbers(nums):
     count = 0
     total = 0
     for i in nums:
        while i > 0:
            i = int(i/10)
            count +=1
        if count % 2 == 0:
                total +=1
        else:
                pass
     return total
nums = list(map(int,input("Inset the number separated by space: ").split()))
print(findNumbers(nums))
