# author: cjsmt
# version: v2
# date: 2021.5.5
# description: 重写交易统计函数

from .salesman import Salesman
from .host import host
from .screen import screen
from .peripherals import peripherals
import pandas as pd
import numpy as np


def transactions(host_sale_num, screen_sale_num, peripherals_sale_num):
    all_host = host()
    all_screen = screen()
    all_peripherals = peripherals()
    salesMan = Salesman(str(np.random.randint(0, 99999)),
                        month_host=all_host,
                        month_screen=all_screen,
                        month_peripherals=all_peripherals)

    resultTyp = []
    if not all_host.isEnough(host_sale_num-1) or host_sale_num <= 0:
        resultTyp.append(1)
    if not all_screen.isEnough(screen_sale_num-1) or screen_sale_num <= 0:
        resultTyp.append(2)
    if not all_peripherals.isEnough(peripherals_sale_num-1) or peripherals_sale_num <= 0:
        resultTyp.append(3)

    if 1 in resultTyp:
        if 2 in resultTyp:
            if 3 in resultTyp:
                result = '主机和显示器和外设销售量不在取值范围内'
            else:
                result = '主机和显示器销售量不在取值范围内'
        elif 3 in resultTyp:
            result = '主机和外设销售量不在取值范围内'
        else:
            result = '主机销售量不在取值范围内'
    elif 2 in resultTyp:
        if 3 in resultTyp:
            result = '显示器和外设销售量不在取值范围内'
        else:
            result = '显示器销售量不在取值范围内'
    elif 3 in resultTyp:
        result = '外设销售量不在取值范围内'
    else:
        salesMan.add_host_sales(host_sale_num-1)
        salesMan.add_screen_sales(screen_sale_num-1)
        salesMan.add_peripherals_sales(peripherals_sale_num-1)
        total_sale = salesMan.add_host_sales(-1)
        commission_rate = salesMan.commission_rate()
        result = '{}|{}'.format(total_sale, total_sale * commission_rate)
    return result


# if __name__ == '__main__':
#     while True:
#         host_num = input('主机销售数量：')
#         screen_num = input('显示器销售数量：')
#         peripherals_num = input('外设销售数量：')
#         result = transactions(host_sale_num=int(host_num),
#                               screen_sale_num=int(screen_num),
#                               peripherals_sale_num=int(peripherals_num))
#         print(result)