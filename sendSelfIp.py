import os
import time
import requests

timestr = ''
timestr = time.strftime('%Y-%m-%d %H:%M',time.localtime(time.time()))
print(timestr)

content = ''
#command = 'curl icanhazip.com'
command = 'curl http://members.3322.org/dyndns/getip'
r = os.popen(command)
info = r.readlines()
for line in info:
    content += line

file_object = open('/home/u-viruser/soft/python/lastip')
try:
    lastip = file_object.read()
finally:
    file_object.close()
lastip = lastip.strip()
print('lastip: |' + lastip + '|')
content = content.strip()
print('content: |' + content+'|')

if content == lastip:
    print('the are same');
else:

    postdata = {'outip':content,'name':'gs'}
    r = requests.post("http://5:9090//c", data=postdata)

    print(r.text)


    file_object = open('/home/u-viruser/soft/python/lastip', 'w')
    file_object.write(content)
    file_object.close()