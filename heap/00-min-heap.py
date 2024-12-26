class MinHeap:
    def __init__(self):
        self.heap = []
    
    def print(self):
        print(self.heap)
        return
        
    def heapify(self):
        l = len(self.heap)
        i = 0
        while i < l:
            left_child = i * 2
            right_child = i * 2 + 1
            
            if left_child < l and right_child < l and self.heap[left_child] < self.heap[right_child] and self.heap[i] > self.heap[left_child]:
                self.heap[i], self.heap[left_child] = self.heap[left_child], self.heap[i]
                i = left_child
            elif right_child < l and self.heap[i] > self.heap[right_child]:
                self.heap[i], self.heap[right_child] = self.heap[right_child], self.heap[i]
                i = right_child
            else:
                break
            
        return
    
    def insert(self, val: int):
        self.heap.append(val)
        l = len(self.heap) - 1
        parent = l//2
        
        while parent >= 0 and self.heap[parent] > self.heap[l]:
            self.heap[parent], self.heap[l] = self.heap[l], self.heap[parent]
            l = parent
            parent = l//2
        
        return
    
    def get_min(self):
        return self.heap[0]
    
    def extract_min(self):
        rslt = self.heap[0]
        self.delete()
        return rslt
        
    
    def delete(self):
        l = len(self.heap)-1
        self.heap[0] = self.heap[l]
        self.heap = self.heap[:l]
        
        if len(self.heap) == 0:
            return
    
        self.heapify()
        
        return
    
min_heap = MinHeap()
min_heap.insert(9)
min_heap.insert(2)
min_heap.insert(4)
min_heap.insert(7)
min_heap.print()
min_heap.insert(6)
min_heap.print()

print(min_heap.get_min())

for i in range(4):
    print(min_heap.extract_min())