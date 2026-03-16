from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        i = 0

        while i < len(chars):
            j = i

            while j < len(chars) and chars[j] == chars[i]:
                j += 1

            count = j - i
            chars[write] = chars[i]
            write += 1

            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1

            i = j

        return write