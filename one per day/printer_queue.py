import random

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

# The Printer class will need to track whether it has a current task. If it does, then it is busy
# and the amount of time needed can be computed from the number of pages in the task. The
# constructor will also allow the pages-per-minute setting to be initialized. The tick method
# decrements the internal timer and sets the printer to idle if the task is completed.
class Printer():
    #initialising and using pages per minute
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0
    #decrements the internal timer and sets the printer to idle if task is completed
    def tick(self):
        if self.current_task != None:
            self.time_remaining -= 1
            if self.time_remaining < 0:
                self.current_task = None
    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate

# The Task class will represent a single printing task. When the task is created, a random number
# generator will provide a length from 1 to 20 pages. We have chosen to use the randrange
# function from the random module.
# Each task will also need to keep a timestamp to be used for computing waiting time. This
# timestamp will represent the time that the task was created and placed in the printer queue. The
# wait_time method can then be used to retrieve the amount of time spent in the queue before
# printing begins.

class Task():
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)
    def get_stamp(self):
        return self.timestamp
    def get_pages(self):
        return self.pages
    def wait_time(self, current_time):
        return current_time - self.timestamp

# The main simulation implements the algorithm described above. The print_queue object is
# an instance of our existing queue ADT. A boolean helper function, new_print_task, decides
# whether a new printing task has been created. We have again chosen to use the randrange
# function from the random module to return a random integer between 1 and 180. Print tasks
# arrive once every 180 seconds. By arbitrarily choosing 180 from the range of random integers,
# we can simulate this random event. The simulation function allows us to set the total time and
# the pages per minute for the printer.
def simulation(num_of_seconds, pages_per_minute):
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_of_seconds):
        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)
        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()
    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average wait is %6.2f secs, and %3d tasks remaining." %(average_wait, print_queue.size()))

def new_print_task():
    num = random.randrange(1, 181)
    if num == True:
        return True
    else:
        return False


def main():
    for i in range(10):
        simulation(3600, 10)



if __name__ == "__main__":
    main()