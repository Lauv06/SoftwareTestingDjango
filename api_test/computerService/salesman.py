# author: cjsmt
# version: v2
# date: 2021.5.5
# description: 重写交易统计函数

class Salesman:
    def __init__(self, ID, month_host, month_screen, month_peripherals):
        self.id = ID
        self._host = month_host
        self._screen = month_screen
        self._peripherals = month_peripherals

        self.sales_num = {
            'host': 1,
            'screen': 1,
            'peripherals': 1
        }
        self._host.sellOne()
        self._screen.sellOne()
        self._peripherals.sellOne()
        self.total_sales = 0

    def add_host_sales(self, num):
        assert isinstance(num, int), 'WRONG NUMBER TO SALE.'
        if num == -1:
            return self.calculate_total()
        else:
            self._host.sellFor(num)
            self.sales_num['host'] += num

    def add_screen_sales(self, num):
        assert isinstance(num, int), 'WRONG NUMBER TO SALE.'
        self._screen.sellFor(num)
        self.sales_num['screen'] += num

    def add_peripherals_sales(self, num):
        assert isinstance(num, int), 'WRONG NUMBER TO SALE.'
        self._peripherals.sellFor(num)
        self.sales_num['peripherals'] += num

    def calculate_total(self):
        self.total_sales = self._host.price * self.sales_num['host'] + \
                           self._screen.price * self.sales_num['screen'] + \
                           self._peripherals.price * self.sales_num['peripherals']
        return self.total_sales

    def commission_rate(self):
        if self.total_sales <= 1000:
            return 0.1
        elif self.total_sales <= 1800:
            return 0.15
        else:
            return 0.2
