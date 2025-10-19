from collections import Counter
def maxFrequencyElements(nums):
        freq = Counter(nums)                 # Count frequency of each number like {1: 2, 2: 2, 3: 1, 4: 1}
        max_freq = max(freq.values())        # Find the maximum frequency
        total = sum(v for v in freq.values() if v == max_freq)  # Sum all that have max frequency
        return total
number  = input("Enter the number separated by space: ")
nums = number.split() 
print(maxFrequencyElements(nums))
