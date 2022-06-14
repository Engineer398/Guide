import collections

# collections.chinmap - объединение нескольких словарей
def show_chainmap():
    a = {"a" : "A", "b" : "B"}
    b = {"b" : "B", "c" : "C"}
    # Create chainmap
    chain = collections.ChainMap(a, b)
    # Show chainmap
    print("a = {}".format(chain["a"]))
    print("b = {}".format(chain["b"]))
    print("c = {}".format(chain["c"]))
    print("Keys = {}".format(chain.keys()))
    print("Values = {}".format(chain.values()))
    # chainmap.map
    print("First map = {}".format(chain.maps[0]))
    print("Second map = {}".format(chain.maps[1]))
    chain.maps = list(reversed(chain.maps))
    print("Reverse maps in chain = {}".format(chain.maps))
    # Change value in chain
    a["a"] = "Z"
    print("After changing = {}".format(chain.maps))

    new_chain = chain.new_child()
    print("After chain: {}".format(chain))
    print("After new_chin: {}".format(new_chain))
    new_chain["c"] = "V"
    print("Before chain: {}".format(chain))
    print("Before new chain: {}".format(new_chain))

# show_chainmap()

def show_counter():
    # Inicilization
    print(collections.Counter(["a", "b", "c", "a", "b", "b"]))
    print(collections.Counter({"a" : 2, "b": 3, "c" : 1}))
    print(collections.Counter(a=2, b=3, c=1))
    # Update
    c = collections.Counter()
    c.update("abcdaab")
    print("Sequence: {}".format(c))
    c.update({"a" : 1, "d" : 5})
    print("Update Sequence: {}".format(c))
    # Output
    for letter in "abcde":
        print("{}: {}".format(letter, c[letter]))
    print("Elements: {}".format(list(c.elements())))
    # find most common
    print("Most common: {}".format(c.most_common(3)))
    # Arifmeticks with counter
    a = collections.Counter(a=3, b=7, d=4)
    b = collections.Counter(a=1, c=2, d=2)
    c = a + b
    print(c)

# show_counter()

def simple_func():
    print("It's simple func")
    return "Default value"

def show_default_dict():
    a = collections.defaultdict(simple_func, bar="bar")
    print(a)
    print("bar: {}".format(a["bar"]))
    print("pub: {}".format(a["pub"]))

# show_default_dict()

# Двухсторонняя очередь - тот же list, только двухсторонний
def show_deque():
    d = collections.deque("abcdef")
    d.maxlen = 10 # ограничение максимальной длинны
    print(d)
    print(f"LEN: {len(d)}")
    print("Left end: {}".format(d[0]))
    d.extendleft("wzx")
    z = d.popleft()
    print("POP: {}".format(z))
    print(d)
    d.rotate(3) # + прокрутка очереди
    print(d)

# show_deque()

# Это просто именованный tuple
def show_nametuple():
    point = collections.namedtuple("Point", ["x", "y"])
    p1 = point(x=10, y=34)
    print(f"Obj: {p1}, obj.x: {p1.x}, obj.y: {p1.y}")
    try:
        p1.x = 11 # can't set new value because its tuple
    except AttributeError as e:
        print(f"Error: {e}")

# show_nametuple()

# Класс OrderedDict — это подкласс словаря, запоминающий порядок добавления содержимого.
def show_orderdict():
    tst_map = {}
    tst_map.update(b="asd", a="A" , c="c")
    print(tst_map)
    tst_dict = collections.OrderedDict()
    tst_dict["a"] = "A"
    tst_dict["b"] = "asd"
    tst_dict["c"] = "c"
    print(tst_dict)

# show_orderdict()

