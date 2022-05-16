def sort(nums):
    for i in range(5):
        min=i
        for j in range(i,6):
            if nums[j]<nums[min]:
                min=j
        temp=nums[i]
        nums[i]=nums[min]
        nums[min]=temp
nums=[5,3,6,7,8,2]
sort(nums)
print(nums)