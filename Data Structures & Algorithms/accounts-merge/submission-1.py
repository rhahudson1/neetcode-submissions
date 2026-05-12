class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        emailIdx = {} # email -> index (number for node)
        emails = [] # stores set of emails
        emailToAcc = {} # store emailIdx -> account_ID (john_newyork@mail.com came from account 0)
        m = 0
        for accId, a in enumberate(accounts):
            for i in range(1,len(a)):
                email = [i]
                if email in emails:
                    continue
                emailIdx[email] = m
                emails.append(email)
                emailToAcc[m] = accId
                m += 1

        adj = [[] for _ in range(m)]
        for a in accounts:
            for i in range(2,len(a)):
                node1 = emailIdx[a[i]]
                node2 = emailIdx[a[i-1]]
                adj[node1].append(node2)
                adj[node2].append(node1)
        emailGroup = defaultdict(list)
        visited = [False] * m
        def dfs(node, accId):
            visited[node] = True
            emailGroup[accId].append(emails[node])
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei, accId)
        for i in range(m):
            if not visited[i]:
                dfs(i, emailToAcc[i])
        for accId in emailGroup:
            name = accounts[accId][0]
            res.append([name] + sorted(emailGRoup[accId]))
        return res
