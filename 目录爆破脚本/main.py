import requests

headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Upgrade-Insecure-Requests': '1',
    'Cookie':  'safedog-flow-item=; PHPSESSID=p196drolb6k8shcopqqmav96c4',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
}

for paths in open('./php.txt', encoding='utf-8'):
    url = 'http://192.168.0.14/'
    paths = paths.replace('\n', '')
    urls = url + paths
    proxy = {
        'http': '127.0.0.1:7777'
    }
    try:
        code = requests.get(urls, headers=headers, proxies=proxy).status_code
        #time.sleep(3)
        print(urls + '|' + str(code))
        if code == 200 or code == 403:
            print(urls + '|' + str(code))
    except Exception as err:
        print('conneting error')
        # time.sleep(3)

