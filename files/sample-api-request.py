#!/usr/bin/python
import os
import time
import requests
import msgpack

### ** Instruction (0)
### FIXME: change to your challenge server URL
base_url = "http://localhost/"


def request(api, _input):
    global base_url
    ### NOTE: Please wait
    time.sleep(2)
    ### NOTE: Challenge server API use MsgPack
    print("\n[*] API {} with input = {}".format(api, _input))
    res = requests.post(base_url + api, data=msgpack.packb({'input': _input}))
    try:
        res_decoded = msgpack.unpackb(res.content)
        print(res_decoded)
    except Exception as f:
        print(res.content)


### ** Instruction (1)
### How to submit argv input

request('/attack/1/submit', 'AAA')


### ** Instruction (2)
### How to submit content of file

### Suppose there are removeme.txt
with open('/tmp/remove-me.txt', 'w') as f:
    f.write('BBB')

with open('/tmp/remove-me.txt') as f:
    request('/attack/3/submit', f.read())


### ** Instruction (3)
### How to download every defense rounds' files

### Recommend use curl or wget :)
time.sleep(2)
print("\n[*] Defense round file download")
os.system("curl {}/defense/latest.zip -o /tmp/latest.zip".format(base_url))
os.system("unzip -l /tmp/latest.zip")
print()


### ** Instruction (4)
### How to submit input in defense rounds

### Same with attack box
request('/defense/latest/submit', 'AAA') 
