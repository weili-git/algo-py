class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)==0 or newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        res = []
        low = None
        high = None
        flag = False
        for interval in intervals:
            if low==None:
                if interval[1]<newInterval[0]:  # right side
                    res += [interval]
                elif interval[0] > newInterval[1]: # left side
                    res += [newInterval, interval]
                    low = newInterval[0]
                    high = newInterval[1]
                    flag = True
                else: # overlap
                    low = min(interval[0], newInterval[0])
                    high = max(interval[1], newInterval[1])
            else:
                if not flag: # still merging
                    if high < interval[0]:
                        res += [[low, high], interval]
                        flag = True
                    else:
                        high = max(interval[1], high)
                else:
                    res += [interval]
        if not flag:
            res += [[low, high]]
        return res
