class Solution(object):
    def removeDuplicates(self, nums):
        """
        26. 删除有序数组中的重复项
        快慢指针
        :type nums: List[int]
        :rtype: int
        """
        p1,p2 = 1,1
        l = len(nums)
        if l <= 1 :
            return l
        while p2<l:
            if nums[p2-1] != nums[p2]:
                nums[p1] = nums[p2]
                p1 += 1
            p2+=1
        return p1
    