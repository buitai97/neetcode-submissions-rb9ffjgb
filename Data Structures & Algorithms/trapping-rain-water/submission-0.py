class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        maxL = height[l]
        maxR = height[r]
        res = 0
        while(l < r):

            cur = min(maxL, maxR) - height[l]
            if (maxL < maxR):
                l += 1
                maxL = max(height[l], maxL)
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(height[r], maxR)
                res += maxR - height[r]
                         
        return res