
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count = Counter(t)  # Count of chars in t
        window_count = {}
        required = len(t_count)  # Number of unique chars to match
        formed = 0  # How many unique chars in current window match required count

        left = 0
        min_len = float('inf')
        min_window = ""

        # Expand the window
        for right, char in enumerate(s):
            window_count[char] = window_count.get(char, 0) + 1

            # Check if current char completes the requirement for this char
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1

            # Try to shrink the window from the left
            while left <= right and formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right+1]

                # Remove the left char from window
                left_char = s[left]
                window_count[left_char] -= 1
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    formed -= 1

                left += 1

        return min_window