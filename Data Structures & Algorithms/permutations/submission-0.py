class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res =[]
        def backtracking(i, cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
            cur.append(nums[i])
            backtracking(i + 1, cur)
            cur.pop()
            
        backtracking(0,[])