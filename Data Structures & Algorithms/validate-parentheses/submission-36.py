class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_symbols = ['{', '(' , '[']
        close_symbols = ['}', ')', ']']
        for char in s:
            if char in open_symbols:
                stack.append(char)
            if char in close_symbols:
                if not stack:
                    return False
                open_symbol = stack.pop()
                if open_symbols.index(open_symbol) != close_symbols.index(char):
                    return False

        return not stack
            