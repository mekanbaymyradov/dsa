class Solution:
    def isPlandrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reverse = 0
        xcopy = x

        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            print('reverse', reverse)
            x //= 10
            print('x', x)
        return reverse == xcopy
    
solution = Solution()
x = int(input())
result = solution.isPlandrome(x)
print(result)

"""
Input: 121

First Loop:
    reverse = 1
    x = 12
Second Loop:
    reverse = 12
    x = 1
Third Loop:
    reverse = 121
    x = 0
Return: 
    False


Input: 567

First Loop:
    reverse = 7
    x = 56
Second Loop:
    reverse = 76
    x = 5
Third Loop:
    reverse = 765
    x = 0
Return:
    False

"""