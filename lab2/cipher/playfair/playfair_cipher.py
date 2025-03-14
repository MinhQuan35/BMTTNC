class PlayfairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I").upper()
        key_set = set(key)
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        remaining_letter = [letter for letter in alphabet if letter not in key_set]
        matrix = list(key) + remaining_letter[:25 - len(key)]
        return [matrix[i:i+5] for i in range(0, len(matrix), 5)]

    def find_letter_coords(self, letter, matrix):
        for i in range(len(matrix)):  
            for j in range(len(matrix[i])):  
                if matrix[i][j] == letter:
                    return i, j
        return None  # Tránh lỗi nếu không tìm thấy ký tự

    def encrypt(self, text, matrix):
        text = text.replace("J", "I").upper()
        encrypted_text = ""

        for i in range(0, len(text), 2):
            pair = text[i:i+2]
            if len(pair) == 1:
                pair += "X"

            row1, col1 = self.find_letter_coords(pair[0], matrix)
            row2, col2 = self.find_letter_coords(pair[1], matrix)

            if row1 == row2:
                encrypted_text += matrix[row1][(col1+1) % 5] + matrix[row2][(col2+1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1+1) % 5][col1] + matrix[(row2+1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]

        return encrypted_text

    def decrypt(self, text, matrix):
        text = text.upper()
        decrypted_text = ""

        for i in range(0, len(text), 2):
            pair = text[i:i+2]
            row1, col1 = self.find_letter_coords(pair[0], matrix)
            row2, col2 = self.find_letter_coords(pair[1], matrix)

            if row1 == row2:
                decrypted_text += matrix[row1][(col1-1) % 5] + matrix[row2][(col2-1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1-1) % 5][col1] + matrix[(row2-1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]

        # Loại bỏ ký tự 'X' dư thừa
        banro = ""
        skip = False
        for i in range(len(decrypted_text)):
            if i < len(decrypted_text) - 1 and decrypted_text[i] == 'X' and decrypted_text[i-1] == decrypted_text[i+1]:
                skip = True
            elif skip:
                skip = False
            else:
                banro += decrypted_text[i]

        return banro
