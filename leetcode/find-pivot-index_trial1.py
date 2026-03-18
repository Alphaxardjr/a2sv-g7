class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0]* (n+1)

        # building a prefix sum
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        total = prefix[n]
        for i in range(n):
            left = prefix[i]
            right = total - prefix[i+1]
            if left == right:
                return i
        return -1