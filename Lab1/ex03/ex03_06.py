def xoa_phan_tu(dict, key):
    if key in dict:
        del dict[key]
        return True
    else:
        return False
    
my_dict = {'a':1, 'b':2, 'c':3, 'd':4}
key_to_delete = 'b'
result = xoa_phan_tu(my_dict, key_to_delete)
if result:
        print("Dictionary sau khi xóa phần tử:", my_dict)
else:
        print("Phần tử không tồn tại trong dictionary")