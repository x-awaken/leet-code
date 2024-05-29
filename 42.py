'''
42. 接雨水
困难
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
'''
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        left_max = [0]*n
        left_max[0] = height[0]
        for i in range(1,n):
            left_max[i] = max(left_max[i-1], height[i])
        
        right_max = height[n-1]
        total = 0
        for i in range(n-2,0,-1):
            total += max(0,min(left_max[i-1],right_max)-height[i])
            right_max = max(right_max, height[i])
        return total

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        追求空间复杂度O(1)
        """
        n=len(height)
        if n <=2:
            return 0
        left_max = height[0]
        right_max = height[-1]
        left = 1
        right = n-2
        total = 0
        while left <= right:
            if left_max <= right_max:
                total += max(0,left_max-height[left])
                left_max = max(left_max,height[left])
                left += 1
            elif right_max <left_max:
                total += max(0,right_max-height[right])
                right_max = max(right_max, height[right])
                right-=1
        return total
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))