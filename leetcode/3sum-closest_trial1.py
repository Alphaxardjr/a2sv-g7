class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        n = len(nums)      
        for i in range(n-2):
            left = i + 1
            right = n-1
   
            while left < right:
                max_curr = nums[i] + nums[left] + nums[right]
                if abs(max_curr - target)< abs(closest-target):
                    closest = max_curr
                if max_curr < target:
                    left +=1
                elif max_curr > target:
                    right -=1
                else:
                    return max_curr
        return closest
