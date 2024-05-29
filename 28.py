'''
28. 找出字符串中第一个匹配项的下标
简单
相关标签
相关企业
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。

 

示例 1：

输入：haystack = "sadbutsad", needle = "sad"
输出：0
解释："sad" 在下标 0 和 6 处匹配。
第一个匹配项的下标是 0 ，所以返回 0 。
示例 2：

输入：haystack = "leetcode", needle = "leeto"
输出：-1
解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
 
'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)):
            if len(haystack)-i < len(needle):
                return -1
            matched = True
            for j in range(len(needle)):
                if i+j >= len(haystack):
                    break
                if haystack[i+j] != needle[j]:
                    matched= False
            
            if matched:
                return i
        return -1

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)
        next = [0]*len(needle)
        for i in range(2,m):
            if needle[i-1] == needle[next[i-1]]:
                next[i] = next[i-1]+1
            else:
                k = next[next[i-1]]
                while needle[i-1] != needle[k] and k !=0:
                    k = next[k]
                
                if needle[i-1] == needle[k]:
                    next[i] = k+1
                else:
                    next[i] = k
        
        i = 0
        j = 0
        while i<n and j<m:
            if haystack[i] ==  needle[j]:
                i+=1
                j+=1
            elif j == 0:
                i+=1
            else:
                j = next[j]
            
        if j == m:
            return i-m
        return -1

print(Solution().strStr('ababcaababcaabc','ababcaabc'))