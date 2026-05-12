class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for words in strs:
            count = [0] * 26
            for s in words:
                count[ord('s') - ord('a')] += 1
            res[count] = words
        return list(res)


