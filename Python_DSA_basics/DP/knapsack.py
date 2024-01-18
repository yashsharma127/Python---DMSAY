## pure recursion solution
def max_profit_recursive(weights, profits, capacity, idx=0):
    if idx == len(weights):
        return 0
    elif weights[idx] > capacity:
        return max_profit_recursive(weights, profits, capacity, idx+1)
    else:
        option1 = max_profit_recursive(weights, profits, capacity, idx+1)
        option2 = profits[idx] + max_profit_recursive(weights, profits, capacity-weights[idx], idx+1)
        return max(option1, option2)
    
## memoization solution
def max_profit_memo(capacity, weights, profit):
    memo = {}
    def recursive(idx , remaining):
        key = (remaining, idx)
        if key in memo :
            return memo[key] 
        elif idx == len(weights):
            memo[key] = 0
        elif weights[idx] > remaining:
            memo[key] = recursive(remaining, idx+1)
        else :
            memo[key] = max(recursive(remaining, idx), profit[idx] + recursive(remaining-weights[idx], idx+1))
        return memo[key]
    return recursive(0, capacity)


## dynamic programming solution
def max_profit_dp(weights, profit, capacity):
    n = len(weights)
    table = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(n):
        for c in range(1, capacity + 1):
            if weights[i] > c:
                table[i + 1][c] = table[i][c]
            else:
                table[i + 1][c] = max(table[i][c], profit[i] + table[i][c - weights[i]])
    
    return table[-1][-1]
