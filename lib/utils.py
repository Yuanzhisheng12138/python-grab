import os, requests
from lxml import etree


def set_header(referer):
    headers = {
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        # 'Referer': '{}'.format(set_referer(referer)),
    }
    return headers


# def set_referer(src):
#     ref = src[25:-4].split('/')
#     if src[-5:-4] == 1:
#         return 'http://www.mm131.com/xinggan/' + ref[0] + '.html'
#     return 'http://www.mm131.com/xinggan/' + ref[0] + '_' + ref[1] + '.html'


# def getmmdir(folder, default=2400):
#     if os.path.exists(folder) and len(os.listdir(folder)) > 0:
#         return int(max(os.listdir(folder)))
#     else:
#         return default


def getnew(default=4600):
    try:
        url = 'http://www.mm131.com/xinggan/'
        content = etree.HTML(requests.get(url).text)
        href = content.xpath('//dl[@class="list-left public-box"]//dd[1]/a/@href')[0]
        newid = href[-9:-5]
        return int(newid)
    except Exception as e:
        return default
