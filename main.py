import time, os
from aio import Aio_mm
from thread import Thread_mm

def start(begin, end):
    start_time = time.time()
    if os.name == 'nt':
        app = Thread_mm()
        app.go_start(begin, end)
    else:
        app = Aio_mm()
        app.go_start(begin, end)
    end_time = time.time()
    print('爬取任务已完成,消耗时间:', end_time - start_time)


if __name__ == '__main__':
    # config={
    # 	'mm_folder':'mm131/',
    # 	'each_limit':60
    # }
    # folder='picture/'
    # finished,newid=getmmdir(folder),getnew()
    sta, end = map(int, input('输入mm起始编号和结束编号 以空格隔开:').split(' '))
    start(sta, end)
