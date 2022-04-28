class Queue():
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
def hot_potato(name_list, number):
    my_queue = Queue()
    #enqueue all name in name_list
    for name in name_list:
        my_queue.enqueue(name)
    #while size of queue > 1, keep moving items from front to back of queue till num is reached, then dequeue front item
    while my_queue.size() > 1:
        for i in range(number):
            my_queue.enqueue(my_queue.dequeue())
        my_queue.dequeue()
    return my_queue.dequeue()
def main():
        # q = Queue()
        # print(q.is_empty())
        # q.enqueue('Apple')
        # q.enqueue('Ball')
        # q.enqueue('Cat')
        # print(q.is_empty())
        # print(q.size())
        # q.dequeue()
        # print(q.size())
        name_list = ['apple', 'ball', 'cat', 'dog', 'eye', 'fish', 'goat', 'hen', 'ink']
        number = 7
        print(hot_potato(name_list, number))
    
if __name__ == "__main__":
    main()