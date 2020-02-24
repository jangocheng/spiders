# 该脚本是用来伪造不同 IP 访问点击某推广链接，可用于一些网站的推广任务，一般是
# 要求用户转发个人专属的推广链接给好友，要求有多少点击量就奖赏金币什么的。
# 代理 IP 池: https://github.com/jhao104/proxy_pool

import time
import requests
import urllib3
from requests.adapters import HTTPAdapter

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Connection": "keep-alive",
    "Accept": "text/html,application/json,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8"}

s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=2))
s.mount('https://', HTTPAdapter(max_retries=2))


def get_proxy():
    while True:
        r = requests.get("http://118.24.52.95/get/")
        if r.status_code == 200:
            return r.json()['proxy']
        else:
            print('sleep for waiting proxy...')
            time.sleep(1)


if __name__ == '__main__':
    # used_ips = dict()
    count = 0
    while True:
        # if count == 100:
        #     exit(0)
        ip_port = get_proxy()
        print('got proxy ip and port: %s' % ip_port)
        # if ip_port in used_ips:
        #     print('repeated ip, skip...')
        #     continue
        # else:
        #     used_ips[ip_port] = 1
        proxies = {
            'http': 'http://%s' % ip_port
        }
        try:
            res = s.get("http://www.93haoshu.com/?fromuid=579654", proxies=proxies, headers=headers, timeout=10)
            if res.status_code == 200:
                count += 1
                print('successful times: %d' % count)
            # print(res.content.decode())
        except (requests.exceptions.ProxyError, requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError,
                urllib3.exceptions.ReadTimeoutError, urllib3.exceptions.MaxRetryError):
            print('proxy error, continue...')
            continue
