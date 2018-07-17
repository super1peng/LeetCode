#coding:utf-8

'''
    最后一个单词长度

    给定一个仅包含大小写字母和恐吓 ' '的字符串，
    返回其最后一个单词的长度，如果不存在最后一个单词，请返回0

    示例：
        输入: "Hello World"
        输出: 5

'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)
        res = 0
        Figure = True
        if s_len == 1:
            if s[0] != ' ':
                return 1
            else:
                return 0
        else:
            for i in range(len(s)-1,-1,-1):
                if s[i] != ' ':
                    res += 1
                    Figure = False
                elif s[i] == ' ' and Figure:
                    continue
                else:
                    return res
            return res

if __name__ == '__main__':
    s = 'hello world'
    a = Solution()
    print(a.lengthOfLastWord(s))
    