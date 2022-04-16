class SalesPerson:
    def __init__(self, employee_id, name,):
        self.sales = []
        self.employee_id = employee_id
        self.name = name

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales = sale + self.sales
        return self.sales

    def total_sales(self, total_sales):
        total_sales = total_sales + self.enter_sale
        return total_sales

    def get_sales(self, total_sales):
        return [total_sales]

    def met_quota(self, total_sales, quota):
        if total_sales >= quota:
            return True
        else:
            return False

    def compare_to(self, other):
        if other > self:
            return -1
        elif self > other:
            return 1
        elif self == other:
            return 0

    def __str__(self):
        return "{}-{}: {}".format(self.employee_id, self.name, self.total_sales())