class Solution:
    def maxArea(self, height: List[int]) -> int:
        # print(sorted([1,8,6,2,5,4,8,3,7]))
        # fistline = (0,0) and (0,1)
        # 2line = (1,0) and (1,8)
        # [8,7,2,1]
        #  | !  
        # [3,4,7]
        n = len(height)
        amount = 0
        start = 0
        end = n-1
        for i in range(n):
            Y_axis = min(height[start],height[end])
            X_axis = end -start
            water_level =  X_axis *  Y_axis
            if amount < water_level:
                amount = water_level
            if height[start]>height[end]:
                end -=1
            else:
                start +=1
        return amount


        #  for i in range(n):
        #     for j in range(i+1,n):
        #         Y_axis = min(height[i],height[j])
        #         X_axis = j -i
        #         water_level =  X_axis *  Y_axis
        #         if amount < water_level:
        #             amount = water_level

        
        # for i in range(n):
            
              

        # return amount


