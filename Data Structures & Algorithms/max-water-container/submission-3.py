class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_a = 0
        l = 0
        r = n - 1
        while l < r:
            cur_a = (r - l) * min(heights[r], heights[l])
            max_a = max(max_a, cur_a)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_a