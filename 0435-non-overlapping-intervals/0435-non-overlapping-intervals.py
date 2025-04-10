class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key= lambda x: x[1])
        result_count = 0
        total_interval = [sorted_intervals[0][0], sorted_intervals[0][1]]
        print(sorted_intervals)

        for interval in sorted_intervals:
            if interval[0] < total_interval[1]:
                    result_count += 1
            else:
                total_interval = interval

        return result_count - 1