class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # given an integer array nums
        # return k most frequent elemtns. 
        # find the frequency of the each element.
        # create a min heap of size k. 
        freq = Counter(nums)
        print(freq)
        for num, val in freq.items():
            print(num + " "+val)