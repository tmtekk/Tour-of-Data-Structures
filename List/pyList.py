#Tim Miller
#Basic singly-linked list in python

class List(object):
    def __init__(self):
        self.head = None

    ##append method adds a new node to end of the list
    def append(self, link):
        newNode = Node(link)
        if self.head == None:
            #create new head node if it doesn't exist
            self.head = Node(link)
            return
        #set the current node equal to the head node
        current = self.head
        #set current node to the next node,
        #until the next is not null
        while current.getNext():
            current = current.getNext()
        current.setNext(newNode)

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
        return newNode.getData()

    ##method to set element in list
    def setElement(self, index):
        newNode = self.head
        for i in range(index):
            newNode = newNode.getNext()
        return newNode.setData()

    ##boolean method to check if the list is empty
    def isEmpty(self):
        if self.head == None:
            return True
        return False

    ##method to return the head data value
    def getHead(self, link):
        link = self.head
        return link

#node class used for the items in the list
class Node(object):
    def __init__(self, data, nextNode = None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data
    def getNext(self):
        return self.nextNode

    def setData(self):
        self.data = data
    def setNext(self, nextNode):
        self.nextNode = nextNode

def main():
    #test that the new list is empty
    newHead = List()
    if newHead.isEmpty():
        print("No elements in the list yet")
    else:
        print("The lsit is not empty")

    #add an item and print it out
    newHead2 = List()
    newHead2.append("Bob")
    res = newHead2.getElement(0)
    print(res)

    #add multiple items and print them out
    newHead3 = List()
    newHead3.append("Bob")
    newHead3.append("Tim")
    newHead3.append("Sam")
    res0 = newHead3.getElement(0)
    res1 = newHead3.getElement(1)
    res2 = newHead3.getElement(2)
    print(res0)
    print(res1)
    print(res2)


if __name__ == "__main__":
        main()
