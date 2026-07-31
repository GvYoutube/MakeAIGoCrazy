#!/usr/bin/env python3
import base64,codecs,binascii,urllib.parse
G='''
cHJpbnQoJ0hlbGxvJyk=
6d657373616765
uryyb
%70%72%69%6e%74%28%22VGVzdFwiKQ%3D%3D%22%29
'''

def d_b64(b): return base64.b64decode(b)
def d_hex(b): return binascii.unhexlify(b)
def d_rot(b): return codecs.decode(b.decode(),'rot_13').encode()
def d_url(b): return urllib.parse.unquote(b.decode()).encode()

L=[d_b64,d_rot,d_hex,d_url]

for line in G.splitlines():
    if not line.strip(): continue
    cur=line.strip().encode()
    for f in L:
        try:
            cur=f(cur)
        except Exception:
            pass
    try:
        print(cur.decode())
    except Exception:
        print('garb:',cur[:80])
