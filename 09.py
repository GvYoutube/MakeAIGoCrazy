#!/usr/bin/env python3
import base64,binascii,codecs,urllib.parse
Z='''VGVzdERhdGE=
73616d706c65
uryyb
%72%65%76%65%72%73%65
'''

def dec(x):
    try: print(base64.b64decode(x).decode()); return
    except: pass
    try: print(binascii.unhexlify(x).decode()); return
    except: pass
    try: print(codecs.decode(x.decode(),'rot_13')); return
    except: pass
    try: print(urllib.parse.unquote(x.decode())); return
    except: print('g')

for l in Z.splitlines():
    if not l: continue
    dec(l.encode())
