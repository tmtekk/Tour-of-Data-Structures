#Tim Miller
#Basic singly-linked list in python

class List(object):
    def __init__(self, head=None):
        self.head = head

    ##append method adds a new node to end of the list
    def append(self, link):
        if self.head == None:
            #create new head node if it doesn't exist
            self.head = Node(link)
            return
        #set the current node equal to the head node
        current.nextNode = self.head
        #point to the new node
        self.head = newNode
        #set current node to the next node,
        #until the next is not null
        while current.nextNode != None:
            current = current.nextNode
        current.next = Node(link)

    ##prepend method adds node to the front of the list
    def prepend(self, link):
        #create node which will become the new head
        newHead = Node(link)
        #point new head node to the head of list
        newHead.nextNode = self.head
        self.head = newHead

    ##delete method to remove a link in the list
    def delete(self, link):
        #return if there is nothing to delete
        if self.head == None:
            return
        #check if the head needs deleted
        if self.head.link == link:
            #point to next link to remove the previous head
            self.head = self.head.nextNode
            return
        #create current pointer and traverse through the list
        current = self.head
        while current.nextNode != None:
            #check if the current link is the same as the
            #next link and delete next link
            if current.nextNode.link == link:
                #pointer to next is moved to the next next link,
                #to remove the next link
                current.nextNode = current.nextNode.nextNode
                return
            #move on to next element
            current = current.nextNode

    ##method to get an element from the list
    def getElement(self, index):
        newNode = self.head
        for i in range(index):
            newNode = newNode.getNext()
        return node.getData()

    ##method to set element in list
    def setElement(self, index):
        newNode = self.head
        for i in range(index):
            newNode = newNode.getNext()
        return newNode.setData()

#node class used for the items in the list
class Node(object):
    def __init__(self, data, nextNode=None):
        self.data = data
        self.next = nextNode

    def getData(self, data):
        return self.data
    def getNext(self,  nextNode):
        return self.nextNode

    def setData(self, data):
        self.data = data
    def setNext(self, nextNode):
        self.nextNode = nextNode
