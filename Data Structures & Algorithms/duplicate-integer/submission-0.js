class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        for (let i = 0; i >= nums.length -1;i++){
            temp = nums[i];
            for (let x = i+1; i>= nums.length-1;i++){
                if(temp === nums[x]){
                    return true
                }
            }
        }
        return false
    }

}
