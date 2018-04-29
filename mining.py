from time import time
import random
from string import ascii_letters as lt
from hashlib import md5 as __md__
import requests


def md5(string, encoding="utf-8"):
    return str(__md__(str(string).encode(encoding)).hexdigest())


id = "id1"
print(md5(id))
start = time()
while True:
    test_sting = "%s-" % id + "".join([random.choice(lt) for i in range(10)])
    if md5(test_sting)[:4] == md5(str(id))[:4]:
        text = "%s\n%s\n" % (test_sting, (time() - start))
        print(text)
        print(text, file=open('keys.txt', 'a'))
        start = time()

"""
173996641-yAzyTJpmoU
173996641-btuFNFdxMh
"""