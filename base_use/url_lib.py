#!/usr/bin/python

import urllib.request as req
import urllib.parse as urlparse
import string
import json


def format_output(msg, err=None):
    print("---------------------------------------------------------")
    print("msg >:", msg)
    print("err >:", err)
    print("---------------------------------------------------------")


def get_token():
    host_url = "http://mspapitoken.onecloud.zj.chinamobile.com:8081"
    clinet_id = 16288
    client_secret = "0235e9dc34d5a29f99195cbf5a5b9038"
    grant_type = "client_credentials"
    url = str.format(
        '{}/oauth/token?client_id={}&client_secret={}&grant_type={}', host_url,
        clinet_id, client_secret, grant_type)

    resp = req.urlopen(urlparse.quote(url, safe=string.printable))
    data = json.loads(resp.read().decode("utf-8"))
    if data['access_token'] is None:
        format_output("获取token失败")
        return None
    token = data["access_token"]
    format_output("获取token成功" + token)
    return token


def main():
    # 获取 token
    token = get_token()
    if token is None:
        return
    # 组装参数, 获取 sign
    req.urlopen("")


if __name__ == "__main__":
    main()
