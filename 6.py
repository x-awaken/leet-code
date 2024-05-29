'''
6. Z 字形变换
中等
相关标签
相关企业
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        m = []
        period = 2*numRows-2 if numRows>2 else numRows
        for i in range(numRows):
            if i ==0 or i== numRows-1:
                for j in range(i,len(s), period):
                    m.append(s[j])
            else:
                l = i-period
                for l,k in zip(range(i,len(s),period),range(period-i,len(s),period)):
                    m.append(s[l])
                    m.append(s[k])
                if l+period < len(s):
                    m.append(s[l+period])
        return ''.join(m)
    
print(Solution().convert('AB',3))
                