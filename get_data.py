import requests
import json
import pygal

url = "http://data.rada.gov.ua/open/data/mps-ids.json"

url_budget = "https://data.rada.gov.ua/ogd/fin/dkaz/fin_transactions_mps_stat.json"

budg = requests.get(url_budget)

data_budg = json.loads(budg.text)

deputies = []
salaries = []
dct = {}
for i in data_budg:
    try:
        if "Невідомо" not in data_budg[i]["full_name"]:
            deputies.append(data_budg[i]["full_name"])
            salaries.append(float(data_budg[i]["amount"]))
            dct[data_budg[i]["full_name"]] = float(data_budg[i]["amount"])
    except:
        pass
print(len(deputies))
print(len(salaries))


# b_chart = pygal.Bar(width=8000)
# b_chart.title = "Зарплати депутатів"
# for j in dct.keys():
#     b_chart.add(j, dct[j])
# b_chart.render_to_file("salaries.svg")
