class Node:
    def __init__(self, Date, Open, High, Low, Close, Volume, AdjClose):
        self.Date = Date
        self.Open = Open
        self.High = High
        self.Low = Low
        self.Close = Close
        self.Volume = Volume
        self.AdjClose = AdjClose
        self.next = None

    


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, Date, Open, High, Low, Close, Volume, AdjClose):
     new_node = Node(Date, Open, High, Low, Close, Volume, AdjClose)

     if self.head is None:
         self.head = new_node
         return
     else:
         new_node.next = self.head
         self.head = new_node     