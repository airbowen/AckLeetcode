class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num)
        min_ops = float('inf')

        # 查找以 tail 结尾的最小操作数
        def find_ops(tail: str) -> int:
            second_char_found = False
            first_char_index = -1

            for i in range(n-1, -1, -1):
                if second_char_found:
                    if num[i] == tail[0]:
                        first_char_index = i
                        break
                else:
                    if num[i] == tail[1]:
                        second_char_found = True
            
            if first_char_index == -1:
                return float('inf')  # 如果没有找到匹配的字符对，返回无限大
            
            return n - first_char_index - 2

        # 考虑所有可能的尾部字符对
        tails = ["00", "25", "50", "75"]
        for tail in tails:
            min_ops = min(min_ops, find_ops(tail))
        
        # 考虑只有一个零的情况
        if '0' in num:
            min_ops = min(min_ops, n - 1)

        return min_ops

# 示例用法
solution = Solution()
print(solution.minimumOperations("2245047"))  # 输出示例
