
"""
1. Brute force method (Nested Loops)

Time Complexity: $O(n^2)$. As the list grows, the number of comparisons grows quadratically

Space Complexity: $O(1)$. We aren't storing any extra data, which is its only real advantage.

"""
def two_sum_m1(nums: list[int], target: int):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


###############################################################################################
"""
2. Hash Map (One-Pass)
Time Complexity: $O(n)$. We only traverse the list once.
Space Complexity: $O(n)$. In the worst case (where the pair is at the very end), we store almost every number in the map.

"""

def two_sum_m2(nums: list[int], target: int):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
