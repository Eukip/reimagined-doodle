'''
    You are given two non-empty linked lists representing two non-negative integers. 
    The digits are stored in reverse order, and each of their nodes contains a single digit. 
    Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Example 1:

        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        Explanation: 342 + 465 = 807.
    
    Example 2:

        Input: l1 = [0], l2 = [0]
        Output: [0]
        
    Example 3:

        Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
        Output: [8,9,9,9,0,0,0,1]
 

    Constraints:

        The number of nodes in each linked list is in the range [1, 100].
        0 <= Node.val <= 9
        It is guaranteed that the list represents a number that does not have leading zeros.
'''

# Definition for singly-linked list.
#
# class ListNode(object):
#
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        a = ''.join(str(i) for i in reversed(l1))
        b = ''.join(str(i) for i in reversed(l2))
        d = str(int(a) + int(b))[::-1]
        return [int(i) for i in d]


    def addTwoNumbersSpisano(self, l1, l2):  # 57 ms
        carry = 0
        res = n = ListNode(0)
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10)
            n.next = n = ListNode(val)
        return res.next
    
    
    def addTwoNumbersFastest(self, l1, l2): # 30 ms
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        carry = 0
        #result = []
        result = None
        head = None
        while (True):
            sum = 0
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next

            sum += carry
            #result.append(sum % 10)

            newnode = ListNode(sum % 10)

            if result == None:
                result = newnode
                head = newnode
            else:
                result.next = newnode
                result = newnode
            
            carry = sum / 10

            if carry == 0 and l1 == None and l2 == None:
                break

        #return result
        return head