class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        res = 0
        for i in range(n - 2):
            l, r = i + 1, n - 1

            while l < r:
                total = arr[i] + arr[l] + arr[r]

                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    if arr[l] == arr[r]:
                        c = r - l + 1
                        res += (c * (c - 1) // 2)
                        break
                    
                    l_count = 1
                    l += 1
                    while l <= n and arr[l] == arr[l-1]:
                        l_count += 1
                        l += 1
                    
                    r_count = 1
                    r -= 1
                    while l <= r and arr[r] == arr[r+1]:
                        r_count += 1
                        r -= 1
                    
                    res += l_count * r_count
        return res % (10**9 + 7)
