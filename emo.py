import time
import urllib.request
import urllib.parse
import json
import hashlib
import base64

#接口地址
url ="http://ltpapi.xfyun.cn/v2/sa"
#开放平台应用ID
x_appid = "94068166"
#开放平台应用接口秘钥
api_key = "9b3558fef5d89985222246653cfa197c"


def emo(text):
    body = urllib.parse.urlencode({'text': text}).encode('utf-8')
    param = {"type": "dependent"}
    x_param = base64.b64encode(json.dumps(param).replace(' ', '').encode('utf-8'))
    x_time = str(int(time.time()))
    x_checksum = hashlib.md5(api_key.encode('utf-8') + str(x_time).encode('utf-8') + x_param).hexdigest()
    x_header = {'X-Appid': x_appid,
                'X-CurTime': x_time,
                'X-Param': x_param,
                'X-CheckSum': x_checksum}
    req = urllib.request.Request(url, body, x_header)

    """从返回的result(字符串)中提取结果 rjl 0909"""
    result = urllib.request.urlopen(req)
    result = result.read().decode('utf-8')
    print(result)
    result = result.split(':')[4][0]
    if result == '-':
        return 'negative'
    elif result == '0':
        return 'neutral'
    else:
        return 'positive'

