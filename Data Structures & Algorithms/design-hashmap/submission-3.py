class ListNode :
    def __init__(self, key,value, next = None) :
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:
    
    def __init__(self):
        self.size = 10**4
        self.buckets =  [ListNode(0,None) for _ in range(self.size)]

    def hash(self,key) -> int :
        return key % self.size
    
    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        curr = self.buckets[index]

        while curr.next != None : 
            if curr.next.key == key :
                curr.next.value = value
                return
            curr = curr.next
        curr.next = ListNode(key,value)

    def get(self, key: int) -> int:
        index = self.hash(key)  
        curr = self.buckets[index] 

        while curr.next != None : 
            if curr.next.key == key : 
                return curr.next.value
            curr = curr.next
        return -1
    
    def remove(self, key: int) -> None:
        index = self.hash(key)
        curr = self.buckets[index]

        while curr.next != None : 
            if curr.next.key == key :
                curr.next = curr.next.next
                return
            curr = curr.next