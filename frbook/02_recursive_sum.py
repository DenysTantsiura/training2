listmy = [
 1, 2, 3, 4]
print(sum(listmy))


def sum1(list):
  if list == []:
    return 0
  
  return list[0] + sum1(list[1:])


print(sum1(listmy))
