arr1 = [ 1,3,9,15,20]
arr2 = [2,4,19,19]
mergedArray =[]
left,right = 0,0
while left < len(arr1) and right < len(arr2):
    if arr1[left] <= arr2[right]:
        mergedArray.append(arr1[left])
        left += 1
    else:
        mergedArray.append(arr2[right])
        right += 1
if left < len(arr1):
    mergedArray.extend(arr1[left:])
elif right < len(arr2):
    mergedArray += arr2[right:]
print(mergedArray)

    
