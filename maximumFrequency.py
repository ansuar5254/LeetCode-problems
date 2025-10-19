def maxFrequencyElements(nums):
         numset = set(nums)
         freq = []
         for i in numset:
              fre = nums.count(i)
              freq.append(fre)
         maxfre = max(freq)
         total = 0
         for i in freq:
             if maxfre == i:
                total +=1
         return (maxfre * total)
number  = input("Enter the number separated by space: ")
nums = number.split() 
print(maxFrequencyElements(nums))



       