'''
55. 跳跃游戏
给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。
'''
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<=1:
            return True
        p2=0
        for i in range(len(nums)):
            if i>p2:
                return False
            p2 = max(nums[i]+i,p2)
            if p2 >= len(nums)-1:
                return True
        return False
    
print(Solution().canJump(nums = [2,3,1,1,4]))
print(Solution().canJump(nums = [3,2,1,0,4]))


