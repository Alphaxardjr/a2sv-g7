class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        runningSum = [0]*n
        total = 0
        for i in range(n):
            total +=nums[i]
            runningSum[i] = total
        return  runningSum
            
        