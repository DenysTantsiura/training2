test_list = [10, 2, -3, 4, 22, 5, 33, 6] 
print(max(test_list))


def maximum_in_list(test_list: list) -> int:
    if len(test_list) < 2:
        return test_list[0] if len(test_list) == 1 else None
    
    return test_list[0] if test_list[0] >= maximum_in_list(test_list[1:]) else maximum_in_list(test_list[1:])


print(maximum_in_list(test_list))
print(maximum_in_list([]))
print(maximum_in_list([99]))
