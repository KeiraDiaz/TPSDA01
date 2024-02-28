class PriorityQueue:
    def __init__(self):
        self.heap = [0] *2
        self.heapsize = 1
        self.size = -1
    
    def parent(self,i):
        return (i-1)//2
    def right(self,i):
        return 2*(i+1)
    def left(self, i):
        return 2*(i+1)-1
    
    def resize(self):
        self.heap.extend([0] * self.heapsize)
        self.heapsize *= 2

    def swap(self,i, j):
        item = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = item

    def perlocateUp(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(self.parent(i), i)
            i = self.parent(i)

    def perlocateDown(self, i):
        minIndex = i
        min = self.heap[i]

        l = self.left(i)
        if l <= self.size and min > self.heap[l]:
            minIndex = l
            min = self.heap[l]
        
        r = self.right(i)
        if r <= self.size and min > self.heap[r]:
            minIndex = r
        
        if minIndex != i:
            self.swap(minIndex,i)
            self.perlocateDown(minIndex)
    
    def insert(self, item):
        if self.size == self.heapsize:
            self.resize()
        self.size += 1
        self.heap[self.size] = item

        self.perlocateUp(self.size)
    
    def __len__(self):
        return self.size + 1
    
    def copy(self):
        newpq = PriorityQueue()
        newpq.heap = self.heap.copy()
        newpq.size = self.size
        newpq.heapsize = self.heapsize
        return newpq
    
    def dequeue(self):
        item = self.heap[0]
        self.heap[0] = self.heap[self.size]
        self.size -= 1
        self.perlocateDown(0)
        return item
    
    def is_empty(self):
        return self.size == -1
    

'''
p1 = MovieGoer(1, "M", 100)
p2 = MovieGoer(2, "M", 100)
p3 = MovieGoer(3, "N", 100)
p4 = MovieGoer(4, "N", 100)

lst = [p1, p2, p3, p4]

MemberBooking = PriorityQueue()
NonMemberBooking = PriorityQueue()

for p in lst:
    if p.member == "M":
        MemberBooking.insert(PriorityQueueItem(p))
    else:
        NonMemberBooking.insert(PriorityQueueItem(p))  
'''

class PriorityQueueItem():
    def __init__(self, data):
         self.data = data


    def __lt__(self, other):
        # This function returns true if you want it to come first, the self before the other 
        # this function is to implement < of this type of object
        return self.data.money < other.data.money
        return self.data.id < other.data.id

    def __gt__(self, other):
        # This function returns true if you want the other to come first, the self after the other 
        # this function is to implement > of this type of object
        return self.data.money > other.data.money
