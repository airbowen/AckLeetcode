class Solution:
    def findIntegers(self, n: int) -> int:
        @cache
        def dfs(i: int, pre1: bool, is_limit: bool) -> int:
            if i < 0:
                return 1
            up = n >> i & 1 if is_limit else 1
            res = dfs(i - 1, False, is_limit and up == 0)  # 填 0
            if not pre1 and up == 1:  # 可以填 1
                res += dfs(i - 1, True, is_limit)  # 填 1
            return res
        return dfs(n.bit_length() - 1, False, True)  # 从高位到低位
