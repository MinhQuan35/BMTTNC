def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]

input_str=input("Nhập 1 chuỗi: ")
numbers = list(map(int, input_str.split(',')))

list_dao_nguoc=dao_nguoc_chuoi(numbers)
print("Chuỗi đảo ngược:", list_dao_nguoc)