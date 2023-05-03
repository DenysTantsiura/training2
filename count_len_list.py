test_list = [10, 2, 3, 4, 5, 6] 
print(len(test_list))


def len_list_counter(test_list: list) -> int:
    if test_list == []:
        return 0
    
    return 1 + len_list_counter(test_list[1:])


print(len_list_counter(test_list))
