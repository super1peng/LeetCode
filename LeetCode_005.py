#coding:utf-8


'''
题目：
    给定一个字符串s，找到s中最长的回文子串。你可以假设s的最大长度是1000

例子：
    示例一：
    输入 “babad”
    输出 “bab” 或者 “aba”

    示例二：
    输入 "cbbd"
    输出 “bb”
'''

class longestPalindrome(object):
    
    def __init__(self):
        self.res = ""
    
    def function(self, s):
        if len(s) < 2:
            return s
    
        for i in range(len(s)):
            self.solve(s, i, i)
            self.solve(s, i, i+1)
        return self.res

    def solve(self, s , left, right):
        # 如果 left 仍然在范围内， right 仍然在范围内， 同时左右等于右边，则将原来的回文进行拓展
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        if right -left -1 > len(self.res):
            self.res = s[left+1:right]
        


if __name__ == '__main__':
    s = 'babad'
    ceshi = longestPalindrome()
    print(ceshi.function(s))
    