def Chiahetcho5(so_nhi_phan):
    """Kiểm tra xem số nhị phân có chia hết cho 5 không"""
    n = int(so_nhi_phan, 2)  # Chuyển từ nhị phân sang thập phân
    return n % 5 == 0  # Trả về True nếu chia hết cho 5, ngược lại False

# Nhập chuỗi số nhị phân từ người dùng
chuoi_nhi_phan = input("Nhập chuỗi số nhị phân (phân tách bởi dấu phẩy): ")
so_nhi_phan_list = chuoi_nhi_phan.split(",")

# Lọc ra các số chia hết cho 5
so_chiahetcho5 = [so for so in so_nhi_phan_list if Chiahetcho5(so)]

# In kết quả
if so_chiahetcho5:
    print("Các số nhị phân chia hết cho 5 là:", ",".join(so_chiahetcho5))
else:
    print("Không có số nhị phân nào chia hết cho 5")