# Create a priority queue with enqueue and deque
class PriorityQueue:
    def __init__(self):
        self.high = []
        self.mid = []
        self.low = []

    def enqueue(self,data,priority):
        priority = priority.lower()
        if priority == "high":
            self.high.append(data)
        elif priority == "mid":
            self.mid.append(data)
        elif priority == "low":
            self.low.append(data)
        else:
            raise ValueError("Enter high, mid or low")
    def dequeue(self):
        if self.high:
            return self.high.pop(0)
        elif self.mid:
            return self.mid.pop(0)
        elif self.low:
            return self.low.pop(0)
        else:
            raise IndexError("Empty Queue")

# Example usage
pq = PriorityQueue()

# Enqueue elements
pq.enqueue("Task1", "high")
pq.enqueue("Task2", "mid")
pq.enqueue("Task3", "low")
pq.enqueue("Task4", "high")

# Dequeue elements
print(pq.dequeue()) 
print(pq.dequeue())  
print(pq.dequeue()) 
print(pq.dequeue())  



