class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        digits = list(s)
        def dfs(i, k, path):
            print(path)
            if k == 4:
                if i == len(digits):
                    print("correct ip:", ".".join(path))
                    return res.append(".".join(path))
                else:
                    return
            
            val = 0
            for j in range(i, i + 3):
                if j == len(digits):
                    break
                
                if digits[j] == '0' and j == i:
                    path.append('0')
                    dfs(j+1, k+1, path)
                    path.pop()
                    break

                val = val * 10 + ord(digits[j]) - ord('0')
                if val > 255:
                    break
                
                path.append(str(val))
                dfs(j+1, k+1, path)
                path.pop()
            
        dfs(0, 0, [])
        return res
