# Definition for singly-linked list.
# class ListNode(object):
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

        l1num = 0
        l2num = 0
        sumVal = 0
        returnVal = ListNode()
        l1cycle = True
        l2cycle = True

        i = 0
        while l1cycle == True or l2cycle == True:
            if l1cycle:
                l1num += l1.val * pow(10,i)
                if l1.next: l1 = l1.next
                else: l1cycle = False
            if l2cycle:
                l2num += l2.val * pow(10,i)
                if l2.next: l2 = l2.next
                else: l2cycle = False
            i+= 1

        sumVal = l1num + l2num
        j = len(str(sumVal)) - 1
        abc = ListNode(j)

        previous = None
        while j >= 0:
            x = sumVal//pow(10,j)
            sumVal-= x*pow(10,j)
            returnVal = ListNode(x)
            if previous:
                returnVal.next = previous
            previous = returnVal
            j-=1

        return returnVal