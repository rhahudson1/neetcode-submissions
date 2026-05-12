class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0,len(heights)-1
        max_area = 0
        while l <= r:
            width = r - l
            max_height = max(heights[l], heights[r])