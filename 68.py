'''
68. 文本左右对齐
困难

给定一个单词数组 words 和一个长度 maxWidth ，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用 “贪心算法” 来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

注意:

单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。
 
'''
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        out = []
        last_line = []
        cur_len = 0
        for i, s in enumerate(words):
            cur_len += len(s)
            last_line.append(s)
            left_len = maxWidth - cur_len - len(last_line)+1
            if left_len < 0 :
                #complete one line without s
                t = last_line[0]
                if len(last_line) == 2:
                    t += ' '*(maxWidth-len(t))
                else:
                    left_len = maxWidth - cur_len + len(s)
                    base_spaces = ' '*(left_len//(len(last_line)-2))
                    more_spaces = base_spaces + ' '
                    more_cnt = left_len%(len(last_line)-2)
                    for j in range(1, len(last_line)-1):
                        if j <= more_cnt:
                            t+= more_spaces
                        else:
                            t+= base_spaces
                        t += last_line[j]
                out.append(t)

                #re init
                last_line = [s]
                cur_len = len(s)
                if i == len(words)-1:#last line
                    t = s + ' '*(maxWidth - len(s))
                    out.append(t)
            elif left_len == 0:
                #complete one line with s
                t = ' '.join(last_line)
                out.append(t)
                last_line = []
                cur_len = 0
            else:
                if i == len(words)-1:#last line
                    t = ' '.join(last_line) + ' '*left_len
                    out.append(t)
        return out

print(Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."],16))