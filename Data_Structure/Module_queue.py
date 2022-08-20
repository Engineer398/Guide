import queue

def show_fifo():
    fifo = queue.Queue()
    for i in range(5):
        fifo.put(i)

    while not fifo.empty():
        print(fifo.get(), end=" ")
    print()

# show_fifo()

def show_lifo():
    lifo = queue.LifoQueue()
    for i in range(5):
        lifo.put(i)

    while not lifo.empty():
        print(f"{lifo.get()}", end=" ")
    print()

show_lifo()