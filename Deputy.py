import requests
import json

class Deputy:
    def __init__(self, fullname):
        self.fullname = fullname
        self.salary = None
        self.spendings = None
        self.coef = None

    def set_salary(self, amount):
        self.salary = amount

    def __str__(self):
        text = "Депутат {}, має зарплату {} грн.".format(self.fullname, self.salary)
        return text

    def visualize(self):
        pass

class Salaries():
    def __init__(self):
        self.salaries = {}
        self.url = None

    def add(self, fullname, salary):
        self.salaries[fullname] = salary

    def set_url(self, url):
        self.url = url

    def get_data(self):
        budg = requests.get(self.url)
        data_budg = json.loads(budg.text)

        deputies = []
        salaries = []
        # dct = {}
        for i in data_budg:
            try:
                if "Невідомо" not in data_budg[i]["full_name"]:
                    deputies.append(data_budg[i]["full_name"])
                    salaries.append(float(data_budg[i]["amount"]))
                    # dct[data_budg[i]["full_name"]] = float(data_budg[i]["amount"])
            except:
                pass

        for j in range(len(deputies)):
            self.add(deputies[j], salaries[j])

    def __len__(self):
        return len(self.salaries)

    def __str__(self):
        return str(self.salaries)

    def sort(self):
        return sorted(self.salaries.items(), key=lambda x: x[1])

    def mean(self):
        total = 0
        for i in self.salaries.values():
            total += i
        mean = total / len(self.salaries)
        return round(mean, 2)

    def __iter__(self):
        return iter(self.salaries.items())



if __name__ == "__main__":
    sals = Salaries()
    sals.set_url("https://data.rada.gov.ua/ogd/fin/dkaz/fin_transactions_mps_stat.json")
    sals.get_data()
    print(sals)
    print(sals.sort())
    print(sals.mean())
    deps = []
    for dep, sal in sals:
        deputy = Deputy(dep)
        deputy.set_salary(sal)
        deps.append(deputy)
    print(deps)
    print(deps[1])
    for i in deps:
        if "Шевченко" in i.fullname:
            print(i)
            print(i.salary)

