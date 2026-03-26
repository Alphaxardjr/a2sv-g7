class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        len_p = len(p)
        len_s = len(s)
        
        if len_p > len_s:
            return result
        
        p_count = Counter(p)  # Count of chars in p
        window_count = Counter()
        
        for i in range(len_s):
            window_count[s[i]] += 1
            
            # Remove leftmost character when window is too big
            if i >= len_p:
                left_char = s[i - len_p]
                if window_count[left_char] == 1:
                    del window_count[left_char]
                else:
                    window_count[left_char] -= 1
            
            # Compare window with p
            if window_count == p_count:
                result.append(i - len_p + 1)
        
        return result