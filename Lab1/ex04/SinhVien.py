# File: SinhVien.py
class SinhVien:
    def __init__(self, id, name, sex, major, diemTB):
        self._id = id
        self._name = name
        self._sex = sex
        self._major = major
        self._diemTB = diemTB
        self._hocLuc = ""
        self.xepLoaiHocLuc()
    def xepLoaiHocLuc(self):
        """Xếp loại học lực dựa trên điểm trung bình"""
        if self._diemTB >= 8.5:
            self._hocLuc = "Giỏi"
        elif self._diemTB >= 7.0:
            self._hocLuc = "Khá"
        elif self._diemTB >= 5.0:
            self._hocLuc = "Trung bình"
        else:
            self._hocLuc = "Yếu"