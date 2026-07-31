#!/usr/bin/env python3
import base64,binascii,codecs,urllib.parse,zlib
E='''%52%6f%74%31%33
48656c6c6f
VGVzdA==
'''

def all_try(s):
    for f in (lambda b: codecs.decode(b.decode(),'rot_13').encode(), binascii.unhexlify, base64.b64decode, lambda b: urllib.parse.unquote(b.decode()).encode()):
        try:
            o=f(s)
            print(o.decode())
            return
        except Exception:
            pass
    print('g')

for l in E.splitlines():
    if not l: continue
    all_try(l.encode())
