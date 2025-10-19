def maximumProduct(nums):
    nums.sort()
    return((nums[-1]-1)*(nums[-2]-1))
nums =list(map(int, input("Inset the number separated by space: ").split()))
print(maximumProduct(nums))