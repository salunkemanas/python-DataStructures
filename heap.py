class Heap:
    def __init__(self):
        self.heap = []

    def create(self, arr):
        for i in arr:
            self.insert(i)

    def createM(self, arr):
        for i in arr:
            self.insertM(i)

    def insert(self, item):
        index = len(self.heap)              #the index to insert the value
        parentIndex = (index-1)//2
        while index>0 and self.heap[parentIndex]<item: # if index==0 just append as no parents # loop will run till parent is smaller
            if len(self.heap)==index:
                self.heap.append(self.heap[parentIndex])
            else:
                self.heap[index] = self.heap[parentIndex]
            index = parentIndex
            parentIndex = (index-1)//2
        if index==len(self.heap):
            self.heap.append(item)
        else:
            self.heap[index]=item

    def insertM(self, item):
        index = len(self.heap)              #the index to insert the value
        parentIndex = (index-1)//2
        self.heap.append(item)
        while index>0 and self.heap[parentIndex]<item: # if index==0 just append as no parents # loop will run till parent is smaller
            self.heap[parentIndex], self.heap[index] = self.heap[index], self.heap[parentIndex]
            index = parentIndex
            parentIndex = (index-1)//2

    def printHeap(self):
        print(self.heap)
    

heap1 = Heap()
heap2 = Heap()
heap1.create([40,13,80,90,25,23,34,45,43,32])
heap2.createM([40,13,80,90,25,23,34,45,43,32])
heap1.printHeap()
heap2.printHeap()

