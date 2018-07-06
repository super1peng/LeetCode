#coding:utf-8

'''
    字符串相乘
    给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式

    示例：
        输入: num1 = "2", num2 = "3"
        输出: "6"

        输入: num1 = "123", num2 = "456"
        输出: "56088"
'''

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        num1 = list(num1)
        num2 = list(num2)

        num1.reverse()
        num2.reverse()

        add_list = []
        res = ""

        i_c = 0
        for i in num1:
            j_c = 0
            for j in num2:
                ge_multi = int(i) * int(j)

                ge_multi = str(ge_multi)
                k = 0
                while k < j_c:
                    ge_multi = ge_multi + "0"
                    k = k + 1
                k = 0
                while k < i_c:
                    ge_multi = ge_multi + "0"
                    k = k + 1
                add_list.append(ge_multi)
                j_c = j_c + 1
            i_c = i_c + 1
        print(add_list)
        for _ in range(len(add_list)):
            if _ == 0:
                res = self.add_1('0',add_list[_])
            else:
                res = self.add_1(res,add_list[_])
        return res

    
    def add_1(self, num1, num2):
        """
            首先写一个字符串加法
        """
        len_1 = len(num1)
        len_2 = len(num2)
        num1 = list(num1)
        num1.reverse()
        num2 = list(num2)
        num2.reverse()
        res = ""
        if len_1<len_2:
            len_max = len_2
            for _ in range(len_2-len_1):
                num1.append('0')
        else:
            len_max = len_1
            for _ in range(len_1-len_2):
                num2.append('0')
        clg = 0 # 进位标志符
        for i in range(len_max):
            xixi = int(num1[i]) + int(num2[i]) + clg
            if xixi >= 10:
                xixi = xixi % 10
                clg = 1
            else:
                clg = 0
            res = str(xixi) + res
        if clg == 1:
            res = "1" + res
        return res

    def better(self, num1, num2):
        if len(num1) > len(num2):
            return self.multiply(num2,num1)
        num1 = num1[::-1]
        num2 = num2[::-1]
        ans = [0] * (len(num1) + len(num2))

        for i in range(len(num1)):
            for j in range(len(num2)):
                ans[i + j] += int(num1[i]) * int(num2[j])
        c = 0
        for i in range(len(ans)):
            ans[i] += c
            ans[i],c = ans[i] % 10, ans[i] / 10
        while c > 0:
            ans.append(c % 10)
            c = c / 10
        index = len(ans) - 1
        while index > 0 and ans[index] == 0:
            index -= 1
        return ''.join([str(x) for x in ans[0:index + 1]][::-1])

if __name__ == '__main__':
    
    num1 = "123"
    num2 = "456"
    a = Solution()
    print(a.multiply(num1,num2))
    