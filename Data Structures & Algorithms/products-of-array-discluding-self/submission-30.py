class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output: where output[i] represents the product of nums not inlcuding nums[i]
        '''
        nums [1,2,4,6]
        
        prefix -> represent the product of all numbers before
        [1,1,2,8]
        prefix[i] = prefix[i-1] * nums[i-1]

        postfix -> represent the product of all the numbers after (start from end)
        [48, 24, 6, 1]
        postfix[i] =  nums[i+1] * postfix[i+1]

        output[i] = prefix[i] * postfix[i]
        '''
        prefix = [1] * len(nums)
        postfix = [1] * len(nums) # length = 4
        output = [1] * len(nums)
        for i in range(2,len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        for j in range(len(nums)-2,-1,-1):
            postfix[j] = postfix[j+1] * nums[j+1]
        for i in range(len(nums)):
            output[i] = prefix[i] * postfix[i]
        print(prefix)
        print(postfix)
        return output
        