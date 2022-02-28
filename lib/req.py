import requests, os
from .utils import set_header


class Request(object):

    def __init__(self):
        self.folder = 'picture/'

    def save(self, pic, i):
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)
        with open(self.folder + '%s.jpg' % i, 'wb') as pp:
            pp.write(pic)
        return 'saved!'

    def get(self, url, i):
        # conn = aiohttp.TCPConnector(verify_ssl=False)  # 防止ssl报错
        proxies = {'http': 'http://127.0.0.1:8001', 'https': 'http://127.0.0.1:8001'}
        response = requests.get(url, headers=set_header(url), proxies=proxies)
        pic = response.content
        if response.status_code == 404:
            return '404 not found!'
        elif response.status_code == 200:
            return self.save(pic, i)

    def requestUrl(self, url):
        url = url.replace("\n", "")
        print('正在请求-->', url)
        arr = url.split("/")
        if isinstance(arr, list):
            i = arr[len(arr) - 1]
            result = self.get(url, i)
            print('获取到结果:-->', url, '-->', result)
        else:
            print('未获取到结果')