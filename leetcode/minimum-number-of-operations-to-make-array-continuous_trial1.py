class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        diff = nums[-1] -nums[0]
        unique = Counter(nums)
        operations =0

        if all(v == 1 for v in unique.values()) and  diff == len(nums)-1:
            return 0
    
        for key, value in unique.items():
            if value > 1:
                operations += value - 1
            
        left = 0
        uniqueKey = sorted(unique.keys())
        maxWindow = 0
        for right in range(len(uniqueKey)):
            while uniqueKey[right] - uniqueKey[left] >= len(nums):
                left +=1
            maxWindow = max(maxWindow, right -left +1)
        operations += len(uniqueKey) - maxWindow


            
        return operations
            

        