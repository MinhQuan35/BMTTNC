import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.ecc import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Kết nối nút với hàm
        self.ui.btn_gen_keys.clicked.connect(self.call_api_gen_keys)
        self.ui.btn_sign.clicked.connect(self.call_api_sign)
        self.ui.btn_verify.clicked.connect(self.call_api_verify)

    def show_message(self, title, message):
        """Hiển thị hộp thoại thông báo"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.information)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()

    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/ecc/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                self.show_message("Success", data.get("message", "Keys generated successfully"))
            else:
                self.show_message("Error", f"Failed to generate keys: {response.status_code}")
        except requests.exceptions.RequestException as e:
            self.show_message("Error", f"API request failed: {e}")

    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/ecc/sign"
        message = self.ui.txt_info.toPlainText()
        if not message:
            self.show_message("Warning", "Please enter a message to sign!")
            return

        payload = {"message": message}
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_sign.setText(data.get("signature", ""))
                self.show_message("Success", "Message signed successfully.")
            else:
                self.show_message("Error", f"Failed to sign message: {response.status_code}")
        except requests.exceptions.RequestException as e:
            self.show_message("Error", f"API request failed: {e}")

    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/ecc/verify"
        message = self.ui.txt_info.toPlainText()
        signature = self.ui.txt_sign.toPlainText()

        if not message or not signature:
            self.show_message("Warning", "Please enter both message and signature to verify!")
            return

        payload = {"message": message, "signature": signature}
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if data.get("is_verified"):
                    self.show_message("Success", "Signature verified successfully.")
                else:
                    self.show_message("Fail", "Signature verification failed.")
            else:
                self.show_message("Error", f"Failed to verify signature: {response.status_code}")
        except requests.exceptions.RequestException as e:
            self.show_message("Error", f"API request failed: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
