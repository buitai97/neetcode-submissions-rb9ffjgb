class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = 0
        stack = []
        for i in range(len(operations)):
            match operations[i]:
                case "+":
                    popVal = stack.pop()
                    val = popVal + stack[-1]
                    res += val
                    stack.append(popVal)
                    stack.append(val)
                case "C":
                    res -= stack.pop()
                    
                case "D":
                    val = stack[-1] * 2
                    res += val
                    stack.append(val)
                case _:
                    res += int(operations[i])
                    stack.append(int(operations[i]))
                    

        return res