from collections import defaultdict
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Brute-force solutin 
        # total = 0
        # for i in range(len(nums)):
        #     isodd = 0
        #     for mover in range(i, len(nums)):
        #         if nums[mover] % 2 != 0:
        #             isodd += 1
        #         if isodd == k:
        #             total += 1
        #         elif isodd > k:
        #             break 
        # return total

        # at most k
        def at_most(k):
            count = 0
            left = 0
            odd_count = 0
            n = len(nums)
            
            for right in range(n):
                if nums[right] % 2 != 0:
                    odd_count += 1
                while odd_count > k:
                    if nums[left] % 2 != 0:
                        odd_count -= 1
                    left += 1
                count += right - left + 1
            return count

        # Number of subarrays with exactly k odd numbers
        return at_most(k) - at_most(k - 1)