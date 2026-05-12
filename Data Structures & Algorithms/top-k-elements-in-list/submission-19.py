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
        print(freq)
        return 8