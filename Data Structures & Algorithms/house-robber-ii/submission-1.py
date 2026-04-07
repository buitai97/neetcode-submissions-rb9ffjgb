class Solution:
    def rob(self, nums: List[int]) -> int:
        trip1, trip2 = 0,0
        trip3, trip4 = 0,0
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums) - 1):
            temp = trip2
            trip2 = max(trip1 + nums[i], trip2)
            trip1 = temp

        for i in range(1, len(nums)):
            temp = trip4
            trip4 = max(trip3 + nums[i], trip4)
            trip3 = temp
        return max(trip2, trip4)