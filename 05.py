#!/usr/bin/env python3
import base64,codecs,binascii
PAY='''VGhlIHBheWxvYWQgaXMgc2VjcmV0Lg==
746869736973686578
uryyb
'''

def dec(x):
    for f in (base64.b64decode, lambda b: binascii.unhexlify(b)):
        try:
            out=f(x)
            print(out.decode())
            return
        except Exception:
            pass
    try:
        print(codecs.decode(x.decode(),'rot_13'))
    except Exception:
        print('g')

for l in PAY.splitlines():
    if not l: continue
    dec(l.encode())
