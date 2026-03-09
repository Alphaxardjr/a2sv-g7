class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count =0
        # for cookie in s:
        #     for i in range(len(g)):
        #         if g[i] >=0 and cookie >= g[i]:
        #             g[i]= -g[i]
        #             count +=1
        #             break

        sp= 0
        gp = 0
        s.sort()
        g.sort()

        while sp < len(s) and gp < len(g):
            if s[sp] >= g[gp]:
                count += 1
                gp += 1
            sp += 1
                
        return count
