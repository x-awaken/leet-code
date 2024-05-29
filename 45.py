'''
45. 跳跃游戏 II
中等
给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。

每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:

0 <= j <= nums[i] 
i + j < n
返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。
'''
class Solution(object):
    def jump(self, nums):
        """
        计算每一跳能够到达的最远位置
        :type nums: List[int]
        :rtype: int
        """
        step = 0
        global_border = 0
        step_border = 0
        for i in range(len(nums)):
            if step_border<i:
                step += 1
                step_border = global_border
                if step_border >= len(nums)-1:
                    break
            global_border = max(global_border, nums[i]+i)
        return step

print(Solution().jump(nums = [2]))

            