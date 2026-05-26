class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # time: O(E + ElogV) = O(ElogV)
        # space: O(n * E)
        # Build graph
        graph = defaultdict(list)
        for src, des, time in times:
            graph[src].append((des, time))

        dist = [float("inf")] * (n+1)
        dist[k] = 0
        heap = [(0, k)]

        while heap:
            curr_time, node = heapq.heappop(heap)

            if curr_time > dist[node]:
                continue

            for nei, time in graph[node]:
                new_time = curr_time + time

                if new_time < dist[nei]:
                    dist[nei] = new_time
                    heapq.heappush(heap, (new_time, nei))
        
        res = max(dist[1:])
        
        return res if res != float("inf") else -1
