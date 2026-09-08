class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLastLetter = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # adds word to the dict 
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.isLastLetter = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur.children or char != ".":
                return False
            cur = cur.children[char]
        return True

        
