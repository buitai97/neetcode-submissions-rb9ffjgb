class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = "".join(str(n) for n in digits)
        plusOne = int(total) + 1

        res = [n for n in str(plusOne)]

        return res