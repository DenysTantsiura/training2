class Graph:
    def __init__(self):
        self.data = {}

    def adds(self, key, item):
        try:
            self.data[key] = item
        
        except TypeError as err:
            print(f'1 {err}')

        except Exception as err:
            print(f'2 {err}')

    def extracts(self):
        if self.data:
            return self.data.popitem()  # Python 3.7+ = removes the item that was last inserted into the dictionary
        
        else:
            return 'Graph is empty.'
        
    def __str__(self):
        return f'{self.data}'
    
    
a = []
b = [1]
c = {'1': 100}
test1 = Graph()
test1.adds(0, 100)
test1.adds(None, 200)
test1.adds((1, 2), 300)
test1.adds(a, 400)
test1.adds(b, 400)
test1.adds(c, 400)
print(test1.data)
test2 = Graph()
test2.adds(0, 10)
test2.adds(None, 20)
test2.adds((3, 4), 30)
test1.adds('c', test2)
print(test1.data)
print(test1.data['c'])
