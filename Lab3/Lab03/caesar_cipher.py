import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnEncrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btnDecrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plain_text": self.ui.txtPlainText.toPlainText(),
            "key": self.ui.txtKey.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()  # Kiểm tra lỗi HTTP
            data = response.json()
            print("API Response:", data)  # In phản hồi API
            self.ui.txtCipherText.setText(data["encrypted_text"])  # Khóa đã sửa

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Encrypted Successfully")
            msg.exec_()
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e)
        except KeyError as e:
            print("KeyError:", e)


    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": self.ui.txtCipherText.toPlainText(),  # Đã sửa tên của trường văn bản đơn giản.
            "key": self.ui.txtKey.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            data = response.json()
            print("API Response:", data)
            self.ui.txtPlainText.setText(data["decrypted_message"])  # Khóa đã sửa

            msg = QMessageBox()
            msg.setIcon(QMessageBox.information)
            msg.setText("Decrypted Successfully")
            msg.exec_()
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e)
        except KeyError as e:
            print("KeyError:", e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())