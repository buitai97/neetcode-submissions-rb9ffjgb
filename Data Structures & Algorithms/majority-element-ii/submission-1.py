from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        keys = [k for k,v in counter.items() if v > len(nums) / 3]
        return keys