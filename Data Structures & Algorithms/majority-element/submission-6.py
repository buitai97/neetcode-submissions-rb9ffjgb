from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        result = heapq.nlargest(1, counts.keys(), key=counts.get)[0]

        return result