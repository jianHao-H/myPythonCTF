import requests
import re

s = requests.Session()
url = 'http://114.67.175.224:11115/'  # 把网址定义给url参数
r = s.get(url)  # 以get的方式，去访问
r.encoding = 'utf-8'  # 可有可无吧，定义编码形式为utf-8，一些题是必须，加一个以防万一
a = r.text  # 把那个页面定义给a
print(a)
n = eval(re.findall(r'\d(.*?)=', a)[0])  # 利用re正则，把算式匹配出来
print(n)
o = s.post(url, data={'value': n})  # 提交结果
print(o.text)  # 输出返回结果