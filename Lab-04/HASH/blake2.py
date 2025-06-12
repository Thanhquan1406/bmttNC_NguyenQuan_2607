import hashlib

def sha3(message):
    sha3_hash = hashlib.blake2b(digest_size=64)
    sha3_hash.update(message)
    return sha3_hash.digest()

def main():
    text = input("Nhap chuoi: ").encode('utf-8')
    hashed_text = sha3(text)

    print("Chuoi van ban da nhap: ", text.decode('utf-8'))
    print("blake2b HASH: ", hashed_text.hex())



if __name__ == "__main__":
    main()