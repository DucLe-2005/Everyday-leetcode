class Solution:
    def distMoney(self, money: int, children: int) -> int:
        # Everyone needs at least $1
        if money < children:
            return -1

        if money > 8 * children:
            return children - 1

        # Give everyone $1 first
        m = money - children  # extra to distribute
        max8 = min(children, m // 7)
        r = m % 7

        if max8 == children and r == 0:
            return children

        # If remainder is 3 and there's exactly one non-8 kid left,
        # that last kid would be 1+3=4 (forbidden). Sacrifice one 8.
        if r == 3 and max8 == children - 1:
            return max8 - 1

        return max8
