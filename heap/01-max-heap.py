class MaxHeap:
    
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
            largest = i 
            
            if left_child < l and self.heap[left_child] > self.heap[largest]:
                largest = left_child
            
            if right_child < l and self.heap[right_child] > self.heap[largest]:
                largest = right_child
            
            if i == largest:
                break
            
            if i != largest:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest
                
        return
    
    def insert(self, val: int):
        self.heap.append(val)
        i = len(self.heap) - 1
        
        while i > 0:
            parent = i // 2
            
            if self.heap[parent] < self.heap[i]:
                self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
                i = parent
            else:
                break
            
    
    def get_max(self) -> int:
        if len(self.heap) > 0:
            return self.heap[0]

        return -1
    
    def delete(self):
        l = len(self.heap)
        
        if l == 0:
            return
        
        self.heap[0] = self.heap[l-1]
        self.heap = self.heap[:l-1]
        self.heapify()
        
        return
        
    def extract_max(self) -> int:
        if len(self.heap) == 0:
            return
        
        rslt = self.heap[0]
        self.delete()
        
        return rslt

max_heap = MaxHeap()
max_heap.insert(2)
max_heap.insert(7)
max_heap.insert(3)
max_heap.insert(5)
max_heap.insert(9)
max_heap.insert(1)

max_heap.print()

print(max_heap.get_max())

for i in range(6):
    print(max_heap.extract_max())