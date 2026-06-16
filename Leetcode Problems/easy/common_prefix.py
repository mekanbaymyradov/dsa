"""
14. Longest Common Prefix
Easy
Write a function to find the longest common prefix string amongst an array of strings.

Input: strs = ["flower","flow","flight"]
Output: "fl"

If there is no common prefix, return an empty string "".
"""

def longestCommonPrefix(strs: list[str]) -> str:
        pref = strs[0]
        pref_len = len(pref)
        for s in strs[1:]:
            while pref != s[0:pref_len]:
                pref_len -= 1
                if pref_len == 0:
                    return ""
                
                pref = pref[0:pref_len]
        return pref
                
            
            
            
                


result = longestCommonPrefix(["flower","flow","flight"])
print(result)