class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # initialize current_time
        # add tasks with enqueueTime <= currtime_time to a heap
        # each element in the heap = (processingTime, index) -> always pick task with least processingTime,
        # then smallest index
        # current_time += processingTime
    
        tasks = [
            (enqueue_time, processing_time, idx)
            for idx, (enqueue_time, processing_time) in enumerate(tasks)
        ]
        tasks.sort()

        heap = []
        res = []
        curr_time = tasks[0][0]
        i = 0
        n = len(tasks)
        while i < n or heap:
            # cpu is idle, move to the next task
            if not heap and i < n and curr_time < tasks[i][0]:
                curr_time = tasks[i][0]
            
            # Add every task that has arrived
            while i < n and tasks[i][0] <= curr_time:
                enqueue_time, processing_time, original_idx = tasks[i]
                heapq.heappush(heap, (processing_time, original_idx))
                i += 1
            
            processing_time, original_idx = heapq.heappop(heap)
            res.append(original_idx)
            curr_time += processing_time
        return res