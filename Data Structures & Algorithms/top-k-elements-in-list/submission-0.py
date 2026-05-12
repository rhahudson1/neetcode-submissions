class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        values = {}
        for i,n in enumerate(nums):
            values[n] += 1
        