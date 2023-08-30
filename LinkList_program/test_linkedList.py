class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linked_list:
    def __init__(self):
        self.head=None

    '''insert a data starting possion creat a funtion'''
    def insert_last(self,data):

        if self.head==None:
            self.head=Node(data)
            return

        start = self.head
        while start.next:
            start=start.next
        start.next=Node(data)
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        start=self.head
        while start:
            print(start.data,end="--> ")
            start=start.next
        print("")

    '''find linklist length'''

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    '''print any node position number'''
    def node_number(self,number=None):
        if number<0 or number >= self.get_length():
            print(f"out of range {number} in linked list finding node")
            return
        count = 0
        itr=self.head
        while itr:
            if count == number:
                print(itr.data)
                return
            itr = itr.next
            count+=1







if __name__=="__main__":
    root=Linked_list()
    root.insert_last(12)
    root.insert_last(14)
    root.insert_last(15)
    root.insert_last(22)
    root.print()
    root.insert_last(12)
    root.insert_last(14)
    root.print()
    root.node_number(6)
