import xlrd
import time
from .computerService.main import transactions


# 业务逻辑层
# 每道题的解决方法，包含不同版本

########### 第一道题 ###########
# 三角形问题程序设计1
def HandleTriangle1(edges):
    edge1 = edges.get('edge1')
    edge2 = edges.get('edge2')
    edge3 = edges.get('edge3')
    triType = ""
    if float(edge1) <= 0 and float(edge2) <= 0 and float(edge3) <= 0:
        triType = 'a取值不在范围内'
        return triType
    if float(edge1) <= 0 and float(edge2) <= 0:
        triType = 'a取值不在范围内'
        return triType
    if float(edge2) <= 0 and float(edge3) <= 0:
        triType = 'b取值不在范围内'
        return triType
    if float(edge1) <= 0 and float(edge3) <= 0:
        triType = 'a取值不在范围内'
        return triType
    if float(edge1) <= 0:
        triType = 'a取值不在范围内'
        return triType
    if float(edge2) <= 0:
        triType = 'b取值不在范围内'
        return triType
    if float(edge3) <= 0:
        triType = 'c取值不在范围内'
        return triType
    edge = [float(edge1), float(edge2), float(edge3)]
    edge.sort()
    if edge[0] + edge[1] <= edge[2]:
        triType = "非三角形"
        print(0)
    elif edge[0] == edge[1] and edge[1] == edge[2]:
        triType = "等边三角形"
        print(1)
    elif edge[0] == edge[1] or edge[1] == edge[2]:
        triType = "等腰三角形"
        print(2)
    else:
        triType = "不等边三角形"
        print(3)
    return triType


# 三角形问题最终设计
def HandleTriangle(edges):
    edge1 = edges.get('edge1')
    edge2 = edges.get('edge2')
    edge3 = edges.get('edge3')
    triType = ""
    if float(edge1) <= 0 and float(edge2) <= 0 and float(edge3) <= 0:
        triType = 'a和b和c取值不在范围内'
        return triType
    if float(edge1) <= 0 and float(edge2) <= 0:
        triType = 'a和b取值不在范围内'
        return triType
    if float(edge2) <= 0 and float(edge3) <= 0:
        triType = 'b和c取值不在范围内'
        return triType
    if float(edge1) <= 0 and float(edge3) <= 0:
        triType = 'a和c取值不在范围内'
        return triType
    if float(edge1) <= 0:
        triType = 'a取值不在范围内'
        return triType
    if float(edge2) <= 0:
        triType = 'b取值不在范围内'
        return triType
    if float(edge3) <= 0:
        triType = 'c取值不在范围内'
        return triType
    edge = [float(edge1), float(edge2), float(edge3)]
    edge.sort()
    if edge[0] + edge[1] <= edge[2]:
        triType = "非三角形"
        print(0)
    elif edge[0] == edge[1] and edge[1] == edge[2]:
        triType = "等边三角形"
        print(1)
    elif edge[0] == edge[1] or edge[1] == edge[2]:
        triType = "等腰三角形"
        print(2)
    else:
        triType = "不等边三角形"
        print(3)
    return triType


# 三角形问题用例测试
def TestTriangle(info):
    version = info.get('version')
    method = info.get('method')
    if method == "boundary":
        # 打开文件
        workBook = xlrd.open_workbook('xls/P1_Boundary.xls')
    elif method == "equivalence":
        workBook = xlrd.open_workbook('xls/P1_Equivalence.xls')
    else:
        return False
    sheet1_content = workBook.sheet_by_index(0)  # sheet索引从0开始
    reList = [0 for x in range(0, sheet1_content.nrows)]
    count = 0
    while count < sheet1_content.nrows:
        edge1 = sheet1_content.row_values(count)[0]
        edge2 = sheet1_content.row_values(count)[1]
        edge3 = sheet1_content.row_values(count)[2]
        expectedOutput = sheet1_content.row_values(count)[3]
        edges = {
            "edge1": edge1,
            "edge2": edge2,
            "edge3": edge3
        }
        if version == "v1":
            actualOutput = HandleTriangle1(edges)
        elif version == "v2":
            actualOutput = HandleTriangle(edges)
        else:
            actualOutput = "暂无此版本！"
        if expectedOutput == actualOutput:
            correctness = "正确"
        else:
            correctness = "错误"
        row = {
            "testCaseID": count + 1,
            "edge1": edge1,
            "edge2": edge2,
            "edge3": edge3,
            "expectedOutput": expectedOutput,
            "actualOutput": actualOutput,
            "correctness": correctness,
            "testTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        }
        reList[count] = row
        count = count + 1
    return reList


########### 第三道题 ###########
# 电脑销售问题程序设计1
def HandleComputer(nums):
    mainframe = nums.get('mainframe')
    peripheral = nums.get('peripheral')
    monitor = nums.get('monitor')
    info = transactions(host_sale_num=int(mainframe),
                        screen_sale_num=int(monitor),
                        peripherals_sale_num=int(peripheral))
    return info


# 电脑销售问题用例测试
def TestComputer(info):
    version = info.get('version')
    method = info.get('method')
    if method == "boundary":
        # 打开文件
        workBook = xlrd.open_workbook('xls/P3_Boundary.xls')
    elif method == "equivalence":
        workBook = xlrd.open_workbook('xls/P3_Equivalence.xls')
    else:
        return False
    sheet1_content = workBook.sheet_by_index(0)  # sheet索引从0开始
    reList = [0 for x in range(0, sheet1_content.nrows)]
    count = 0
    while count < sheet1_content.nrows:
        mainframe = sheet1_content.row_values(count)[0]
        monitor = sheet1_content.row_values(count)[1]
        peripheral = sheet1_content.row_values(count)[2]
        expectedOutput = sheet1_content.row_values(count)[3]
        nums = {
            "mainframe": mainframe,
            "peripheral": peripheral,
            "monitor": monitor
        }
        if version == "v1":
            actualOutput = HandleComputer(nums)
        else:
            actualOutput = "暂无此版本!"
        if expectedOutput == actualOutput:
            correctness = "正确"
        else:
            correctness = "错误"
        row = {
            "testCaseID": count + 1,
            "mainframe": mainframe,
            "monitor": monitor,
            "peripheral": peripheral,
            "expectedOutput": expectedOutput,
            "actualOutput": actualOutput,
            "correctness": correctness,
            "testTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        }
        reList[count] = row
        count = count + 1
    return reList


########### 第六道题 ###########
# 电信收费问题程序设计1
def HandleTelephone1(inputs):
    time = float(inputs.get('minutes'))
    num = float(inputs.get('times'))
    if time <= 0 or time > 31 * 24 * 60:
        if num < 0 or num > 12:
            return '通话分钟和未按时缴费次数不在取值范围内'
        return '通话分钟不在取值范围内'
    if num < 0 or num > 12:
        return '未按时缴费次数不在取值范围内'
    if 0 < time <= 60 and num <= 1:
        discRate = 0.01
    elif 60 < time <= 120 and num <= 2:
        discRate = 0.015
    elif 120 < time <= 180 and num <= 3:
        discRate = 0.02
    elif 180 < time <= 300 and num <= 3:
        discRate = 0.025
    elif time > 300 and num <= 6:
        discRate = 0.03
    else:
        discRate = 0
    return 25 + (1 - discRate) * 0.15 * time


def HandleTelephone(inputs):
    time = float(inputs.get('minutes'))
    num = float(inputs.get('times'))
    if time <= 0 or time > 31 * 24 * 60:
        if num < 0 or num > 12:
            return '通话分钟和未按时缴费次数不在取值范围内'
        return '通话分钟不在取值范围内'
    if num < 0 or num > 12:
        return '未按时缴费次数不在取值范围内'
    if 0 < time <= 60 and num <= 1:
        discRate = 0.01
    elif 60 < time <= 120 and num <= 2:
        discRate = 0.015
    elif 120 < time <= 180 and num <= 3:
        discRate = 0.02
    elif 180 < time <= 300 and num <= 3:
        discRate = 0.025
    elif time > 300 and num <= 6:
        discRate = 0.03
    else:
        discRate = 0
    return format(25 + (1 - discRate) * 0.15 * time, '.1f')


# 电信收费问题用例测试
def TestTelephone(info):
    version = info.get('version')
    method = info.get('method')
    if method == "boundary":
        # 打开文件
        workBook = xlrd.open_workbook('xls/P6_Boundary.xls')
    elif method == "equivalence":
        workBook = xlrd.open_workbook('xls/P6_Equivalence.xls')
    elif method == "decision-table":
        workBook = xlrd.open_workbook('xls/P6_Decision-table.xls')
    else:
        return False
    sheet1_content = workBook.sheet_by_index(0)  # sheet索引从0开始
    reList = [0 for x in range(0, sheet1_content.nrows)]
    count = 0
    while count < sheet1_content.nrows:
        minutes = sheet1_content.row_values(count)[0]
        times = sheet1_content.row_values(count)[1]
        expectedOutput = sheet1_content.row_values(count)[2]
        inputs = {
            "minutes": minutes,
            "times": times,
        }
        if version == "v1":
            actualOutput = HandleTelephone1(inputs)
        elif version == "v2":
            actualOutput = HandleTelephone(inputs)
        else:
            actualOutput = "暂无此版本!"
        if expectedOutput == actualOutput:
            correctness = "正确"
        else:
            correctness = "错误"
        row = {
            "testCaseID": count + 1,
            "minutes": minutes,
            "times": times,
            "expectedOutput": expectedOutput,
            "actualOutput": actualOutput,
            "correctness": correctness,
            "testTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        }
        reList[count] = row
        count = count + 1
    return reList


########### 第八道题 ###########
# 万年历问题程序设计1
def HandleCalendar1(dates):
    year = float(dates.get('year'))
    month = float(dates.get('month'))
    day = float(dates.get('day'))
    if not 1900 <= year <= 2100:
        if not 1 <= month <= 12 and not 1 <= day <= 31:
            result = '年月日不在取值范围内'
        else:
            result = '年份不在取值范围内'
    elif not 1 <= month <= 12:
        result = '月份不在取值范围内'
    elif month in [4, 6, 9, 11] and day >= 31:
        result = '日份不在取值范围内'
    elif month == 2 and year % 4 == 0 and year % 100 != 0 and day > 29:
        result = '日份不在取值范围内'
    elif not (month == 2 and year % 4 == 0 and year % 100 != 0) and day > 28:
        result = '日份不在取值范围内'
    else:
        if month in [1, 3, 5, 7, 8, 10] and day == 31:
            result = '{}-{}-{}'.format(year, month + 1, 1)
        elif month in [4, 6, 9, 11] and day == 30:
            result = '{}-{}-{}'.format(year, month + 1, 1)
        elif month == 2 and year % 4 == 0 and year % 100 != 0 and day == 29:
            result = '{}-{}-{}'.format(year, month + 1, 1)
        elif month == 2 and day == 28:
            result = '{}-{}-{}'.format(year, month + 1, 1)
        elif month == 12 and day == 21:
            result = '{}-{}-{}'.format(year + 1, 1, 1)
        else:
            result = '{}-{}-{}'.format(year, month, day + 1)
    return result


# 万年历问题程序设计
def HandleCalendar(dates):
    year = int(dates.get('year'))
    month = int(dates.get('month'))
    day = int(dates.get('day'))
    if not 1900 <= year <= 2100:
        if not 1 <= month <= 12 and not 1 <= day <= 31:
            result = '年月日不在取值范围内'
        else:
            result = '年份不在取值范围内'
    elif not 1 <= month <= 12:
        result = '月份不在取值范围内'
    elif month in [4, 6, 9, 11] and day >= 31:
        result = '日份不在取值范围内'
    elif month == 2 and year % 4 == 0 and year % 100 != 0 and day > 29:
        result = '日份不在取值范围内'
    elif not (month == 2 and year % 4 == 0 and year % 100 != 0) and day > 28:
        result = '日份不在取值范围内'
    else:
        if month in [1, 3, 5, 7, 8, 10] and day == 31:
            result = '{}-{}-{}'.format(year, month + 1, 1)
        elif month in [4, 6, 9, 11] and day == 30:
            result = '{}-{}-{}'.format(year, month + 1, 1)
        elif month == 2 and year % 4 == 0 and year % 100 != 0 and day == 29:
            result = '{}-{}-{}'.format(year, month + 1, 1)
        elif month == 2 and day == 28:
            result = '{}-{}-{}'.format(year, month + 1, 1)
        elif month == 12 and day == 21:
            result = '{}-{}-{}'.format(year + 1, 1, 1)
        else:
            result = '{}-{}-{}'.format(year, month, day + 1)
    return result


# 万年历问题用例测试
def TestCalendar(info):
    version = info.get('version')
    method = info.get('method')
    if method == "boundary":
        # 打开文件
        workBook = xlrd.open_workbook('xls/P8_Boundary.xls')
    elif method == "equivalence":
        workBook = xlrd.open_workbook('xls/P8_Equivalence.xls')
    else:
        return False
    sheet1_content = workBook.sheet_by_index(0)  # sheet索引从0开始
    reList = [0 for x in range(0, sheet1_content.nrows)]
    count = 0
    while count < sheet1_content.nrows:
        year = sheet1_content.row_values(count)[0]
        month = sheet1_content.row_values(count)[1]
        day = sheet1_content.row_values(count)[2]
        expectedOutput = sheet1_content.row_values(count)[3]
        dates = {
            "year": year,
            "month": month,
            "day": day
        }
        if version == "v1":
            actualOutput = HandleCalendar1(dates)
        elif version == "v2":
            actualOutput = HandleCalendar(dates)
        else:
            actualOutput = "暂无此版本!"
        if expectedOutput == actualOutput:
            correctness = "正确"
        else:
            correctness = "错误"
        row = {
            "testCaseID": count + 1,
            "year": year,
            "month": month,
            "day": day,
            "expectedOutput": expectedOutput,
            "actualOutput": actualOutput,
            "correctness": correctness,
            "testTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        }
        reList[count] = row
        count = count + 1
    return reList


# ATM问题程序设计
def HandleATM(sequence):
    seq = sequence.get('event')
    # print(seq)
    state = "暂无此版本"
    return state


# ATM问题用例测试
def TestATM(info):
    version = info.get('version')
    method = info.get('method')
    if method == "boundary":
        # 打开文件
        workBook = xlrd.open_workbook('xls/P9.xls')
        # print(workBook)
    else:
        return False
    sheet1_content = workBook.sheet_by_index(0)  # sheet索引从0开始
    reList = [0 for x in range(0, sheet1_content.nrows)]
    count = 0
    while count < sheet1_content.nrows:
        sequence = sheet1_content.row_values(count)[0]
        print(sequence)
        expectedOutput = sheet1_content.row_values(count)[1]
        events = {
            "event": sequence
        }
        if version == "v1":
            actualOutput = HandleATM(events)
        else:
            actualOutput = "暂无此版本!"
        if expectedOutput == actualOutput:
            correctness = "正确"
        else:
            correctness = "错误"
        row = {
            "testCaseID": count + 1,
            "sequence": sequence,
            "expectedOutput": expectedOutput,
            "actualOutput": actualOutput,
            "correctness": correctness,
            "testTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        }
        reList[count] = row
        count = count + 1
    return reList
