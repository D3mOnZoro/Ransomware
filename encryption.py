from cryptography.fernet import Fernet
def gene_key():
    key = Fernet.generate_key()
    with open("key.khi","wb") as key_file:
        key_file.write(key)
def load_key():
    return open("key.khi","rb").read()
def encryption(filename,key):
    with  open(filename,"rb") as file:
        file1=file.read()
    f = Fernet(key)
    encrypted_data = f.encrypt(file1)
    with open("encrypted_file","wb") as encryptt:
        encryptt.write(encrypted_data)

def decryption(filename,key):
    with open("encrypted_file","rb") as file:
        file= file.read()
    f = Fernet(key)
    decrypted_data = f.decrypt(file)
    with open("decrypted_file","wb") as decryptt:
        decryptt.write(decrypted_data)
gene_key()
encryption("msg.txt",load_key())
decryption("encrypted_file",load_key())


