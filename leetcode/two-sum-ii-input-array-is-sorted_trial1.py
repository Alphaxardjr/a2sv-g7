class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1
        found = False
        while left < right:
            current = numbers[left] + numbers[right]
            if current == target:
                return [left + 1,right +1]
            elif current < target:
                left += 1
            else:
                right -=1
            # if numbers[left] + numbers[right]== target:
            #     return [left + 1,right +1]
            # left +=1
            # right -=1
        