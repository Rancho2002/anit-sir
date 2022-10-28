class dequeue:
    def __init__(self):
        self.array = []

    def is_empty(self):
        if len(self.array)==0:
            return True
        else:
            return False

    def insert_at_front(self,data):
        if self.is_empty():
            self.array.append(data)
        else:
            self.array.insert(0,data)
    
    def insert_at_rear(self,data):
        self.array.insert(0,data)

    def delete_from_front(self):
        if self.is_empty():
            print("There is nothing to delete")
        else:
            self.array.remove(self.array[0])

    def delete_from_rear(self):
        if self.is_empty():
            print("There is nothing to delete")
        else:
            self.array.pop()
    
    def reverse(self):
        l = len(self.array)
        self.array= self.array[::-1] #generator

    def print_queue(self):
        if self.is_empty():
            print("Nothing to print")
        else:
            for i in range(len(self.array)):
                if i==len(self.array)-1:
                    print(self.array[i])
                else:
                    print(self.array[i],end=" --> ")

d = dequeue()

d.insert_at_rear(567)
d.insert_at_rear(87)
d.insert_at_rear(34)
d.insert_at_rear(56)
d.insert_at_front(23)
d.delete_from_front()
d.delete_from_rear()
d.print_queue()
d.reverse()
d.print_queue()