class Solution(object):
    def longestCommonSubsequence(self, text1, text2, indx1=0, indx2=0):
        if indx1 == len(text1) or indx2 == len(text2):
            return 0
        elif text1[indx1] == text2[indx2]:
            return 1 + self.longestCommonSubsequence(text1, text2, indx1+1, indx2+1)
        else:
            option1 = self.longestCommonSubsequence(text1, text2, indx1+1, indx2)
            option2 = self.longestCommonSubsequence(text1, text2, indx1, indx2+1)
            return max(option1, option2)


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        memo ={}
        def recurse(idx1=0, idx2=0):
            key = (idx1, idx2)
            if key in memo:
                return memo[key]
            elif idx1 == len(text1) or idx2 == len(text2):
                memo[key] = 0
            elif text1[idx1] == text2[idx2]:
                memo[key] = 1 + recurse(idx1+1, idx2+1)
            else:
                memo[key] = max(recurse(idx1+1, idx2), recurse(idx1, idx2+1))
            return memo[key]
        return recurse(0,0)
    
def lcs_dp(seq1, seq2):
    n1, n2 = len(seq1), len(seq2)
    table = [[0 for x in range(n2+1)] for x in range(n1+1)]
    for i in range(n1):
        for j in range(n2):
            if seq1[i] == seq2[j]:
                table[i+1][j+1] = 1 + table[i][j]
            else:
                table[i+1][j+1] = max(table[i][j+1], table[i+1][j])
    return table[-1][-1]


def longestCommonSubsequence(self, text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]