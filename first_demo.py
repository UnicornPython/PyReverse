import requests

cookies = {
    'ASP.NET_SessionId': 'm1yyrjykt4h2yuex4qqooaxv',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'ASP.NET_SessionId=m1yyrjykt4h2yuex4qqooaxv',
    'Origin': 'https://ggzyfw.fj.gov.cn',
    'Referer': 'https://ggzyfw.fj.gov.cn/index/newList?type=11',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62',
    'portal-sign': 'd08fde0f29fa0fb7a24e6fe856b51850',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'pageNo': 3,
    'pageSize': 10,
    'total': 600,
    'type': '11',
    'timeType': '0',
    'ts': 1693007267257,
}

response = requests.post('https://ggzyfw.fj.gov.cn/FwPortalApi/Article/PageList', cookies=cookies, headers=headers, json=json_data).json()
print(response)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"pageNo":3,"pageSize":10,"total":600,"type":"11","timeType":"0","ts":1693007267257}'
#response = requests.post('https://ggzyfw.fj.gov.cn/FwPortalApi/Article/PageList', cookies=cookies, headers=headers, data=data)
