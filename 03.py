#!/usr/bin/env python3
import base64,binascii,codecs,urllib.parse,zlib,gzip,io
ENC='''VGhpcyBpcyBhIHZlcnkgc2VjcmV0IGxpbmUuCjE2NDEyMzQ1Njc4OTAK
6162636465666768696a6b6c6d6e6f70
uryybjbeyq
%70%72%69%6e%74%28%22%48%65%6c%6c%6f%22%29
R0lGSw0KVGhpcyBpcyBhIHBsZWFzZQ==
'''

def b64(b): return base64.b64decode(b)
def hx(b): return binascii.unhexlify(b)
def r13(b): return codecs.decode(b.decode(),'rot_13').encode()
def url(b): return urllib.parse.unquote(b.decode()).encode()
def gz(b):
    f=io.BytesIO(b)
    with gzip.GzipFile(fileobj=f) as g: return g.read()

decoders=[b64,r13,hx,lambda x:x[::-1],url]

def try_decode(e):
    cur=e.encode()
    for d in decoders:
        try:
            cur=d(cur)
        except Exception:
            pass
    try:
        print(cur.decode())
    except Exception:
        print('partial:',cur[:200])

if __name__=='__main__':
    try_decode(ENC)
