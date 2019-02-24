import random
alist = [random.randint(0, 100) for i in range(30)]
def quick_sort(alist):
    left_list = []
    right_list = []
    # 以列表中的第0个元素为基准，将比基准数小的放入left_list中，将比基准数大或等于的放入right_list中
    for i in alist[1:]:
        right_list.append(i) if i > alist[0] else left_list.append(i)
    #如果left_list列表元素大于等于2将比基准数小的列表(left_list)排序
    if len(left_list) > 1:
        left_list = quick_sort(left_list)
    #如果ringt_list列表元素大于等于2将比基准数小的列表(right_list)排序
    if len(right_list) > 1:
        right_list = quick_sort(right_list)
    # 以上操作后，比基准数小的列表和比基准数大的列表都是有序列表了
    # 排序后的列表是：left_list + 基准数 + right_list
    left_list.extend([alist[0]])
    if right_list:
        left_list.extend(right_list)
    return left_list

print(quick_sort(alist))