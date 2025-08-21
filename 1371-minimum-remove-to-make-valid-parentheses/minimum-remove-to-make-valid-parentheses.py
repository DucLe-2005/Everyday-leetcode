class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        indexes_to_remove = set()
        for i in range(len(s)):
            if s[i] not in "()":
                continue
            elif s[i] == "(":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    indexes_to_remove.add(i)
        indexes_to_remove = indexes_to_remove.union(set(stack))

        res = []
        for i in range(len(s)):
            if i in indexes_to_remove:
                continue

            res.append(s[i])

        return "".join(res)


