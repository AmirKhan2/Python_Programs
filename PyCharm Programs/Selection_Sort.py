def sort(nums):
    for i in range(len(nums)):
        lowpos = i
        for j in range(i,len(nums)):
            if nums[lowpos] > nums[j]:
                lowpos = j

        temp = nums[i]
        nums[i] = nums[lowpos]
        nums[lowpos] = temp

        print(nums)

userList = [9,4,6,32,9,3,1,2]
sort(userList)
print(userList)