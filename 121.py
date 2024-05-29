class Solution(object):
    def maxProfit(self, prices):
        """
        121. 买卖股票的最佳时机
        给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

        你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

        返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
        暴力搜索-超时
        :type prices: List[int]
        :rtype: int
        """
        p = 0
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                if prices[j]-prices[i] > p:
                    p = prices[j]-prices[i]
        return p
    def maxProfit(self, prices):
        """
        记录高低点位置，判断明天价格，是否可构成更大的利益（包括两种情况，一种是突破历史高点，一种是与历史低点的差值大于当前最大利益）
        :type prices: List[int]
        :rtype: int
        """
        p = 0
        if len(prices) == 0:
            return 0
        min1,max,min2 = 0,0,0
        for i in range(len(prices)):
            if prices[min2] > prices[i]:
                min2 = i
            if prices[i]-prices[min2] >= prices[max]-prices[min1]:
                min1=min2
                max = i
            if prices[i]>=prices[max]:
                max = i

        return prices[max]-prices[min1]
    
    def maxProfit(self, prices):
        """
        更加简洁的思想，考虑当天卖出能够达到的最大利益（与历史低点相减），同时记录记录当前全局的最大利益。
        :type prices: List[int]
        :rtype: int
        """
        maxp = 0
        minp = prices[0]
        for p in prices:
            maxp = max(p-minp,maxp)
            minp = min(p,minp)
        return maxp
s = Solution()
print(s.maxProfit([7,2,5,3,6,4]))