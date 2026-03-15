class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapping = {} 
        left = 0
        right = 0
        max_len = 0
        # "abcabcbb"
        while right < len(s):
            if s[right] not in mapping:
                mapping[s[right]] = True
                max_len = max(max_len, right - left + 1)
                right += 1
            else:
                mapping.pop(s[left])
                left += 1

        return max_len
