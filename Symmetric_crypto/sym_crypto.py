from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken

class Crypto():
    def __init__(self):
        self.key = Fernet.generate_key()

    def crypt(self, file):
        file_path = file.split('.')
        data = open(file, 'rb').read()
        crypto = Fernet(self.key)
        encrypted_data = crypto.encrypt(data)
        encrypted_path = ("_encrypted.".join(map(str, file_path)))
        try:
            with open(encrypted_path, 'wb') as f:
                f.write(encrypted_data)
                return True
        except:
            return False
    
    def decrypt(self, file, key):
        crypto = Fernet(key)
        encrypted_path = file.split('.')
        decrypted_path = ("_decrypted.".join(map(str, encrypted_path)))
        with open(file, 'rb') as file_enc:
            try:
                data = crypto.decrypt(file_enc.read())
                with open(decrypted_path, 'wb') as file_rec:
                        file_rec.write(data)
                        return True
            except InvalidToken:
                print('O arquivo não está encriptado corretamente')
                return False

# c = Crypto()
# c.encrypt('image.png')
# key = c.key
# c.decrypt('image_encrypted.png', key)