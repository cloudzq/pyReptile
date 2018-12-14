from spider import request
# GET
url = 'http://httpbin.org/get'
# url = ['http://httpbin.org/get']
params = {
    'pyReptile': 'spiderGet'
}
cookies = {
    'pyReptile': 'spiderCookies'
}
r = request.get(url, params=params, cookies=cookies)
print(r['text'])
# print(r[0]['text'])

# POST
url = 'http://httpbin.org/post'
# url = ['http://httpbin.org/post']
data = {
    'pyReptile': 'spiderPost'
}
cookies = {
    'pyReptile': 'spiderCookies'
}
r = request.post(url, data=data, cookies=cookies)
print(r['text'])
# print(r[0]['text'])
