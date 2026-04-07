class WordDictionary:

    def __init__(self):
        self.dictionary = []

    def addWord(self, word: str) -> None:
        self.dictionary.append(word)

    def search(self, word: str) -> bool:
        for storedWord in self.dictionary:
            if len(storedWord)!=len(word):
                continue
            i = 0
            while i < len(word):
                if word[i] == storedWord[i] or word[i] == '.':
                    i+=1;
                else:
                    break
                
            if i == len(word):
                return True
        return False