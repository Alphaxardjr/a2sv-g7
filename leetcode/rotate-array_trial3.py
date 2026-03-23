class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # USING 
        n= len(nums)
        # for _ in range(k):
        #     last =nums[-1]
        #     for i in range(n-1,0,-1):
        #         nums[i] = nums[i-1]
        #     nums[0]= last
        # return nums

        # i = 0
        # while i<k:
        #     el = nums.pop()
        #     nums.insert(0,el)
        #     i+=1

        temp = []
        k %=n
        d= n-k
        for i in range(d,n):
            temp.append(nums[i])
        for i in range(d):
            temp.append(nums[i])
        nums[:] =temp
    

         
