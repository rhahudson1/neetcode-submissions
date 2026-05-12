class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l , r = 0, len(numbers) - 1
        while l < r:
            tempSum = numbers[l] + numbers[r]
            if tempSum < target:
                l += 1
            elif tempSum > target:
                r -= 1
            elif tempSum == target:
                return [l,r]
