def numRescueBoats(people,limit):
        left,count,right, = 0,0,1
        people.sort()
        n = len(people)
        while right < n:
            if people[left] + people[right] <= limit:
                count += 1
                left += 2
                right += 2
        if left < n:
            count += (n-left)
        return count
print(numRescueBoats([1,1,1,1],3))