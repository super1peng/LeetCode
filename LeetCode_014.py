#coding:utf-8



'''
    最长公共前缀：
        查找字符串数组中的最长公共前缀，如果不存在公共前缀，返回空字符串""

    示例：
        输入: ["flower","flow","flight"]
        输出: "fl"

        输入: ["dog","racecar","car"]
        输出: ""
        解释: 输入不存在公共前缀。
'''

class Solution(object):
    def __init__(self):
        pass
    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        length = len(strs)
        if length == 1:
            return strs[0]
        min_len = 999
        for i in range(length):
            if len(strs[i]) < min_len:
                min_len = len(strs[i])
        for j in range(min_len):
            for i in range(length):
                if i == 0:
                    continue
                elif strs[i-1][j] ==  strs[i][j]:
                    Flag = True
                    continue
                else:
                    Flag = False
                    break
            if Flag:
                res = res + strs[i-1][j]
            else:
                break
        return res

    def Best_longestCommonPrefix(self, strs):
        """
    :type strs: list[str]
    :rtype: str
    """

        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for item in strs[1:]:
            while item.find(prefix) != 0:
                prefix = prefix[:len(prefix) - 1]
                if prefix == "":
                    return ""
        return prefix
        

if __name__ == '__main__':
    b = ["a"]
    a = Solution()
    print(a.longestCommonPrefix(b))
    