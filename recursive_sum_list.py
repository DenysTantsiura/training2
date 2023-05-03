
def recursive_sum_list(inputed_list: list) -> int:
    if inputed_list == []:
        return 0
    
    return inputed_list[0] + recursive_sum_list(inputed_list[1:])


test_list = [10, 2, 3, 4, 5, 6]  # 30

print(recursive_sum_list(test_list))
