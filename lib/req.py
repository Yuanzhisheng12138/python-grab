import requests, os
from .utils import set_header


class Request(object):

    def __init__(self):
        self.url_name_dict = {}
        self.folder = 'picture/'
        with open('./url.txt', 'r') as file:
            urls = file.readlines()
        with open('./name.txt', 'r') as file2:
            names = file2.readlines()
        for index in range(len(urls)):
            url = urls[index]
            url = url.replace("\n", "")
            arr = url.split("/")
            if isinstance(arr, list):
                i = arr[len(arr) - 1]
                self.url_name_dict[i] = names[index]

    def save(self, pic, i):
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)
        # with open(self.folder + '%s.jpg' % i, 'wb') as pp:
        with open(self.folder + self.url_name_dict[i] + '.jpg', 'wb') as pp:
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