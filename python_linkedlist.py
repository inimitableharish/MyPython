import copy 

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_node_to_left(self, new_data):
        print('adding node with data:', new_data)
        new_node = Node(new_data)
        new_node.next = self.head 
        self.head = new_node

    def display_node(self):
        root_node = copy.deepcopy(self.head) 
        while(root_node!=None):
            print(str(root_node.data), end='->')
            root_node = root_node.next

    def count_nodes(self):
        count = 0 
        root_node = copy.deepcopy(self.head)
        while(root_node!=None):
            count += 1
            root_node = root_node.next 
        print('Total no of nodes in the linked list:',str(count))
    
    def insert_key(self, index, data):
        i = 0 
        prev = self.head
        root_node = self.head
        while(i<=index):
            prev = root_node
            curr = prev.next  
            i += 1 
        new_node = Node(data)
        prev.next = new_node 
        new_node.next = curr 

    def reverse_link_list(self):
        '''O(n) space'''
        current_node = self.head
        prev_node = None 
        while(current_node is not None):
            next = current_node.next 
            current_node.next = prev_node
            prev_node = current_node 
            current_node = next 
        self.head = prev_node 


if __name__ == '__main__':
    ll_obj = LinkedList()
    ll_obj.insert_node_to_left(10)
    ll_obj.insert_node_to_left(20)
    ll_obj.insert_node_to_left(30)
    ll_obj.insert_node_to_left(40)
    print('link list')
    ll_obj.display_node()
    ll_obj.count_nodes()
    print('insert 100 & 300')
    ll_obj.insert_key(2, 100)
    ll_obj.insert_key(3, 300)
    ll_obj.display_node()
    ll_obj.reverse_link_list()
    print('reverse')
    ll_obj.display_node() 

