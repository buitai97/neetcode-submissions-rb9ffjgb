class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        checkMap = defaultdict(bool)
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j + 1] in checkMap: 
                    res += 1
                elif self.isPalindrome(s[i:j + 1]):
                    checkMap[s[i:j + 1]] = True
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