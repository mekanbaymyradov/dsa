"""
Leetcode 28
Find the Index of First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0

Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
"""

def find_index(haystack: str, needle: str) -> int:
    words = haystack.split(needle)
    print(words)


if __name__ == "__main__":
    find_index("sadbutsad", "sad")
