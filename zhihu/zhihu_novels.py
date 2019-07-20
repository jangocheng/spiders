import re

import requests

# 知乎有反爬虫，加入http headers伪装浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Connection": "keep-alive",
    "Accept": "text/html,application/json,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8"}

# 知乎问题id
question_id = 281185483

if __name__ == '__main__':
    novels_file = '281185483.txt'
    interval = 20
    offset = 0
    rank = 100
    novels_count = dict()

    # 正则匹配被《》括起来的书名
    rex = r'《.+?》'
    while True:
        print(f'答案数 {offset} 到 {offset + interval}')
        # 知乎获取回答分页API
        url = f'https://www.zhihu.com/api/v4/questions/{question_id}/answers?include=content&limit={interval}&offset={offset}&sort_by=default'
        r = requests.get(url, headers=headers)
        answers = r.json()['data']
        if len(answers) == 0:
            break
        for answer in answers:
            # 结果去重，过滤掉同一个回答里的多次提及导致的重复统计
            results = set(re.findall(rex, answer['content']))
            for novel_name in results:
                if novel_name in novels_count:
                    novels_count[novel_name] += 1
                else:
                    novels_count[novel_name] = 1
        offset += interval

    # 把结果按提名次数从高到低排序
    novels_rank_list = sorted(novels_count.items(), key=lambda x: x[1], reverse=True)
    print(f'提名电影总数：{len(novels_rank_list)}')

    # 将统计结果保存到本地文件
    with open(novels_file, 'w') as f:
        f.write(f'提名电影总数：{len(novels_rank_list)}\n')
        for i, novel in enumerate(novels_rank_list):
            f.write(f'{i + 1}.{novel[0]}提名{novel[1]}次\n')

    # 打印前50
    for i, novel in enumerate(novels_rank_list):
        if i > rank - 1:
            break
        name = novel[0]
        num = novel[1]
        print(f'{i + 1}.{name}提名{num}次')
