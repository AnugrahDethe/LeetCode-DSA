class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # A valid parentheses string must have even length.
        if (m + n - 1) % 2 == 1:
            return False

        # dp[j] contains all possible balances at column j
        dp = [set() for _ in range(n)]

        # Start at (0, 0)
        if grid[0][0] == '(':
            dp[0].add(1)
        else:
            return False

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    continue

                current = grid[i][j]

                # Possible balances from top and left
                possible = set()

                if i > 0:
                    possible.update(dp[j])

                if j > 0:
                    possible.update(dp[j - 1])

                # Calculate new balances
                new_balances = set()

                for balance in possible:
                    if current == '(':
                        new_balance = balance + 1
                    else:
                        new_balance = balance - 1

                    # A valid parentheses string can never
                    # have negative balance.
                    if new_balance >= 0:
                        new_balances.add(new_balance)

                dp[j] = new_balances

        # A valid parentheses string must finish with balance 0
        return 0 in dp[n - 1]