import base64

def main():
    try:
    # Đọc dữ liệu từ file
        with open("data.txt", "r") as file:
            encoded_string = file.read().strip()
    
    # Giải mã thông tin
        decoded_bytes = base64.b64decode(encoded_string)
        decoded_string = decoded_bytes.decode("utf-8")
    
        print("Dữ liệu đã được giải mã:", decoded_string)
    except Exception as e:
        print("Lỗi", e)

if __name__ == "__main__":
    main()
    