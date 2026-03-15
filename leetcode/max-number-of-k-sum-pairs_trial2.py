class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        counter = 0
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i] >0 and nums[j]>0 and nums[i] + nums[j] == k:
        #             counter +=1
        #             nums[i]= - nums[i]
        #             nums[j] = - nums[j]

        left,right = 0,n-1
        while left <right:
            run_sum = nums[left] + nums[right]
            if run_sum == k:
                counter +=1
                left +=1
                right -=1
            elif run_sum > k:
                right -=1
            else:
                left +=1
                
        return counter
        