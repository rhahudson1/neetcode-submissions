class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res =[]
        def backtracking(i, cur):
            if i == len(nums):
                res.append(cur.copy())
                return
            cur.append(nums[i])
            backtracking(i + 1, cur)
            cur.pop()
            
        backtracking(0,[])
        return res