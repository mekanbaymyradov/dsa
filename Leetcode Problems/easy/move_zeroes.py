def move_zeroes(nums: list[int]):
    lastNoneZeroFoundAt = 0
    for curr in range(len(nums)):
        if nums[curr] != 0:
            nums[curr], nums[lastNoneZeroFoundAt] = nums[lastNoneZeroFoundAt], nums[curr]
            lastNoneZeroFoundAt += 1
    return nums


result = move_zeroes(nums=[1,2,3,4,0,0])
print(result)
