nums = [2,7,11,15,18]
target = 29
def sum_two(nums,target):
    for num in nums:
        x = 0  
        for item in range(len(nums)-1):
            if num != nums[x]:
                sum = nums[x] + num
                if sum == target:
                    return((x,(nums.index(num))))
            x += 1
