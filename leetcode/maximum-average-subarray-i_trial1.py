class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_average = sum(nums[:k])
        left = 0
        right = k
        # [1,12,-5,-6,50,3]
        #  l        r
        current_av = max_average
        while right <len(nums):
            current_av = (current_av - nums[left] + nums[right])
            max_average = max(max_average,current_av)
            left +=1
            right += 1
        return max_average/k


# class Solution:
    # def findMaxAverage(self, nums: List[int], k: int) -> float:
        
    #     window_sum = 0
    #     max_sum = float(-inf)
    #     left = 0

    #     for right in range(len(nums)):
    #         window_sum += nums[right]

    #         if right - left + 1 > k :
    #             window_sum -= nums[left]
    #             left += 1

    #         max_sum = max(max_sum, window_sum)

    #     return max_sum / k