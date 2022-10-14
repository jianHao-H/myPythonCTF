import nmap

def nmapscan():
    nm = nmap.PortScanner()
    try:
        data=nm.scan(hosts='192.168.76.0/24', arguments='-T4 -F')
        print(nm.all_hosts())
        print(nm.csv())
        print(data)
    except Exception as err:
        print("error")

if __name__ == '__main__':
    nmapscan()

