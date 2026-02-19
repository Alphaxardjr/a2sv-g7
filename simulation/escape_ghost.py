class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        a = target[0]
        b = target[1]
        surv = abs(a-0) + abs(b-0)
        # print(surv)
        for x, y in ghosts:
            dist = abs(x-a) + abs(y-b)
            # print(dist,surv)
            if dist <= surv:
                return False
        return True



# r=0
#         for i in range(2,n+1):
#             r=(r+k)%i
#         return r+1

# https://cp-training-tracker.vercel.app/