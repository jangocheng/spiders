import os
import csv
import datetime
import requests

# 知乎有反爬虫，加入http headers伪装浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Connection": "keep-alive",
    "Accept": "text/html,application/json,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8"}

user_id = 'andy_pan'
zhihu_api = f'https://www.zhihu.com/api/v4/members/{user_id}?include=follower_count,voteup_count,favorited_count,thanked_count'


def open_statistic_csv(filename):
    if not os.path.isfile(filename):
        csv_writer = csv.writer(open(filename, 'w'))
        csv_writer.writerow(['Date', 'User', 'Likes', 'Follower number', 'Favorite number', 'Thankfulness number'])
        return csv_writer
    return csv.writer(open(filename, 'a+'))


if __name__ == '__main__':
    today = datetime.date.today().strftime('%Y-%m-%d')

    r = requests.get(zhihu_api, headers=headers)
    user = r.json()

    user_name = user['name']
    voteup_count = user['voteup_count']
    follower_count = user['follower_count']
    favorited_count = user['favorited_count']
    thanked_count = user['thanked_count']

    writer = open_statistic_csv('my_zhihu_statistic.csv')
    writer.writerow([today, user_name, voteup_count, follower_count, favorited_count, thanked_count])
