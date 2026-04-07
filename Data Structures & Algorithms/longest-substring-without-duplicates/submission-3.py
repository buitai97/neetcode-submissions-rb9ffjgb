class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        charSet = set()
        left = 0
        maxSize = 0
        for right in range(0, n):
            while s[right] in charSet:
                
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            maxSize = max(maxSize, right - left + 1)
        return maxSize
