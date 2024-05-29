class Solution(object):
    def removeElement(self, nums, val):
        """
        88. 合并两个有序数组
        首尾指针
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j=len(nums)-1
        while i<=j:
            if nums[i] == val:
                while i<j and nums[j]==val:
                    if i==j:
                        break
                    j-=1
                if i<j:
                    nums[i] = nums[j]
                    j -= 1 
                    i+=1
                else:
                    break
            else:
                i += 1
        return i

class Solution(object):
    def removeElement(self, nums, val):
        """
        快慢指针
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left=0
        for right in range (len(nums)):
            if nums[right]!=val:
                nums[left]=nums[right]
                left+=1

        return left
s = Solution()
l = [1,2,2,3]
n = s.removeElement(l,3)
print(l[:n])
