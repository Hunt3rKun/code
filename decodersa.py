"""
flag = open('flag.txt','r').read()
N = 221
e = 5
enc = b''

for i in flag:
    enc += bytes([pow(ord(i),e,N)])
    # ord()以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值
    # bytes()只负责以字节序列的形式（二进制形式）来存储数据
    字节串转字符串:
    # 字节码解码为字符串: bytes(b'\x31\x32\x61\x62').decode('ascii')  ==>  12ab
    # 字节串转16进制表示,夹带ascii: str(bytes(b'\x01\x0212'))[2:-1]  ==>  \x01\x0212
    # 字节串转16进制表示,固定两个字符表示: str(binascii.b2a_hex(b'\x01\x0212'))[2:-1]  ==>  01023132
    # 字节串转16进制数组: [hex(x) for x in bytes(b'\x01\x0212')]  ==>  ['0x1', '0x2', '0x31', '0x32']
encrypt = open('encrypt','wb')
encrypt.write(enc)
encrypt.close()
"""

encrypt = open('encrypt','rb+').read()      # 以二进制模式追加读取文件
# encrypt : b'f[TCSjy\x1d\x1d!34m3UU\xda\xbf6mU!4\xaf\xbas\x1dm\xac4UB\xbf3\xba\x1d\xaf\x1d\xb1'
# 将二进制转换成ASCI码
for item in encrypt:
    print(item,end=' ')     # 102 91 84 67 83 106 121 29 29 33 51 52 109 51 85 85 218 191 54 109 85 33 52 175 186 115 29 109 172 52 85 66 191 51 186 29 175 29 177
# 对每一项进行解密，得到相应字符的ASCII码
"""
from Crypto.Util.number import long_to_bytes
p=13
q=17
e=5
def exgcd(a, n):
    if n == 0:
        return 1, 0
    else:
        x, y = exgcd(n, a % n)
        x, y = y, x - (a // n) * y
        return x, y
def getReverse(a, n):
    re, y = exgcd(a, n)
    while (re < 0):
        re += n
    return re
if __name__ == "__main__":

    d = getReverse(e, (p - 1) * (q - 1))
    n = p * q
    encrypt = open('encrypt', 'rb+').read()
    flag =''
    s = ''
    for c in encrypt:
        m = pow(c, d, n)
        plaintext = long_to_bytes(m)
        flag = bytes(plaintext).decode('ascii')
        print(flag,end='')
"""



