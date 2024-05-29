'''
14. 最长公共前缀
简单
相关标签
相关企业
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        if len(strs) == 0:
            return ""
        min_j = 500
        for s in strs:
            min_j = min(min_j, len(s))
        
        for j in range(min_j):
            for i in range(n):
                if strs[i][j] != strs[0][j]:
                    return strs[0][:j] if j >0 else ""
        return strs[0][:j+1] if min_j > 0 else ""

print(Solution().longestCommonPrefix(["flower","flow","flight"]))