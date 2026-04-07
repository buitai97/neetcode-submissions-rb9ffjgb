class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)] 
        for num in nums:
            count[num] = count.get(num, 0) + 1   
        for num, val in count.items():
            freq[val].append(num)
        res = []
        for i in range(len(freq)-1, -1, -1):
            for j in range(len(freq[i])):
                if k > 0:
                    res.append(freq[i][j])
                    k-=1
        return res
