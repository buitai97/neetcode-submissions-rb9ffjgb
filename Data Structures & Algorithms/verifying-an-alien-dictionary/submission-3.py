class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c: i for i,c in enumerate(order)}
        def compare(w1,w2):
            for i in range(len(w1)):
                if i == len(w2):
                    return False
                if w1[i]!= w2[i]: 
                    if order_index[w1[i]] > order_index[w2[i]]:
                        return False
                    break
            return True 
        for i in range(len(words) - 1):
            # compare words[i] to words[i+1]
            if not compare(words[i], words[i + 1]):
                return False
        return True

