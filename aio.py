from aiomultiprocess import Pool
import aiohttp, asyncio, time, os


class Aio_mm(object):

    def __init__(self):
        self.mm_folder = 'picture/'
        self.each_limit = 60

    async def async_get(self, url):
        await asyncio.sleep(2)
        conn = aiohttp.TCPConnector(verify_ssl=False)  # 防止ssl报错
        proxies = {'http': "socks5://127.0.0.1:8080",
                   'https': "socks5://127.0.0.1:8080"}
        # url = "https://img.yituyu.com/gallery/1111/02_teu5QjDK.jpg"

        if not os.path.exists(self.mm_folder):
            os.makedirs(self.mm_folder)
        url = url.replace("\n", "")
        print('Waiting for', url)
        async with aiohttp.request('GET', url, connector=conn, proxy="http://127.0.0.1:8001") as resp:
            if resp.status != 200:
                return ''
            pic = await resp.read()
        # async with aiohttp.ClientSession() as session:
        #     print('Waiting for', url)
        #     response = await session.get(url)
        #     pic = await response.read()
        # if response.status == 404:
        #     return '404 not found!'
        print('Get res from', url, 'Result:', resp.status, 'ok!')

        arr = url.split("/")
        if isinstance(arr,list):
            i = arr[len(arr) - 1]
            with open(self.mm_folder + '%s.jpg' % i, 'wb') as pp:
                pp.write(pic)

    async def makeurl(self, sta, end, limit):
        with open('./url.txt', 'r') as file:
            urls = file.readlines()
        # urls = ['http://img1.mm131.me/pic/' + str(i) + '/' + str(j) + '.jpg' for i in range(sta, end + 1) for j in
        #         range(1, limit)]
            urls = urls[sta-1:end-1]
            return await Pool().map(self.async_get, urls)

    def go_start(self, begin, end):
        task = asyncio.ensure_future(self.makeurl(begin, end, self.each_limit))
        loop = asyncio.get_event_loop()
        loop.run_until_complete(task)


if __name__ == '__main__':
    sta, end = map(int, input('输入mm起始编号和结束编号 以空格隔开:').split(' '))
    app = Aio_mm()
    start_time = time.time()
    app.go_start(sta, end)
    end_time = time.time()
    print('爬取任务已完成,消耗时间:', end_time - start_time)
