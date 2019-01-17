# 对插入排序进行性能优化
import random
import timeit
import bisect
from collections import deque, defaultdict, Counter
# random_list = [random.randint(0,100) for i in range(30)]

# 计时器
def min_time(name, number=10, repeat=50):
    '''
    对目标函数执行时间进行计时，默认跑50遍（repeat=50），每遍跑10次（number=10）,取50遍中用时最短者
    '''
    t = timeit.repeat(name, globals=globals(), number=number, repeat=repeat)
    mix_time = min(t)
    print(name+"耗时：{0}".format(mix_time))
    return mix_time

def charu(): # 耗时 0.06143649999285117
    '''插入排序最初版'''
    ran_list = [96, 14, 86, 13, 91, 94, 10, 50, 86, 76, 57, 11, 26, 15, 20, 45, 15, 
    81, 88, 41, 41, 87, 22, 44, 29, 11, 27, 75, 56, 38]*10
    for i in range(1, len(ran_list)):
        for y in range(i, 0, -1):
            if ran_list[y] < ran_list[y-1]:
                ran_list[y], ran_list[y-1] = ran_list[y-1], ran_list[y]

def use_bisect_1(): # 耗时 0.003346951969433576
    '''使用bisect的二分查找算法，代替逐个比较交换，直接将元素插入到适合位置'''
    ran_list = [96, 14, 86, 13, 91, 94, 10, 50, 86, 76, 57, 11, 26, 15, 20, 45, 15, 
    81, 88, 41, 41, 87, 22, 44, 29, 11, 27, 75, 56, 38]*10
    for i in range(1, len(ran_list)):
        index = bisect.bisect(ran_list[:i], ran_list[i])
        if index == i: #如果元素应该插入的位置正好是现在所在的位置，则不必进行删除插入操作
            pass
        else:
            value = ran_list.pop(i) 
            ran_list.insert(index, value)

def use_bisect_2(): # 耗时 0.001062596042174846
    '''对use_bisect_1的优化，不在原列表中操作，在新列表中做插入操作'''
    ran_list = [96, 14, 86, 13, 91, 94, 10, 50, 86, 76, 57, 11, 26, 15, 20, 45, 15, 
    81, 88, 41, 41, 87, 22, 44, 29, 11, 27, 75, 56, 38]*10
    new_list = []
    for i in range(0, len(ran_list)):
        bisect.insort_right(new_list, ran_list[i])   

def use_deque(): # 耗时 0.0018352560000494123
    '''
    与use_biset_2做对比，new_list使用双端队列
    双端队列的优势是在列表左侧插入和删除操作会比顺序表快很多，但劣势也明显，查找元素要比顺序表慢
    本次使用双端队列，并没有发挥出双端队列的优势
    '''
    ran_list = [96, 14, 86, 13, 91, 94, 10, 50, 86, 76, 57, 11, 26, 15, 20, 45, 15, 
    81, 88, 41, 41, 87, 22, 44, 29, 11, 27, 75, 56, 38]*10
    new_list = deque()
    for i in range(0, len(ran_list)):
        index = bisect.bisect(new_list, ran_list[i])
        new_list.insert(index, ran_list[i])
ran_list = [96, 14, 86, 13, 91, 94, 10, 50, 86, 76, 57, 11, 26, 15, 20, 45, 15, 
    81, 88, 41, 41, 87, 22, 44, 29, 11, 27, 75, 56, 38]
s = Counter(ran_list)
print(s)
# min_time(name="charu()")
# min_time(name="use_bisect_1()")
# min_time(name='use_bisect_2()')
# min_time(name='use_deque()')
