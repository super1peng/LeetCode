#coding:utf-8


'''
    报数序列是指一个整数序列，按照其中的整数的迅速进行报数，得到下一个数。
    前5个情况：
        1.     1
        2.     11
        3.     21
        4.     1211
        5.     111221
    示例：
        输入: 1
        输出: "1"

        输入: 4
        输出: "1211"
'''

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        k = 0
        res = ""
        if n == 1:
            res = "1"
            return res
        else:   # res 的长度 大于1时
            res = "1"
            while k < n-1 :
                med = ""
                count = 1
                origin = ""
                res = res + " "  # 便于最后一次判断
                for i in range(len(res)):
                    
                    if i == 0:
                        origin = res[i]

                    elif res[i] == origin:
                        count += 1
                        if i+1 == len(res):
                            med = med + str(count)
                            med = med + res[i]
                    else:
                        med = med + str(count)
                        med = med + res[i-1]
                        origin = res[i]
                        count = 1
                res = med
                k = k + 1

            return res

    def better_countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        origin = str(1)

        for _ in range(n - 1):
            result = ""
            tmp = origin[0]
            count = 0
            for j in range(len(origin)):
                if origin[j] == tmp:
                    count += 1
                else:
                    result += str(count)
                    result += str(tmp)
                    count = 1
                    tmp = origin[j]

                if j == len(origin) - 1:
                    result += str(count)
                    result += str(tmp)

            origin = result

        return origin

if __name__ == '__main__':
    
    a = Solution()
    print("result",a.better_countAndSay(10))
    