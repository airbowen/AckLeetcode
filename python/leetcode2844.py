class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num)
        found0 = found5 = False  # 初始化标志
        for i in range(n - 1, -1, -1):  # 从右向左遍历字符串
            c = num[i]
            if found0 and c in "05" or found5 and c in "27":  # 如果找到匹配的字符对
                return n - i - 2  # 返回需要删除的字符数
            if c == '0':  # 如果找到 '0'
                found0 = True
            elif c == '5':  # 如果找到 '5'
                found5 = True
        return n - found0  # 如果没有找到符合条件的字符对，返回删除所有字符的数量减去一个 '0' 的数量

# 示例用法
solution = Solution()
print(solution.minimumOperations("2245047"))  # 输出示例
