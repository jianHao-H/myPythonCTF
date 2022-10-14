import requests
import time

url = "http://61.147.171.105:60972"
headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Upgrade-Insecure-Requests': '1',
    'Cookie': 'safedog-flow-item=; PHPSESSID=p196drolb6k8shcopqqmav96c4',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
}
proxy = {
    'http': '127.0.0.1:8080'
}


def logo():
    print('''
             __    __     _       ___               _             
            / / /\ \ \___| |__   / __\ __ __ _  ___| | _____ _ __ 
            \ \/  \/ / _ \ '_ \ / / | '__/ _` |/ __| |/ / _ \ '__|
             \  /\  /  __/ |_) / /__| | | (_| | (__|   <  __/ |   
              \/  \/ \___|_.__/\____/_|  \__,_|\___|_|\_\___|_|   
                                                      
          welcome to my webcracker, I will scan the web for you to win the commpetiton!
          You can set the dictionary by youself or use the default one 
          There are some pages i have found:

        ''')


def scanner():
    for paths in open('CTFdir.txt', encoding='utf-8'):
        paths = paths.replace('\n', '')
        urls = url + paths

        try:
            res = requests.get(urls, headers=headers)
            code = res.status_code
            lengths = res.headers.get('Content-Length')

            if code == 200 or code == 404:
                print(urls + "status:" + str(code) + "  " + "lenghts:" + lengths)

        except Exception as err:
            print(err)


if __name__ == "__main__":
    logo()
    scanner()

