class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # can only do one operation
        # insert a character at any position
        # delete a character at any position
        # replace a achracteer at any position

        # return min number of operations to make word1 equal to word 2
        cache = [[float("inf")] * (len(word2) + 1) for i in range(len(word1)+ 1)]
        # dp[i][j] = the minimum number of operations to convert word1[i:] into word2[j:]
        for j in range(len(word2) + 1): # fill bottom row
            cache[len(word1)][j] = len(word2) - j
        for i in range(len(word)+1): 
            cache[i][len(word2)] = len(word1) - i
        # initialize the base case of the array

        for i in range(len(word1)-1,-1,-1):
            for j in range(len(words2) - 1, -1,-1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    cache[i][j] = 1 + min(cache[i+1][j], cache[i][j+1], cache[i+1][j+1])     # those three options
        return cache[0][0]




        