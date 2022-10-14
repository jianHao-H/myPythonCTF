#域名反查IP功能
import socket
import os
import sys


def getip(url):
    ip=socket.gethostbyname(url)
    print("ip地址：" + ip)

#信息收集脚本

# 一、 识别目标是否存在CDN
#采用nslookup 执行结果进行IP解析数目判断
#利用python执行系统命令

#这个命令不能把结果取出来进行解析，只能print看看而已
# cdn_data=os.system('nslookup www.xiaodi8.com')
# print(cdn_data)

#这里就是判断结果中存在多少个点，大于x个点则为存在cdn
def cdn_judge(url):
    exe_sentence = "nslookup " + url
    cdn_data=os.popen(exe_sentence)
    cdn_datas=cdn_data.read()
    cdn_datas=cdn_datas.count('.')
    if cdn_datas > 8:
        print("存在CDN")
    else:
        print("不存在CDN")


#二、端口扫描
#1.原生自写socket协议tcp，udp扫描

def portScan(url):
    ports= [80,8080,445]
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    for port in ports:
        result = server.connect_ex((url,port))
        if result == 0:
            print(port, ':open')
        else:
            print(port, ':close')


#2.调用第三方工具nmap等等进行扫描
#3.调用系统工具脚本执行


#三、whois查询
import whois
def get_whois(url):
    data=whois.whois(url)
    print(data)

# 四、子域名查询
# 1.利用字典记载爆破进行查询
import time
import socket
def childDomain_check(url):
    url=url.replace('www', '')

    for childDomain in open('./dic/childDomain.txt'):
        childDomain=childDomain.replace('\n', '')
        child_url= childDomain + url
        try:
            ip = socket.gethostbyname(child_url)
            print(child_url + '->' + ip)
            time.sleep(0.1)
        except Exception as e:
            print('error!')
            # pass


# 2.利用bing或第三方接口进行查询


if __name__ == '__main__':
    # check=sys.argv[1]
    # url=sys.argv[2]

    # if check == "all":
        # getip(url)
        # cdn_judge(url)
        # portScan(url)
        # get_whois(url)
        # childDomain_check(url)
    childDomain_check("www.xiaodi8.com")