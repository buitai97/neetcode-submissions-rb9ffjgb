from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        key, val = counts.most_common(1)[0]

        return key