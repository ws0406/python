import random
import timeit

def min_time(name, number=10, repeat=50, *args):
    '''
    对目标函数执行时间进行计时，默认跑50遍（repeat=50），每遍跑10次（number=10）,取50遍中用时最短者
    '''
    t = timeit.repeat(name, globals=globals(), number=number, repeat=repeat)
    mix_time = min(t)
    print(name+"耗时：{0}".format(mix_time))
    return mix_time

alist = [random.randint(0, 100) for i in range(30)]

def quick_sort(alist=alist):
    left_list = []
    right_list = []
    # 以列表中的第0个元素为基准，将比基准数小的放入left_list中，将比基准数大或等于的放入right_list中
    for i in alist[1:]:
        right_list.append(i) if i > alist[0] else left_list.append(i)
    if len(left_list) > 1:      #如果left_list列表元素大于等于2将比基准数小的列表(left_list)排序
        left_list = quick_sort(left_list)
    if len(right_list) > 1:         #如果ringt_list列表元素大于等于2将比基准数小的列表(right_list)排序
        right_list = quick_sort(right_list)
    # 以上操作后，比基准数小的列表和比基准数大的列表都是有序列表了,排序后的列表是：left_list + 基准数 + right_list
    left_list.extend([alist[0]])
    if right_list:
        left_list.extend(right_list)
    return left_list

ss = min_time(name = 'quick_sort')