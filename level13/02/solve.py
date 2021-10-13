from Crypto.Cipher import AES
import base64

"""
Trying 3.249.74.244...
Connected to ec2-3-249-74-244.eu-west-1.compute.amazonaws.com.
Escape character is '^]'.
Pzmxizm bw jm kwvncaml! = (P)repare to be confused! (caesar cipher)
(^_^)?
0n65 0n69 0n83 = AES in charcode
3840 / (22 - 7) = 256
0j43 0j42 0j43 = CBC in hex
xrl=6F796B666F68697963626E6466727A7600000000000000000000000000000000 = KEY (+13)
vi =676B7768736A6F716D76626E62646D62 = IV (+13)or reverse
Jh3pynwIdN+N70/wTHZrCRPX1bLjQ4ganC677iQ2tCkL0PnWHQX3uuWM7Ti09tyv = BASE64 CIPHERTEXT
"""
key = "6F796B666F68697963626E6466727A76"  # + 32 zeros
iv = "gkwhsjoqmvbnbdmb"[
    ::-1
]  # "676B7768736A6F716D76626E62646D62"  #   # 16 bytes could be reversed?
cipher_b64 = "Jh3pynwIdN+N70/wTHZrCRPX1bLjQ4ganC677iQ2tCkL0PnWHQX3uuWM7Ti09tyv"


def decrypt(key, iv, enc):
    # enc = base64.b64decode(enc)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.decrypt(enc)


res = decrypt(key, iv, cipher_b64)
print(res)  # NOT WORKING:(((
