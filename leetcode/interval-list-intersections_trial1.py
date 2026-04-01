class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        fp, sp = 0, 0
        result = []
        fn = len(firstList)
        fs = len(secondList)

        while fp < fn and sp < fs:

            start = max(firstList[fp][0], secondList[sp][0])
            end = min(firstList[fp][1], secondList[sp][1])

            if start <= end:
                result.append([start, end])

            if firstList[fp][1] < secondList[sp][1]:
                fp += 1
            else:
                sp += 1

        return result