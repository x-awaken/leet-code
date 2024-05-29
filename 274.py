'''
274. H 指数
中等

给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数。计算并返回该研究者的 h 指数。

根据维基百科上 h 指数的定义：h 代表“高引用次数” ，一名科研人员的 h 指数 是指他（她）至少发表了 h 篇论文，并且 至少 有 h 篇论文被引用次数大于等于 h 。如果 h 有多种可能的值，h 指数 是其中最大的那个。

'''
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        c = sorted(citations,reverse=True)
        for i in range(len(c)):
            if c[i]/(i+1)<1:
                return i
        return i+1
    
    def hIndex(self, citations):
        """

        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        m = [0]*(n+1)
        for x in citations:
            if x >=n:
                m[n]+=1
            else:
                m[x] +=1
        total = 0 #代表引用数大等于i的文章数量
        for i in range(n,-1,-1):
            total += m[i]
            if total >=i :
                break
        return i

print(Solution().hIndex([1,2,3,4,5]))