class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        for (let i = 0; i <= nums.length -1;i++){
            for (let x = i+1; x<= nums.length-1; x++){
                if(nums[i] === nums[x]){
                    return true
                }
            }
        }
        return false
    }

}
