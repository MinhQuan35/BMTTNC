def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

int_list = input("Nhập dãy số nguyên (phân tách bởi dấu phẩy): ")
numbers=list(map(int,int_list.split(",")))
tong_chan=tinh_tong_so_chan(numbers)
print("Tổng các số chẵn trong dãy là:", tong_chan)
