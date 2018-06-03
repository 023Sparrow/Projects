import base64

def encrpt(s):
    return base64.b64encode(bytes(s,encoding='utf-8'))

def decrypt(b):
    return str(base64.b64decode(b),encoding='utf-8')
