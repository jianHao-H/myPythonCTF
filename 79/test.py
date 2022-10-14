import requests
import json

# 创建任务ID
task_new_url = 'http://127.0.0.1:8775/task/new'
resq = requests.get(task_new_url)
task_id = resq.json()['taskid']
print(task_id)

#设置任务ID的配置信息
data = {
    'url': 'http://123.57.226.43/sqli-labs/Less-2/?id=1'
}

headers = {
    'Content-Type': 'application/json'
}

task_set_url = 'http://127.0.0.1:8775/option/' + task_id + '/set'
# print(task_set_url)
task_set_resq = requests.post(task_set_url, data=json.dumps(data), headers=headers)
# print(task_set_resq.content.decode('utf-8'))

# 启动对应ID的扫描任务
task_start_url = 'http://127.0.0.1:8775/scan/' + task_id + '/start'
task_start_resq = requests.post(task_start_url, data=json.dumps(data), headers=headers)
# print(task_start_resq.content.decode('utf-8'))

# 获取对应ID的扫描状态
task_status_url = 'http://127.0.0.1:8775/scan/' + task_id + '/status'
task_status_resq = requests.get(task_status_url)
print(task_status_resq.content.decode('utf-8'))