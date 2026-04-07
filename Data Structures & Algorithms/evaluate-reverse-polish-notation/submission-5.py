class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            token = tokens[i]

            if (token == '-' or token == '+' or token == '*' or token == '/'):
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if (token =='/' and num1==0):
                    raise Exception("devided by zero")

                res = 0;
                match(token):
                    case '-':
                        res = num2-num1
                    case '+':
                        res = num2+num1
                    case '*':
                        res = num2*num1
                    case '/':
                        res = num2/num1
                stack.append(int(res))
            else:
                stack.append(int(token))

        return stack.pop()