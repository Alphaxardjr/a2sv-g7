class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 1  
        start = 0
        last_pair_index = -1 

        for end in range(1, n):
            if s[end] == s[end-1]:
                if last_pair_index >= 0:
                    start = last_pair_index + 1
                last_pair_index = end - 1
            max_len = max(max_len, end - start + 1)

        return max_len