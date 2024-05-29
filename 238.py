'''
238. 除自身以外数组的乘积
中等
给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。

题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

请 不要使用除法，且在 O(n) 时间复杂度内完成此题。
'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answers = [1]*n
        #left multi
        for i in range(n-1):
            if i == 0:
                answers[0] = nums[i]
            else:
                answers[i] = answers[i-1]*nums[i]
        
        # right multi
        right_total = 1
        for i in range(n-1,-1,-1):
            ans = 1
            if i < n-1:
                ans = ans*right_total
            if i > 0:
                ans = ans*answers[i-1]
            answers[i] = ans
            right_total*=nums[i]
        return answers
    
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        优雅一点，上一个有多余的乘法运输算
        """
        n = len(nums)
        answer = [1]*n
        #left total,从第一个元素开始需要
        for i in range(1,n):
            answer[i] = nums[i-1]*answer[i-1]
        
        #right total
        right_total = 1
        for i in range(n-1,-1,-1):
            answer[i] *= right_total
            right_total *= nums[i]