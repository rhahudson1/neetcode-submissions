class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # given an integer array nums
        # return k most frequent elemtns. 
        # find the frequency of the each element.
        # create a min heap of size k. 
        freq = [[] for _ in range(len(nums)+1)]
        fre = Counter(nums)
        for num, val in fre.items():
            freq[val].append(num)
        res = []
        for i in range(len(nums),-1,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res