"""
假设有一个中央调度机，有n个相同的任务需要调度到m台服务器上去执行，由于每台服务器的配置不一样，因此服务器
 执行一个任务所花费的时间也不同。现在假设第i个服务器执行 一个任务需要的时间为t[i].
 例如：有2个执行机a,b,执行一个任务分别需要7min,10min,有6个任务待调度。如果平分这6个任务，即a,b各3个
 任务，则最短需要30min执行完所有。如果a分4个任务 ，b分2个任务，则最短28min执行完。 请设计调度算法，使得所有任务完成所需要的时间最短。
 输入m台服务器，每台机器处理一个任务的时间为t[i],完成n个任务，输出n个任务在m台服务器的分布。
"""


def estimate_process_time(t, m, n):
    i = 0
    total = 0
    time = [0 for i in range(len(t))]
    t_min = 0
    while i < n:
        tmp = total + t[0]
        for j in range(len(t)):
            if time[j] + t[j] < tmp:
                tmp = time[j] + t[j]
                t_min = j
        time[t_min] += t[t_min]
        total = tmp
        i += 1
    return total


t = [1, 10]
m = 2
n = 23

print(estimate_process_time(t, m, n))
