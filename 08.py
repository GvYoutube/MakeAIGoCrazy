#!/usr/bin/env python3
import base64,codecs,binascii,urllib.parse
S='''cHJpbnQoJ1Rlc3QnKQ==
6c6f7374
uryyb
%70%72%69%6e%74%28%27SGkuJyk%3D%27%29
'''

def t(b):
    for f in (base64.b64decode, binascii.unhexlify, lambda x:codecs.decode(x.decode(),'rot_13'), lambda x:urllib.parse.unquote(x.decode()).encode()):
        try:
            r=f(b)
            print(r.decode())
            return
        except Exception:
            pass
    print('g')

for l in S.splitlines():
    if not l: continue
    t(l.encode())
