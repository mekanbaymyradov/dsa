def move_zeroes(nums: list[int]):
    lastNoneZeroFoundAt = 0
    for curr in range(len(nums)):
        if nums[curr] != 0:
            nums[curr], nums[lastNoneZeroFoundAt] = nums[lastNoneZeroFoundAt], nums[curr]
            lastNoneZeroFoundAt += 1
            print(nums)
    return nums


result = move_zeroes(nums=[0,1,0,3,12])
print(result)
