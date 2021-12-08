import requests
import json


def get_information_php(url1, url2):

  #home = requests.get(url1)
  #cookieJar = home.cookies
  #phpsessid = cookieJar["PHPSESSID"]
  #print("phpsessid", phpsessid)
  payload = {
    "field": "time",
    "order": "DESC",
    "pageNum": "0",
    "maxRows": "20",
    "keyword": "",
    "uid": "WID_0_2_0516b5aba93b58b0547367faafb2f1dbe2ebba4c",
    "tf": "1",
    "auth_type": "user",
    "use_cache": "1"
  }
  headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": f"PageLang=zh-tw; PHPSESSID=xxxx",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43",
    "X-Requested-With": "XMLHttpRequest",
  }
  news = requests.post(url2, data = payload, headers = headers)

  news = json.loads(news.__dict__["_content"].decode('utf-8'))
  titles = [news[i]["title"] for i in range(1, 2)]
  times = [news[i]["time"] for i in range(1, 2)]
  return titles, times


a = get_information_php("http://www.hchs.hc.edu.tw/home",
                    "http://www.hchs.hc.edu.tw/ischool/widget/site_news/news_query_json.php")

print(a) 
