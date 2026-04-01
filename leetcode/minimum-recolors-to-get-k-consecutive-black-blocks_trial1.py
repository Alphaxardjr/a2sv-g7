class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        # Count ws in range of k
        current_white = sum(1 for i in range(k) if blocks[i] == 'W')
        min_ops = current_white

        for i in range(k, n):
            if blocks[i - k] == 'W':
                current_white -= 1
           
            if blocks[i] == 'W':
                current_white += 1
           
            min_ops = min(min_ops, current_white)

        return min_ops