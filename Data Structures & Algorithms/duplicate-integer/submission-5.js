class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        for (let i = 0; i <= nums.length -1;i++){
            x = i+1
                if(nums[i] === nums[x]){
                    return true
                }
            
        }
        return false
    }

}
