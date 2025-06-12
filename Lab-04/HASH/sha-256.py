import hashlib

def calculate(input_string):
    md5_hash = hashlib.sha256()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()

input_string = input("nhap chuoi can bam: ")
md5_hash = calculate(input_string)

print("Ma bam SHA-256 cua chuoi '{}' la: {}".format(input_string, md5_hash))