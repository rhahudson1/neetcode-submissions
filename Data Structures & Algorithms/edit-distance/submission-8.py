class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[float("inf")] * (len(word1)+1) for i in range(len(word2)+1)]
        #    w o r d 1
        #  w
        #  o
        #  r
        #  d
        #  2
        for i in range(len(word1)+1):
            cache[len(word2)][i] = len(word1) - i
        for j in range(len(word2) + 1):
            cache[j][len(word1)] = len(word2) - j
        
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2) -1,-1,-1):
                if word[i] == word[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    cache[i][j] = 1 + min(cache[i+1][j+1], cache[i+1][j], cache[i][j+1])
        return cache[0][0]
        