from time import time
import random
from string import ascii_letters as lt
from hashlib import md5 as __md__
import requests
from mogo_db import create_coin, COEFF


def md5(string, encoding="utf-8"):
    return str(__md__(str(string).encode(encoding)).hexdigest())


id = "173996641"
print(md5(id)[:COEFF])
start = time()
while True:
    test_string = id + "-" + "".join([random.choice(lt) for i in range(10)])
    if md5(test_string)[:COEFF] == md5(str(id))[:COEFF]:

        print(str(create_coin(test_string)['status'])+":")
        text = "%s\n%s\n" % (test_string, (time() - start))
        print(text)
        print(text, file=open('keys.txt', 'a'))
        print(test_string, file=open('only_keys.txt', 'a'))
        start = time()

"""
173996641-yAzyTJpmoU
173996641-btuFNFdxMh
"""