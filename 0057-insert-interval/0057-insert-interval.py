class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        arr = []
        inserted = False

        # Step 1: Insert newInterval in correct position
        for interval in intervals:
            if not inserted and interval[0] > newInterval[0]:
                arr.append(newInterval)
                inserted = True

            arr.append(interval)

        if not inserted:
            arr.append(newInterval)

        # Step 2: Apply your merge logic
        res = []
        arr.sort()

        start1 = arr[0][0]
        end1 = arr[0][1]

        for i in range(1, len(arr)):
            start2 = arr[i][0]
            end2 = arr[i][1]

            if end1 >= start2:
                end1 = max(end1, end2)
                continue

            res.append([start1, end1])
            start1 = start2
            end1 = end2

        res.append([start1, end1])
        return res

        
           
        