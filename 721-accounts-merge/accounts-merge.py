class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [0] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b] 

        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # time: O(Ea(N) + Elog(E)) = O(Elog(E)), N = len(accounts), E = number of emails
        # space: O(N + E)
        u = UnionFind(len(accounts))

        email_to_owner = {}
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in email_to_owner:
                    u.union(i, email_to_owner[email])
                email_to_owner[email] = i

        owner_to_email = defaultdict(list)
        for email, owner in email_to_owner.items():
            owner_to_email[u.find(owner)].append(email)
        
        return [[accounts[owner][0]] + sorted(emails) for owner, emails in owner_to_email.items()] 
    