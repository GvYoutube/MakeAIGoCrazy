#!/usr/bin/env python3
import base64,codecs,binascii
H='''R0lG
7072696e74
uryyb
QGJhc2U2NA==
'''

def p(b):
    try: print(base64.b64decode(b).decode())
    except Exception:
        try: print(binascii.unhexlify(b).decode())
        except Exception:
            try: print(codecs.decode(b.decode(),'rot_13'))
            except Exception: print('g')

for s in H.splitlines():
    if not s: continue
    p(s.encode())
