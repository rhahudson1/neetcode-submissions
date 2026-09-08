class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        curIdx = len(s) 
        dp = [False] * (len(s) + 1)
        dp[curIdx] = True
        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                if len(word) + i <= len(s) and s[i:len(word) + i] == word:
                    dp[i] = dp[i + len(word) + 1]
        if dp[0]:
            return True
        return False

        


        