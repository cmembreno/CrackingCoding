class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def add(self, data, head = None):
        temp = head
        newNode = Node(data)
        if(head == None):
            return newNode
        else:
            while(temp.next!=None):
                temp = temp.next
        temp.next = newNode
        return head

    def printList(self, head):
        temp = head
        if(head==None):
            print("empty")
        else:
            while(temp!=None):
                print(temp.data)
                temp = temp.next

    def deleteDuplicate(self,head):
        temp = head
        table = set()
        if(head == None):
            return None
        else:
            table.add(temp.data)
            while(temp.next!=None):
                if(temp.next.data in table):
                    temp.next = temp.next.next
                else:
                    table.add(temp.next)
                    temp = temp.next

        return head

    def deleteDuplicate2(self,head):
        current = head
        if(head == None):
            return None
        else:
            while(current.next!=None):
                front = current
                while(front.next!=None):
                    if(current.data == front.next.data):
                        front.next = front.next.next
                    else:
                        front = front.next
                if(current.next!=None):
                    current = current.next

        return head


    def kthToLast(self, head, index):
        size = self.findSize(head)
        temp = head
        i=0
        while(temp!=None):
            currentIndex = size -i
            if(currentIndex==index):
                return temp.data
            else:
                i+=1
                temp = temp.next

        return None

    def findSize(self,head):
        temp = head
        i = 0
        while(temp!=None):
            i+=1
            temp = temp.next

        return i

    def deleteMiddle(self, node, head):
        temp = node
        while(temp.next!=None):
            temp.data = temp.next.data
            if(temp.next.next == None):
                temp.next =None
            else:
                temp = temp.next

        return head

def main():
    list = LinkedList()
    l1 = list.add(1)
    l1 = list.add(2,l1)
    l1 = list.add(3,l1)
    l1 = list.add(4,l1)
    list.printList(l1)
    print("break")
    node = l1.next
    l1 = list.deleteMiddle(node,l1)
    list.printList(l1)


if __name__ == "__main__":
    main()