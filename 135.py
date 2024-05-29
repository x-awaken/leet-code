'''
135. 分发糖果
困难
n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。

你需要按照以下要求，给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
相邻两个孩子评分更高的孩子会获得更多的糖果。
请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。
'''
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        polar = 1
        n = len(ratings)
        total = 0
        cur_total = 1
        cur_cnt = 1
        down_cnt = 0
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                if down_cnt == 0:
                    cur_cnt += 1
                    cur_total += cur_cnt
                    polar = cur_cnt
                else:
                    down_cnt = 0
                    total+= cur_total
                    cur_total = 2
                    polar= 2
                    cur_cnt = 2
            elif ratings[i]==ratings[i-1]:
                cur_cnt = 1
                polar = 1
                down_cnt = 0
                total+= cur_total
                cur_total = 1
            else:
                down_cnt += 1
                cur_total += down_cnt
                if down_cnt >= polar:
                    cur_total += 1
                    polar += 1
        total += cur_total
        return total


print(Solution().candy([1,3,4,4,2]))
