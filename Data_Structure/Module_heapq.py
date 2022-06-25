import heapq
import random


def heap_push():
    data = [random.randint(1, 20) for _ in range(10)]
    print(f"Data: {data}")
    heap = []

    for element in data:
        heapq.heappush(heap, element)

    print(heap)

def heap_pop():
    data = [random.randint(1, 20) for _ in range(10)]
    heapq.heapify(data)
    print(f"Data: {data}")
    print(f"HEAP POP: {heapq.heappop(data)}")
    print(f"After POP: {data}")

def heapify():
    data = [random.randint(1, 20) for _ in range(10)]
    print(f"Data: {data}")
    heapq.heapify(data)
    print(f"Heap data: {data}")

def heapreplace():
    # heapreplace = heappop + heapush
    data = []
    for _ in range(10):
        heapq.heappush(data, random.randint(1, 20))
    print(f"Data: {data}")
    for i in range(5):
        heapq.heapreplace(data, i)

    print(f"Data after replace: {data}")

def heap_small_largest():
    data = [random.randint(1,20) for _ in range(10)]
    heapq.heapify(data)
    print(f"Data: {data}")
    print(f"Smallest: {heapq.nsmallest(2, data)}")
    print(f"Largest: {heapq.nlargest(2, data)}")

def merge():
    data = []
    for i in range(4):
        new_data = [random.randint(1, 30) for _ in range(10)]
        new_data.sort() # ONLY sorted lists
        data.append(new_data)

    for i, d in enumerate(data):
        print(f"{i}: {d}")

    for d in heapq.merge(*data):
        print(f"{d} ", end="")


# heap_push()
# heap_pop()
# heapify()
# heapreplace()
# heap_small_largest()
# merge()

