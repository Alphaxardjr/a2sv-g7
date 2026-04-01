class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left,right = 0,int(math.isqrt(c))
        
        while left <= right:
            total= left**2 + right**2
            if total==c:
                return True
            elif total < c:
                left +=1
            elif total >c:
                right -=1
            else:
                return False
        return False