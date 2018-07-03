#coding:utf-8

'''
    给定一个字符串(s)和一个字符模式(p)，实现支持 '.'和'*'的正则表达式匹配
    '.' 匹配任意单个字符
    '*' 匹配零个或多个前面的元素
    匹配应该覆盖整个字符串(s)，而不是部分字符串。

    说明：
        s 可能为空，且只包含从 a-z 的小写字母。
        p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
'''

class Solution(object):
    def __init__(self):
        pass
    
    @staticmethod
    def function(s, p):
        # dp[i][j] = true 表示长度为i的s 和 j的p匹配
        dp = [[False] * (len(p)+1) for _ in range(len(s) + 1)]
        
        # 情况1
        dp[0][0] = True 

        # 情况5 
        dp[0][1] = False
        
        # 情况2 当 j =0 i >=1 时，默认为false
        
        # 情况3 当 i=0 j>=2
        for j in range(2, len(p) + 1):
            dp[0][j] = dp[0][j-2] and p[j-1] == "*"      
        
        # 情况4 当 i>=1 j >=1
        for i in range(1, len(s)+1):
            for j in range(1,len(p)+1):
                
                if p[j-1] != '*':
                    dp[i][j] = dp[i-1][j-1] and (p[j-1] == '.' or p[j-1] == s[i-1])
                else:
                    dp[i][j] = dp[i][j-2] or (dp[i-1][j] and (p[j-2] == '.' or p[j-2] == s[i-1]))
        return dp[-1][-1]




if __name__ == '__main__':
    
    s = 'ab'
    p = '.*'
    print(Solution.function(s,p))
    