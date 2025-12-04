class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.email_to_name = {}
        self.parents = {}
        self.sizes = {}

        # create parents and sizes array
        for account in accounts:
            name = account[0]

            for email in account[1:]:
                self.parents[email] = email
                self.sizes[email] = 1
                self.email_to_name[email] = name
        
        # merge accounts
        for account in accounts:
            for i in range(1, len(account) - 1):
                for j in range(i + 1, len(account)):
                    print("unioinin", account[i], account[j])
                    self.union(account[i], account[j])
                    
        
        groups = defaultdict(list)
        for email in self.email_to_name:
            root = self.find(email)
            groups[root].append(email)
        
        res = []
        for root, emails in groups.items():
            emails.sort()
            res.append([self.email_to_name[root]] + emails)
        
        return res

    def find(self, A):
        root = A
        while root != self.parents[root]:
            root = self.parents[root]
        
        old_root = self.parents[A]
        while A != root:
            old_root = self.parents[A]
            self.parents[A] = root
            A = old_root
        
        return root

    def union(self, A, B):
        root_A = self.find(A)
        root_B = self.find(B)  

        if self.sizes[root_A] < self.sizes[root_B]:
            self.email_to_name[root_A] = self.email_to_name[root_B]
            self.parents[root_A] = root_B
            self.sizes[root_B] += self.sizes[root_A]
            
        else:
            self.email_to_name[root_B] = self.email_to_name[root_A]
            self.parents[root_B] = root_A
            self.sizes[root_A] += self.sizes[root_A]

        return True
        


