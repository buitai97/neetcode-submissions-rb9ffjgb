class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, val in enumerate(temperatures):
            if stack:
                while(stack and val > stack[-1][1]):
                    topIndex, topVal = stack.pop()
                    result[topIndex] = i - topIndex
                    
            stack.append((i, val))

        while stack:
            topIndex, topVal = stack[-1]
            result[topIndex] = 0
            stack.pop()
        return result