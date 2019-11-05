from ss_chk.ss_fun import verify

url = 'url.txt'

with open(url, encoding='utf8') as f:
    url_list = []
    for i in f.readlines():
        item = i.split()
        url_list.append(item[1:5])

print(url_list[0])

dict_list = []
for item in url_list:
    my_dict = {'host': item[0], 'port': item[1], 'pwd': item[3], 'method': item[2]}
    dict_list.append(my_dict)

print(dict_list[0])

for i in dict_list:
    node = i
    status = verify(node['host'], node['port'], node['pwd'], node['method'], 1080)
    print(status)
    if status:
        print(node)
    print('\n')
