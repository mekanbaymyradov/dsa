"""
Running Sum of 1d Array

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Time Complexity: $O(n)$, We only iterate through the list once. 

Space Complexity: $O(1)$, We are modifying the input directly
"""

def runningSum(nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        return nums


result = runningSum(nums=[1,1,1,1,1])
print(result)
                