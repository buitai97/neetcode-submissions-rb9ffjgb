class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for string in strs:
            sorted_string = sorted(string)
            key = "".join(sorted_string)
            res.setdefault(key, []).append(string)
        values = list(res.values())

        return values