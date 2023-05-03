class Queue:
    def __init__(self, item = None):
        self.data = []
        self.data.append(item) if not isinstance(item, type(None)) else None

    def adds(self, new_item):
        self.data.append(new_item) if not isinstance(new_item, type(None)) else None

        return self.data[-1]

    def extracts(self):
        if self.data:
            return self.data.pop(0)
        
        else:
            return 'Queue is empty.'


test1 = Queue()
[print(test1.adds(i)) for i in range(10)]
[print(test1.extracts()) for _ in range(12)]
