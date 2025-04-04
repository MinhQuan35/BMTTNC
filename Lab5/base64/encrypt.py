import base64

def main():
    input_string = input("Nhập thông tin cần mã hóa: ")
    
    # Mã hóa thông tin
    encoded_bytes = base64.b64encode(input_string.encode('utf-8'))
    encoded_string = encoded_bytes.decode('utf-8')
    
    with open("data.txt", "w") as file:
        file.write(encoded_string)
        
    print("Dữ liệu đã được mã hóa và lưu vào file data.txt")

if __name__ == "__main__":
    main()