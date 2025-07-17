my_list = []
my_list = [10, 20, 30, 40]
my_list[1] = 32
print(my_list)
my_list2 = [50, 60, 70]
my_list.extend(my_list2)
print(my_list)
my_list.remove(70)
print(my_list)
my_list.sort()
print(my_list)
index = my_list.index(30)
print(index)