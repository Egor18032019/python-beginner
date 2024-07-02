str_list = [[1, 2, 3], [4, 5, 6]]

for i in range(len(str_list)):
    for j in range(len(str_list[i])):
        point = str_list[i][j]
        print(point,   end=' - ')
