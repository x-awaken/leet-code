'''
58. 最后一个单词的长度
简单
相关标签
相关企业
给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。

单词 是指仅由字母组成、不包含任何空格字符的最大
子字符串。
'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        for i in range(len(s)-1,-1,-1):
            if s[i]!= ' ':
                l += 1
            elif l >0:
                break
        return l
    