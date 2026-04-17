class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_map = {0:0}
        max_ = 0 
        for num in nums:
            if num not in count_map:
                count_map[num] = 1

            else:
                count_map[num] += 1
            if count_map[num] > count_map[max_]:
                max_ = num
        return max_