import hashlib


def encryption_md5(s):
    encryption = hashlib.md5()
    encryption.update(s.encode('utf-8'))
    return encryption.hexdigest()