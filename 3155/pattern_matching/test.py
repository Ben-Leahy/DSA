
# my_list = ["1", "2", "3", "4"]
my_list = "abbba"
new = my_list + my_list
matrix = []
for i in range(len(my_list)):
    matrix.append(new[i:(len(my_list) + i)])
print(matrix)
matrix.sort()
print(matrix)