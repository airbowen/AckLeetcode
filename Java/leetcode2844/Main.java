package leetcode2844;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // 示例测试用例
        String num1 = "2245047";
        String num2 = "123456789";
        String num3 = "1000";
        
        System.out.println("Minimum operations for " + num1 + ": " + solution.minimumOperations(num1));  // 输出示例
        System.out.println("Minimum operations for " + num2 + ": " + solution.minimumOperations(num2));
        System.out.println("Minimum operations for " + num3 + ": " + solution.minimumOperations(num3));
    }
}
