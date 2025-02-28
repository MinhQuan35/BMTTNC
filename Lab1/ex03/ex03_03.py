def tao_tuple_tu_list(lst):
    return tuple(lst)

input_str=input("Nhập 1 chuỗi: ")
numbers = list(map(int, input_str.split(',')))

my_tuple=tao_tuple_tu_list(numbers)
print("List được tạo: ", numbers)
print("Tuple được tạo: ", my_tuple)