''' Creat a class node for data node '''


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


'''creat a link list class for link list '''


class linkedlist:
    def __init__(self):
        self.head = None
    # insert data in begin point

    def insert_at_bigin(self, data):
        node = Node(data, self.head)
        self.head = node

    ''' print link list '''

    def print(self):
        itr = self.head

        link_list = ''
        while itr:
             
            print(itr.data,end="--> ")
             
            itr = itr.next

         
    '''find linklist length'''
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
        
    '''data insert End position'''

    def insert_at_End(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)

    '''insert any index position link list node'''


    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("Out of range index")

        if index==0:
            self.insert_at_bigin(data)
            return

        itr=self.head
        count=0
        while itr:
            if count ==index -1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count +=1
    ''' remove data in index position link list'''


    def remove_at(self,index):
        if index < 0 or index > self.get_length():
            raise Exception("Out of range in link list")

        if index ==0:
            self.head=self.head.next
            return

        itr=self.head
        count=0
        while itr:
            if count==index -1:
                itr.next=itr.next.next
                break

            itr=itr.next
            count +=1

    ''' insert data list'''


    def insert_list(self,data_list):
        # self.head=None
        for data in data_list:
            self.insert_at_End(data)

if __name__ == "__main__":
    root = linkedlist()
    root.insert_at_bigin(3)
    root.insert_at_bigin(5)
    root.insert_at_bigin(8)
    root.insert_at_bigin(10)
    root.insert_at(2, 20)
    root.insert_at_End(4)
    root.insert_at_End(5)
    root.insert_at_End(10)
    root.insert_at_End(15)
    l=["praveen","ayush gupta","sandeep shrivasta"]
    root.insert_list(l)
    root.remove_at(10)
    root.print()
    print(" \n the length of linklist is :", root.get_length())
