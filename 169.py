class Solution(object):
    def majorityElement(self, nums):
        """
        169. 多数元素
        给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

        你可以假设数组是非空的，并且给定的数组总是存在多数元素。
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for n in nums:
            if n not in d:
                d[n]= 1
            else:
                d[n]+=1
        max=-1
        target = -1
        for n,t in d.items():
            if t>max:
                target=n
                max = t
        return target
    def majorityElement(self, nums):
        """
        摩尔投票
        核心思想就是抵消，由于数组肯定存在大于N/2个的众数，众数肯定可以抵消掉其他元素
        如果当前拟定众数是真正的众数，则全部遍历后score肯定大于0
        如果当前拟定众数是错的，那么其他元素中存在众数，一定会把当前拟定众数中和掉
        :type nums: List[int]
        :rtype: int
        """
        score = 0
        for i in len(nums):
            if score == 0:
                t = i
            if i == t:
                score += 1
            else:
                score -= 1
        return t
            


    
            
        
            
