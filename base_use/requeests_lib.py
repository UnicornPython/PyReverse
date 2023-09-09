import requests
import json
from bs4 import BeautifulSoup, NavigableString
import re

def zhihu_comment():
    res = requests.get(
            "https://www.zhihu.com/api/v4/questions/594333293/feeds?cursor=022dc8b45d503261c0fc433878752b81&include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Creaction_instruction%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cvip_info%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=5&offset=0&order=default&platform=desktop&session_id=1693183899470828787"
    )
    # 返回的 json 数据直接转化为字典
    data = json.loads(res.text)

    print(data['data'])


def user_agent():

    res = requests.get(
        url = "https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0",
        headers = {
            # 模拟浏览器访问
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62"
        }
    )
    dict = json.loads(res.text)
    for row in dict['subjects']:
        print(row['title'], row['url'])
   

# 定义一个 jsonp 返回的 callback 相同名称的函数
# 即可获得内部的 json 数据
def jsonp_queryMoreNums(data):
    print(data)


def jsonp():
    # 处理jsonp 格式
    res = requests.get(
        url = "http://num.10010.com/NumApp/NumberCenter/qryNum?callback=jsonp_queryMoreNums&provinceCode=11&cityCode=110&featureType=04&niceTag=1&qryType=01&searchCategory=3&goodsNet=4&_=1693226468382"
    )
    content = res.text
    # 1. 截取有用部分
    result = content.strip("jsonp_queryMoreNums(").strip(")")
    print(result)
    print("-" * 90)
    # 2. 使用 eval 处理
    eval(content)


def html_soup():
    """汽车之家"""
    res = requests.get(
        url = "https://www.autohome.com.cn/news",
    )
    # requests 默认使用 UTF8 编码
    # 这里这个网站使用的 gbk 编码
    # 要想不乱码，在解析返回报文之前，设置一下返回值的编码
    res.encoding = "gb2312"
    # 将文本内容交给 BeautifulSoup 解析
    soup = BeautifulSoup(res.text, features="html.parser")
    # 查找内容
    tag = soup.find( name = "div", attrs = {"id": "auto-channel-lazyload-article"})
    if not tag:
        return
    # 找到多个
    for li in tag.find_all(name = "li"):
        h3 = li.find(name="h3")
        if not h3 :
            continue
        # 获取标签中间的内容
        print("-------------------------")
        print(h3.text)
        # 获取标签的所有属性
        img = li.find(name="img")
        print(img)
        img_url = img.attrs['src']

        # 下载保存二进制的图片
        if not re.match(r"https?://.*", img_url):
            continue
        name = img_url.split('/')[-1]
        response = requests.get(img_url)
        with open(f"./image/{name}", mode="wb") as f:
            f.write(response.content)



def html_union():
    """爬取联通商品内容"""

    res = requests.get(
        url = "http://s.10010.com/bj/mobile/",
        headers = {
            # 模拟浏览器访问
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62"
        }
    )
    soup = BeautifulSoup(res.text, features="html.parser")
    goodsList = soup.find(name="div", attrs={ "id": "goodsList"})
    if not goodsList :
        return

    li_list = goodsList.find_all(name = "li", attrs= { "class": "goodsLi"})

    for li in li_list:
        title = li.find(name = "p", attrs = {"class": "mobileGoodsName"}).text.strip()
        price = li.find(name = "p", attrs = {"class": "evaluation"}).text.strip()
        comment = li.find(name = "p", attrs = {"class": "evalNum"}).text.strip()
        print(title)
        print(price)
        print(comment)
        print("-" * 30)



def html_json():
    """
    > 双色球开奖. 存在混合结果的情况，
    - 第一页时展示在页面上
    - 第二页往后都是 json 格式的数据
    """
    
    res = requests.get(
        url = "https://m.78500.cn/kaijiang/ssq?years=list&page=1",
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62"
        }
    )
    cookies = res.cookies.get_dict()

    soup = BeautifulSoup(res.text, features="html.parser")
    articles = soup.find(name = "article", attrs = { "id": "list"})
    for section in articles.find_all(name = "section", attrs= {"class": "item"}):
        title  = section.find(name = "strong").text
        code = section.find(name = "p").text
        print(title, code)

    
    for i in range(2,100):
        result = requests.get(
            url = f"https://m.78500.cn/kaijiang/ssq?years=list&page={i}",
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62",
                "X-Requested-With": "XMLHttpRequest",
                "Accept": "application/json",
                "Referer": "https://m.78500.cn/kaijiang/ssq/",
                "Sec-Fetch-Dest": "empty"
            },
            cookies = cookies,
        )
        data = result.json()
        info = data['list']
        for item in info:
            print(f"{item['qishu']}期 {''.join(item['result'])}")


def main():
    # zhihu_comment()
    # user_agent()
    # jsonp()
    # html_soup()
    # html_union()
    html_json()


if __name__ == "__main__":
    main()  


