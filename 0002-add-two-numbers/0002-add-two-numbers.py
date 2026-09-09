class Solution(object):
    def addTwoNumbers(self, l1, l2):

        p1 = l1
        p2 = l2
        c = 0

        while p1 != None:

            if p2 != None:
                v = p1.val + p2.val + c
                p2 = p2.next
            else:
                v = p1.val + c

            c = v // 10
            v = v % 10

            p1.val = v

            if p1.next == None:
                if p2 != None:
                    p1.next = ListNode(0)
                elif c != 0:
                    p1.next = ListNode(c)
                    c = 0

            p1 = p1.next

        return l1