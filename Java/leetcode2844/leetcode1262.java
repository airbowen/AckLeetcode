package leetcode2844;

public class leetcode1262 {
    class Solution {
        public int maxSumDivThree(int[] nums) {
            int n = nums.length;
            var f = new int[n + 1][3];
            f[0][1] = f[0][2] = Integer.MIN_VALUE;
            for (int i = 0; i < n; i++)
                for (int j = 0; j < 3; j++)
                    f[i + 1][j] = Math.max(f[i][j], f[i][(j + nums[i]) % 3] + nums[i]);
            return f[n][0];
        }
    }    
    
}
