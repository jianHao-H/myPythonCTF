import time
import requests
import json

# 批量扫描
#设置任务ID的配置信息

def sqlmapaip(url):
    # 设置任务ID的配置信息
    data = {
        'url':url
    }

    headers = {
        'Content-Type': 'application/json'
    }

    # 创建任务ID
    task_new_url = 'http://127.0.0.1:8775/task/new'
    resq = requests.get(task_new_url)
    task_id = resq.json()['taskid']
    print(resq.content.decode('utf-8'))
    if 'success' in resq.content.decode('utf-8'):
        print('sqlmapApi task create success!')

        task_set_url = 'http://127.0.0.1:8775/option/' + task_id + '/set'
        # print(task_set_url)
        task_set_resq = requests.post(task_set_url, data=json.dumps(data), headers=headers)
        # print(task_set_resq.content.decode('utf-8'))
        if 'success' in task_set_resq.content.decode('utf-8'):
            print('sqlmapapi task set success！')
            # 启动对应ID的扫描任务
            task_start_url = 'http://127.0.0.1:8775/scan/' + task_id + '/start'
            task_start_resq = requests.post(task_start_url, data=json.dumps(data), headers=headers)
            # print(task_start_resq.content.decode('utf-8'))
            if 'success' in task_start_resq.content.decode('utf-8'):
                print('sqlmapapi task start success！')
                # 获取对应ID的扫描状态
                while 1:
                    task_status_url = 'http://127.0.0.1:8775/scan/' + task_id + '/status'
                    task_status_resq = requests.get(task_status_url)
                    #print(task_status_resq.content.decode('utf-8'))
                    if 'running' in  task_status_resq.content.decode('utf-8'):
                        print('sqlmapapi task scan running... ')
                        pass
                    else:
                        task_data_url = 'http://127.0.0.1:8775/scan/' + task_id + '/data'
                        task_data_resq = requests.get(task_data_url)
                        print(task_data_resq.content.decode('utf-8'))
                        break
                time.sleep(3)

if __name__ == '__main__':
    print("scanurl checking ok...")
    for url in open('url.txt'):
        url = url.replace('\n', '')
    sqlmapaip(url)
