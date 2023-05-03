def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        # print('*')
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        
        if guess > item:
            high = mid - 1

        else:
            low = mid + 1

    return None


my_list = [1, 3, 5, 7, 8, 10]


# Not normal worked!:
def rbinary_search(list, item):
    # print('*')

    if list == [] or item < list[0] or item > list[-1]:
        return None
    
    if len(list) == 1:
        return None if list[0] != item else 0

    low = 0
    high = len(list)-1
    mid = (low + high) // 2
    slide = (low + high) % 2

    if list[mid] >= item:
        if list[mid] == item:
            return mid
        
        next_one = rbinary_search(list[:mid+1], item)
        if isinstance(next_one, int):
            return next_one
        
        else:
            return None
    
    else:
        slide += 1 if len(list[mid+1:]) == 1 else 0
        next_one = rbinary_search(list[mid+1:], item)

        if isinstance(next_one, int):
            return mid + slide + next_one
        
        else:
            return None


test_items = (-1, 1, 2, 3, 5, 7, 8, 9, 10, 100)
test_answers = (None, 0, None, 1, 2, 3, 4, None, 5, None)


def test(fun, i):
    print(f'{fun(my_list, test_items[i])} ? {test_answers[i]}')
    # assert fun(my_list, test_items[i]) == test_answers[i]

# [test(binary_search, i) for i in range(len(test_items))]
# [test(rbinary_search, i) for i in range(len(test_items))]

my_list = [1, 3, 5, 7, 8, 10, 15, 16, 20, 22, 23]
test_items = (-1, 1, 2, 3, 5, 7, 8, 9, 10, 100, 15, 16, 18, 20, 22, 23)
test_answers = (None, 0, None, 1, 2, 3, 4, None, 5, None, 6, 7, None, 8, 9, 10)
# [test(binary_search, i) for i in range(len(test_items))]
[test(rbinary_search, i) for i in range(len(test_items))]
