#Tim Miller
#simple python class for a node data structure
class Node(object):
    """docstring for Node."""
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
