from sales_person import SalesPerson


class SalesForce:

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        with open(file_name) as f:
            for line in f:
                line = line.strip()
                line = line.split(",")
                employee_id = int(line[0])
                name = line[1]
                sales = []
                for sale in line[2:]:
                    sales.append(float(sale))
                self.sales_people.append(SalesPerson(employee_id, name, sales))

    def quota_report(self, quota):
        report = []
        for person in self.sales_people:
            if person.total_sales() >= quota:
                report.append([person.get_id(), person.get_name(), person.total_sales(), True])
            else:
                report.append([person.get_id(), person.get_name(), person.total_sales(), False])
        return report

    def top_seller(self):
        top_sellers = []
        top_sales = 0
        for person in self.sales_people:
            if person.total_sales() > top_sales:
                top_sales = person.total_sales()
                top_sellers = [person]
            elif person.total_sales() == top_sales:
                top_sellers.append(person)
        return top_sellers

    def individual_sales(self, employee_id):
        for person in self.sales_people:
            if person.get_id() == employee_id:
                return person
        return None

    def get_sale_frequencies(self):
        frequencies = {}
        for person in self.sales_people:
            for sale in person.get_sales():
                if sale in frequencies:
                    frequencies[sale] += 1
                else:
                    frequencies[sale] = 1
        return frequencies
