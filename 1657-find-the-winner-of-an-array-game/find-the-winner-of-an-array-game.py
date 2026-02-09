class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # 1. create a queue with the numbers in arr
        # 2. pop a number
        # 3. pop the next numbers and increase win count, put the popped numbers back to th queue
        # 4. if lose, reset win count and get the next number to compare

        q = deque(arr)
        i = 0
        while True:
            count = 0 if i == 0 else 1
            num = q.popleft()

            while count < k and count < (len(arr) - 1) and q:
                if q[0] > num:
                    break
                q.append(q.popleft())
                count += 1
            q.append(num)
            
            if count == k or count == len(arr) - 1:
                return num
            i += 1
            