class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # time: O(V + E)
        # space: O(V + E)
        prereq = defaultdict(list)
        need_count = [0] * numCourses
        for a, b in prerequisites:
            prereq[b].append(a)
            need_count[a] += 1
        
        # take courses whose prerequisites are satisfied
        q = deque([])
        for c in range(numCourses):
            if need_count[c] == 0:
                q.append(c)

        order = []
        while q:
            prereq_course = q.popleft()
            order.append(prereq_course)
            for course in prereq[prereq_course]:
                need_count[course] -= 1

                if need_count[course] == 0:
                    q.append(course)

        return order if len(order) == numCourses else []