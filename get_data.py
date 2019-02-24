import requests
import json

# url = "http://data.rada.gov.ua/open/data/mps-ids.json"
# url ="https://data.gov.ua/api/3/action/package_show?id=470196d3-4e7a-46b0-8c0c-883b74ac65f0"
# url = "https://data.rada.gov.ua/ogd/mps/data/mps-ids.json"
# r = requests.get(url)
#
# data = json.loads(r.text)
#
# # print(data)
# json.dump(data, open("deputaty.json", "w", encoding="utf-8"), ensure_ascii=False, indent=4)

url_budget = "https://data.rada.gov.ua/ogd/zpr/skl8/bills-skl8.json"

budg = requests.get(url_budget)

data_budg = json.loads(budg.text)

print(data_budg)

