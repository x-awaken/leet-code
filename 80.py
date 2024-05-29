class Solution(object):
    def removeDuplicates(self, nums):
        """
        80. 删除有序数组中的重复项 II
        :type nums: List[int]
        :rtype: int
        """
        p1,p2 = 2,2
        n = []
        l = len(nums)
        if l < 3:
            return l
        while p2<l:
            if nums[p2]==nums[p2-1] and nums[p2]!=nums[p2-2] or nums[p2] != nums[p2-1]:
                if p2-p1>=2:
                    nums[p1] = nums[p2]
                else:
                    n.append(p1,nums[p2])
                p1+=1
            p2+=1
        for p, k in n:
            nums[p] = k
        return p1
    
    def removeDuplicates(self, nums) :
        def solve(k):
            u = 0
            for x in nums:
                if u < k or nums[u - k] != x:
                    nums[u] = x
                    u += 1
            return u
        return solve(2)
