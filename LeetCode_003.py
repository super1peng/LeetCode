#coding:utf-8


'''
Given a string, find the length of the longest substring without repeating characters

给出一个字符串，找到最长的没有重复字符的子字符串，并返回该子字符串的长度。

例子：
    Given "abcabcbb", the answer is "abc", which the length is 3.
    Given "bbbbb", the answer is "b", with the length of 1.
    Given "pwwkew", the answer is "wke", with the length of 3. 
    (Note that the answer must be a substring, "pwke" is a subsequence and not a substring.)

'''

class lengthofLongestSubstring(object):
    
    def __init__(self):
        pass
    
    @staticmethod
    def function_1(s):

        max_len = 0

        if len(s) == 1 or len(s) == 0:
            max_len = len(s)
        
        else:
            for i in range(0,len(s)-1):
                for j in range(i+1, len(s)):
                    if s[j] in s[i:j]:
                        if j-i > max_len:
                            right = j
                            left = i

                            max_len = right - left
                        break
                    elif j == len(s) -1:
                        if max_len < j -i + 1:
                            max_len = j - i + 1
        return max_len
    
    @staticmethod
    def function_2(s):
        
        index_dict = {}
        maxLength  = currMax = 0

        for i in range(len(s)):
            
            if s[i] in index_dict and i - index_dict[s[i]] -1 <= currMax:
                if maxLength < currMax:
                    maxLength = currMax
                currMax = i - index_dict[s[i]] - 1
            currMax = currMax + 1
            index_dict[s[i]] = i
        return maxLength if currMax < maxLength else currMax

if __name__ == '__main__':
    
    s = 'pwwkewgc'
    print(lengthofLongestSubstring.function_1(s))
    print(lengthofLongestSubstring.function_2(s))