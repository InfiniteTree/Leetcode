import java.util.Arrays;
class Solution {
    public int maximumBeauty(int[] nums, int k) {
        // The susarray A will satisfy the condiction that A[r] - A[l] <= 2 * k
        Arrays.sort(nums);
        //System.out.println(Arrays.toString(nums));
        if(nums.length == 1) {return 1;}
        int l = 0, r = 0, res = 0;
        while (r <= nums.length-1){
            while (nums[r] - nums[l] > 2*k){
                l++;
            }
            res = res>(r-l+1) ? res:r-l+1;
            r++;
        }
        return res;
    }
}