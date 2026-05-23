class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = Counter(students)
        students = deque(students)
        idx = 0

        print(count)
        while students:
            s = students.popleft()
            # print(f"s: {s}, students: {students}, sandwich: {sandwiches[idx]}, count: {count}")
            if idx == len(sandwiches):
                return len(students) + 1
            if sandwiches[idx] != s and count[sandwiches[idx]] == 0:
                return len(students) + 1
            if sandwiches[idx] == s:
                idx += 1
                count[s] -= 1
            else:
                students.append(s)
        
        return 0
                