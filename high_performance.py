import multiprocessing
import time
from threading import Thread
from multiprocessing import Process
import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def test(num):
    print('start test,num:{0}'.format(num))
    time.sleep(3)
    print(num)
    print('end test,num:{0}'.format(num))
    return num
    
def multi_pool():
    '''进程池'''
    a = multiprocessing.Pool()
    for i in range(3):
        res = a.apply_async(test, (i,))
    print('start multiprocessing')
    a.close()
    a.join()
    
def asyncio_test():
    '''协程'''
    loop = asyncio.get_event_loop()
    # excuter = ThreadPoolExecutor(max_workers=3)  
    excuter = ProcessPoolExecutor(max_workers=10)
    loop.run_until_complete(asyncio.wait([loop.run_in_executor(excuter, test, i) for i in range(10)]))

class TestTread(Thread):
    
    def __init__(self):
        super().__init__()
        
    def run(self):
        res = test(2)

class TestMultiprocessing(Process):
    
    def __init__(self):
        super().__init__()
        
    def run(self):
        res = test(2)

if __name__ == "__main__":
    asyncio_test()
    