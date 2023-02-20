from hashlib import md5
from sys import stderr


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = {}.fromkeys(range(self.size), None)

    @staticmethod
    def __hashfunction(val_in):
        val_in = str(val_in)
        val_out = md5(bytes(val_in, "UTF-8")).hexdigest()
        return val_out

    def put(self, value):
        hash_key = self.__hashfunction(value)
        if hash_key in self.slots:
            temp = Node(value)
            p = self.slots[hash_key]
            while p.next is not None:
                p = p.next
            p.next = temp
        else:
            for i in self.slots:
                if self.slots[i] is None:
                    self.slots[hash_key] = self.slots[i]
                    del self.slots[i]
                    self.slots[hash_key] = Node()
                    self.slots[hash_key].data = value
                    break
            else:
                print('HashTable is full, cannot add more hashes!', file=stderr)

    def get(self, value):
        hash_key = self.__hashfunction(value)
        if hash_key in self.slots:
            if self.slots[hash_key].data == value:
                return True
            else:
                p = self.slots[hash_key]
                while p is not None and p.data != value:
                    p = p.next
                if p is not None and p.data == value:
                    return True
            return False
        else:
            return False

    def delete(self, value):
        hash_key = self.__hashfunction(value)
        if hash_key in self.slots:
            if self.slots[hash_key].data == value:
                self.slots[hash_key].data = None
            else:
                p = self.slots[hash_key]
                pre = None
                while p is not None and p.data != value:
                    pre = p
                    p = p.next
                if p is None:
                    print(f"Delete Error\nValue {value} not in HashTable")
                else:
                    pre.next = p.next
        else:
            print(f"Delete Error\nValue {value} not in HashTable")

    def print_hash_table(self):
        for k, v in self.slots.items():
            print(k)
            print(self.slots[k].data)
            p = self.slots[k]
            while p.next is not None:
                print(p.data)
                p = p.next


ht = HashTable(2)

ht.put(100)
ht.put(110)
ht.put(120)
ht.put(130)
ht.put(100)
ht.put(100)
ht.put(100)

print(ht.get(100))
print(ht.get(150))

ht.delete(110)
ht.delete(100)
ht.delete(100)

ht.print_hash_table()
