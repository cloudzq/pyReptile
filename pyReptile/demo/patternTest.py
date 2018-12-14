from pattern import dataPattern
from spider import request

url = 'https://movie.douban.com/subject/3168101/comments'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}
r = request.get(url, headers=headers)
title = dataPattern.get_data(r['text'], '#content > h1')
print(title)
selector = 'div.comment > p > span'
comment = dataPattern.get_data(r['text'], selector, parser='html5lib')
print(len(comment))
