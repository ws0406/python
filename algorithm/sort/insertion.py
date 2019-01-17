import timeit
import cProfile
import random
import copy
random_list = [77, 63, 38, 4, 58, 99, 13, 22, 0, 15]
# 依次从列表中第1个元素（63）开始,于该元素前面的元素比较大小后放入合适的位置
# 依次取出列表中第一个到最后一个元素
def get_element():
    for i in range(1, len(random_list)):
        print('拿到第{0}个元素：{1}'.format(i, random_list[i]))
        # todo: 于该元素前面的元素比较大小后放入合适的位置

# 拿到元素所在位置前面的元素
def get_left_element(i):
    for x in range(i, -1, -1): # 倒序遍历
        print('第{0}个元素前面的元素有：{1}'.format(i, random_list[x]))
        # todo: 当前元素与元素前面的元素比较，如果当前元素小就交换位置

# 比较两个元素，如果第一个比第二个小 就交换位置
def check_number(x, z):
    if random_list[x] < random_list[z]:
        random_list[x], random_list[z] = random_list[z], random_list[x]

# 最后将以上方法整合
def charu(ran_list): 
    for i in range(1, len(ran_list)):
        for y in range(i, 0, -1):
            if ran_list[y] < ran_list[y-1]:
                ran_list[y], ran_list[y-1] = ran_list[y-1], ran_list[y]
    print(ran_list)
# print(timeit.repeat('charu()', globals=globals(), repeat=5, number=3))