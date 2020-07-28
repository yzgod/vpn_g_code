#!/usr/bin/env python
# -*- coding:utf-8 -*-

import hmac
import hashlib
import base64
import struct
import time
import sys

def g_code_3(token):
    key = base64.b32decode(token)
    pack = struct.pack(">Q", int(time.time()) // 30)   # 将间隔时间转为big-endian(大端序)并且为长整型的字节
    sha = hmac.new(key, pack, hashlib.sha1).digest() # 使用hmac sha1加密,并且以字节的方式取出 = b'\x0f\x1a\xaeL\x0c\x8e\x19g\x8dv}\xde7\xbc\x95\xeal\xa3\xc1\xee'
    o = sha[19] & 15  # bin(15)=00001111=0b1111

    pwd = str((struct.unpack(">I", sha[o:o + 4])[0] & 0x7fffffff) % 1000000)
    code = str(0) + str(pwd) if len(pwd) < 6 else pwd
    return code

if __name__ == '__main__':
    print(g_code_3(token=sys.argv[1]))