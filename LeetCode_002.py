#coding:utf-8


'''
Add Two Number

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain ang leading zero, except the number0 itself

给出两个链表，存储非负数，两个链表都是按倒序方式存储数字（个位、十位、百位）要求将两个链表相加并以链表形式返回

例子：
 Input (2 -> 4 -> 3) + (5 -> 6 -> 4)
 Output 7 -> 0 ->8
 Explanation 342 + 465 = 807

'''


# 需要考虑不同位数相加的情况
# 同时数组的长度不能用len来获取

class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None
        

def addTwoNumbers(l1, l2):
    '''
    type l1 : ListNode
    type l2 : ListNode
    retun : ListNode
    '''

    # 指定到链表头结点
    p = dummy = ListNode(-1)
    carry = 0

    while l1 and l2:
        p.next = ListNode(l1.val + l2.val + carry)

        carry = p.next.val / 10
        p.next.val  = p.next.val % 10
        
        p = p.next
        l1 = l1.next
        l2 = l2.next
    
    res = l1 or l2  # 取得高位

    while res:
        p.next = ListNode(res.val + carry)
        carry = p.next.val / 10
        p.next.val = p.next.val % 10
        p = p.next
        res = res.next
    
    if carry:
        p.next = ListNode(1)
    return dummy.next