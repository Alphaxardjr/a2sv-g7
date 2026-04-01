class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # # convert the arr into ascii chars
        # arr = [ord(ch) - ord('a') for ch in s]

        # def shiftForward(start: int, end: int):
        #     for i in range(start, end + 1):
        #         arr[i] = (arr[i] + 1) % 26

        # def shiftBackward(start: int, end: int):
        #     for i in range(start, end + 1):
        #         arr[i] = (arr[i] - 1) % 26

    
        # for start, end, direction in shifts:
        #     if direction == 1:
        #         shiftForward(start, end)
        #     else:
        #         shiftBackward(start, end)

        # return "".join(chr(val + ord('a')) for val in arr)

        # OPTMAL SOLN

        n = len(s)
        arr = [0] * n 

        # counting shigt for each char
        for start, end, direction in shifts:
            shift = 1 if direction == 1 else -1
            arr[start] += shift
            if end + 1 < n:
                arr[end + 1] -= shift

        # running sum for shifts
        for i in range(1, n):
            arr[i] += arr[i - 1]

        # calculating shifts
        res = []
        for i, ch in enumerate(s):
            new_char = (ord(ch) - ord('a') + arr[i]) % 26
            res.append(chr(new_char + ord('a')))

        return "".join(res)
        
        
        