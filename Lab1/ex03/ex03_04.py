def truy_cap_phan_tu(tuple):
    first_element = tuple[0]
    last_element = tuple[-1]
    return first_element, last_element
input_str=eval(input("Nhập 1 chuỗi: "))
first, last = truy_cap_phan_tu(input_str)
print("Phần tử đầu tiên cuar tuple: ", first)
print("Phần tử cuối cùng của tuple:", last)