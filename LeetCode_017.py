#coding:utf-8


'''
    电话号码的字母组合
        给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
        给出数字到字符的映射。

    示例：
        输入："23"
        输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''
class Solution(object):
    def __init__(self):
        pass

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letter = {
            "2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],
            "5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],
            "8":["t","u","v"],"9":["w","x","y","z"]
        }
        
        res = []
        for alpha in digits:
            med = []
            for i in letter[alpha]:
                if len(res) == 0:
                    med.append(i)
                else:
                    for word in res:
                        word = word + i
                        med.append(word)
            res = med
        return res
                

if __name__ == '__main__':
    digits = "23"
    a = Solution()
    print(a.letterCombinations(digits))
    