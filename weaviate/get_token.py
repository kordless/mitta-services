#!/usr/bin/python3
# get token from gcp tag
import httplib2
http = httplib2.Http()
url = 'http://metadata.google.internal/computeMetadata/v1/instance/tags'
headers = {'Metadata-Flavor': 'Google'}
response, content = http.request(url, 'GET', headers=headers)
evalcontent = eval(content)
for item in evalcontent:
        if 'token' in item:
                key,token = item.split('-')
        if 'openai' in item:
                key,openai_token_1,openai_token_2 = item.split('-')

# set nginx password with http token
import os, sys
user = sys.argv[1]
os.system("/usr/bin/htpasswd -b -c /etc/nginx/htpasswd %s %s" % (user, token))

# drop it for the env
f = open('bidntoken', 'w')
f.write("TOKEN=%s\n" % token)
f.close()

f1 = open('config.sh', 'w')
f1.write("OPENAI_TOKEN=%s-%s\n" % (openai_token_1,openai_token_2))
f1.close()