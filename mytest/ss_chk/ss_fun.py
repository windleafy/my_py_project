import os
import json
import time
import socket
import httplib2


def verify(host, port, passwd, method, local_port):
    ip = socket.getaddrinfo(host, None)[0][4][0]
    v6 = ':' in ip
    config = {'server': host, 'server_port': port,
              'password': passwd, 'method': method,
              'local_address': '127.0.0.1',
              'local_port': local_port, 'timeout': 60}
    cfile = '/etc/shadowsocks-libev/local_port.json'
    with open(cfile, 'w') as f:
        json.dump(config, f)

    os.system('systemctl restart shadowsocks-libev-local@local_port.service')
    print('start server')

    time.sleep(1)
    h = httplib2.Http(proxy_info=httplib2.ProxyInfo(2, '127.0.0.1', local_port), timeout=60)
    status = False
    try:
        if v6:
            r, c = h.request('http://v6.ipv6-test.com/api/myip.php')
        else:
            r, c = h.request('http://httpbin.org/ip')
        status = r['status'] == '200'
    except Exception as e:
        print(e)
    os.system('systemctl stop shadowsocks-libev-local@%s.service' % local_port)
    os.remove(cfile)
    return status
