# author: cjsmt
# version: v2
# date: 2021.5.5
# description: 重写交易统计函数

class peripherals:
    def __init__(self):
        self.price = 45
        self.total_quantity = 90
        self.spare_quantity = 90

    def sellOne(self):
        assert self.isEnough(1), 'NOT ENOUGH.'
        self.spare_quantity -= 1

    def sellFor(self, num):
        assert self.isEnough(num), 'NOT ENOUGH.'
        self.spare_quantity -= num

    def isEnough(self, num):
        return True if self.spare_quantity - num >= 0 else False
