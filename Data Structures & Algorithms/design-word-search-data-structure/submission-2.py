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
        def dfs(j, root):
            cur = self.root

            for i in range(len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        dfs(j, child)
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
        return dfs(0,self.root)


        
