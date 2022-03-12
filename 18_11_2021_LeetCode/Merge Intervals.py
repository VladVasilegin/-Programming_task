class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        mas = sorted(intervals, key=lambda x: x[0])
        resultMas = []
        start = None
        end = None

        for i in mas:
            if start == None:
                start = i[0]
                end = i[1]
                continue
            if i[0] <= end:
                end = max(end, i[1])
            else:
                resultMas.append([start, end])
                start = i[0]
                end = i[1]
        resultMas.append([start, end])
        return resultMas