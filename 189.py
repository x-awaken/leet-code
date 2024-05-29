
import math
class Solution(object):
    def rotate(self, nums, k):
        """
        189.轮转数组：给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k%l
        def reverse(v, start, end):
            for i in range(start, start + int((end-start)/2)):
                tmp = v[i]
                v[i] = v[end-i+start-1]
                v[end-i+start-1] = tmp
        reverse(nums,0,l-k)
        print(nums)
        reverse(nums,l-k,l)
        print(nums)
        reverse(nums,0,l)
    
    def rotate(self, nums, k):
        """
        模 n 的整数环
        环状替换，若len(nums)和k为互质数，即最大公约数为1，那么k是Z_n环的单位，即存在b使得k*b%n =1
        也就是说，元素i经过b跳之后，会到达元素i+1，依次类推可以到达n的所有位置。
        结论：如果GCD(N,K)=1，那么可以k跳可以遍历所有元素
        对于此题目，如果GCD(N,K)=m,那么GCD(N/m,k/m)=1
        对N的环状替换相当于对N/m环替换m次（复制m次N/m环）
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def gcd(m,n):
            if m<n:
                tmp = m
                m=n
                n= tmp
            while n!=0:
                tmp = n
                n = m-n
                m = tmp
                if m<n:
                    tmp = m
                    m=n
                    n= tmp
            return m
        
        l = len(nums)
        a = gcd(l,k)
        for i in range(a):
            start = i
            next = i
            s = nums[i]
            while True:
                cur = next
                next = (cur+k)%l
                tmp = nums[next]
                nums[next] = s
                s = tmp
                if next == start:
                    break


s = Solution()
l = [1,2,3,4,5,6,7,8]
s.rotate(l,2)
print(l)