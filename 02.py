#!/usr/bin/env python3
import base64,binascii,codecs,urllib.parse,random
_vocab=[(["b64"],"YXBwbGU="),(["b64"],"YmFuYW5h"),(["b64"],"Y2hlcnJ5"),(["rot13"],"abbxvr"),(["hex"],"70656172"),(["url"],"%66%6c%75%6d%65")]

def _d(chain,s):
    cur=s
    for scheme in reversed(chain):
        if scheme=="b64": cur=base64.b64decode(cur).decode('utf-8')
        elif scheme=="hex": cur=binascii.unhexlify(cur).decode('utf-8')
        elif scheme=="rot13": cur=codecs.decode(cur,'rot_13')
        elif scheme=="url": cur=urllib.parse.unquote(cur)
    return cur

def r(n=1):
    c=random.choice(_vocab)
    w=_d(c[0],c[1])
    return w if n==1 else [r() for _ in range(n)]

if __name__=='__main__':
    for _ in range(6): print(r())
