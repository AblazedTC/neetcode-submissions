class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]

        for start, end in intervals:
            if start <= ans[-1][1]:
                ans[-1][1] = max(end, ans[-1][1])
            else:
                ans.append([start, end])
        return ans


        