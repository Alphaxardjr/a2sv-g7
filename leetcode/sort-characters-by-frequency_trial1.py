class Solution:
    def frequencySort(self, s: str) -> str:
        mapping = {}
        for ch in s:
            if ch not in mapping:
                mapping[ch] = 1
            else:
                mapping[ch] += 1

        sorted_chars = sorted(mapping.items(), key=lambda x: x[1], reverse=True)

        ans = []
        for ch, freq in sorted_chars:
            ans.append(ch * freq)
        
        return "".join(ans)