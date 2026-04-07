class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                print(i, j)
                print(s[i:j + 1])
                if self.isPalindrome(s[i:j + 1]):
                    res += 1
        return res
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            r -= 1
            l += 1
        return True