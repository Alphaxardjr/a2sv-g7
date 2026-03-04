class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # [0 1 2 3 4 5 ]
        # 1  + "1" = 2
        # "1"+ 1 = 11
    
        left = 0
        right = len(s)-1
        while left < right:
            s[left],s[right] = s[right],s[left]
            left +=1
            right -=1