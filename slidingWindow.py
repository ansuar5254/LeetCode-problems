nums = [2, 1, 5, 1, 3, 2] 
k = 3 
curr_value = sum(nums[:k])
maxValue = curr_value
left = 0
right = k
while right < len(nums):
    #remove the leftmost value and add the right side
    curr_value = curr_value-nums[left] + nums[right]
    maxValue = max(curr_value,maxValue)
    left += 1
    right += 1
print(maxValue)

