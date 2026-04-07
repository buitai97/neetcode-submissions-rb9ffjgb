class Solution:
    def isHappy(self, n: int) -> bool:
        found = set()
        total = n
        while True:
            digitsSQRT = [(int(d))**2 for d in str(total)]
            print(digitsSQRT)
            total = sum(digitsSQRT)
            print(total)
            if total == 1:
                return True
            if total in found:
                return False
            
            found.add(total)