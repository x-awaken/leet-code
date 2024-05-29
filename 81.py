import copy
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums = copy.deepcopy(nums1)
        i,j,k = 0,0,0
        while i<m and j<n:
            if nums[i] > nums2[j]:
                nums1[k] = nums2[j]
                j = j+1
            else:
                nums1[k] =  nums[i] 
                i = i+1
            k+=1

        if i>=m:
            left_len = n-j
            for l in range(left_len):
                nums1[k+l] = nums2[j+l]
        elif j>=n:
            left_len = m-i
            for l in range(left_len):
                nums1[k+l] = nums[i+l]

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i,j,k = m-1,n-1,m+n-1
        while True:
            if i>=0 and j>=0:
                if nums1[i] > nums2[j]:
                    nums1[k] = nums1[i]
                    i = i-1
                else:
                    nums1[k] =  nums2[j] 
                    j = j-1
            elif i<0 and j<0:
                break
            elif i<0:
                nums1[k] =  nums2[j]
                j = j-1
            elif j<0:
                nums1[k] =  nums1[i] 
                i = i-1
            k = k-1

s = Solution()
nums1 = [2,0]
s.merge(nums1 , m = 1, nums2 = [1], n = 1)
print(nums1)