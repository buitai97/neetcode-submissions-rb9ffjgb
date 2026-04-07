class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_a = 0

        for i in range(n):
            for j in range(i + 1,n):
                cur_a = (j - i) * min(heights[i], heights[j])
                max_a = max(max_a, cur_a)

        return max_a