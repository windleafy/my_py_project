from ss_chk.ss_chk_fun import verify
import json
import time


# 取ss-free服务器列表
def get_server_url():
    with open('url_list.txt', encoding='utf8') as f:
        s_content = f.read()
    content_list = s_content.split('\n')
    for i in content_list:
        yield i.split()[1:5]


# 验证ss-free服务器列表
def chk_url(urls):
    dict_list = []
    for item in urls:
        url_dict = {
            'server': item[0],
            'server_port': item[1],
            'password': item[3],
            'method': item[2],
            'plugin': '',
            'plugin_opts': '',
            'plugin_args': '',
            'remarks': '',
            'timeout': 5
        }

        dict_list.append(url_dict)

    # print(dict_list)
    count = 1
    l = len(dict_list)
    for i in dict_list:

        print(f'No.{count}, left: {l-count}')
        count += 1
        item = i
        host = item['server']
        port = item['server_port']
        passwd = item['password']
        method = item['method']

        status = verify(host, port, passwd, method, 1080)
        e_time = time.time()
        if status:
            print(item)
            yield item
        print(f'used time:{e_time - star_time}')
        print('\n')

    # 待处理为有效server
    return dict_list


# 刷新客户端配置文件
def refresh_client_json():
    # 读取gui客户端配置文件
    file = 'gui-config.json'
    with open(file, encoding='utf8') as f:
        c_content = json.load(f)
    # print(c_content['configs'])
    print('ss gui client 配置文件读取完毕')

    # 客户端文件刷新
    c_content['configs'] = s_info_list['config']
    print('url信息更新完毕')

    # 写入新的gui客户端配置文件
    file = 'gui-config.json'
    with open(file, 'w', encoding='utf8') as f:
        json.dump(c_content, f)
    print('ss gui client 配置文件重写完毕')


if __name__ == '__main__':
    star_time = time.time()
    # 取出全部url
    url = get_server_url()

    # 取出有效的url
    s_info_list = {'config': list(chk_url(url))}
    print('free-ss url获取完毕')

    # 将有效的url存入客户端配置
    refresh_client_json()

    end_time = time.time()
    print(f'used time:{end_time-star_time}')
