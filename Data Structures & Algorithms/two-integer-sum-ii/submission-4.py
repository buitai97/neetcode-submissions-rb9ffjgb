class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        curSum = 0
        L, R = 0,len(numbers)-1

        while R > L:
            curSum = numbers[R] + numbers[L]
            if  curSum == target:
                return [L + 1, R +1]
            elif curSum < target:
                L += 1
            elif curSum > target:
                R -= 1
               