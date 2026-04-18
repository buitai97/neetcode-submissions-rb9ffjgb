class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return - 1

        visited = set(deadends)
        steps = 0
        q = collections.deque()
        q.append("0000")
        possibilities = [[1,0,0,0],[-1,0,0,0],[0,1,0,0], [0,-1,0,0],[0,0,1,0], [0,0,-1,0], [0,0,0,1],[0,0,0,-1]]
        while q:
            
            for _ in range(len(q)):
                code = q.popleft()
                if code == target:
                    return steps
                for i in range(4):
                    digit = str((int(code[i]) + 1) % 10)
                    new_code = code[:i] + digit + code[i+1:]
                    if new_code not in visited:
                        visited.add(new_code)
                        q.append(new_code)
                    digit = str((int(code[i]) - 1 + 10) % 10)
                    new_code = code[:i] + digit + code[i+1:]
                    if new_code not in visited:
                        visited.add(new_code)
                        q.append(new_code)
            steps += 1
        return -1