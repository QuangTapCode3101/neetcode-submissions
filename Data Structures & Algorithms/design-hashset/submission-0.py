class ListNode:

    def __init__(self, key, next = None):
        self.key = key
        self.next = next
        
class MyHashSet:

    def __init__(self):
        self.size = 10**4
        self.buckets = [ListNode(0) for _ in range(self.size)]

    def hash(self, key : int) -> int :
        return key % self.size
    
    def add(self, key: int) -> None:
        index = self.hash(key)
        curr = self.buckets[index]

        while curr.next != None :
            if curr.next.key == key : 
                return
            curr = curr.next
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = self.hash(key) 
        curr = self.buckets[index]
        while curr.next != None : 
            if curr.next.key == key :
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        index = self.hash(key)
        curr = self.buckets[index]
        while curr.next != None :
            if curr.next.key == key :
                return True
            curr = curr.next
        return False 
