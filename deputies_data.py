import json
import requests
import pandas as pd
import io


class DeputiesData:
    """Class to represent the information about deputies"""
    def __init__(self):
        self.deputies = {}
        # self.general_data = []
        self.salaries = {}
        self.organizations_and_committees = []
        self.budget_url = None
        self.orgs_url = None
        self.present_url = None
        self.projects_url = None

    def add_salaries(self, fullname, salary):
        """
        Add information about salaries
        :param fullname: str
        :param salary: float
        :return: None
        """
        self.deputies[fullname] = []
        self.deputies[fullname].append(salary)

    def add_orgs(self, fullname, orgs_count):
        """
        Add information about organizations and committees
        :param fullname: str
        :param orgs_count: int
        :return: None
        """
        try:
            self.deputies[fullname].append(orgs_count)
        except:
            self.deputies[fullname] = []
            self.deputies[fullname].append(orgs_count)

    def add_present(self, fullname, present):
        """
        Add information about presence and absence
        :param fullname: str
        :param present: tuple
        :return: None
        """
        try:
            self.deputies[fullname].append(present)
        except:
            self.deputies[fullname] = []
            self.deputies[fullname].append(present)

    def add_projects(self, fullname, projects):
        """
        Add information about projects and approved projects
        :param fullname: str
        :param present: tuple
        :return: None
        """
        try:
            self.deputies[fullname].append(projects)
        except:
            self.deputies[fullname] = []
            self.deputies[fullname].append(projects)

    def set_salaries_url(self, url):
        """
        Set the url to data with salaries
        :param url: str
        :return: None
        """
        self.budget_url = url

    def set_orgs_url(self, url):
        """
        Set the url to data with organizations and committees
        :param url: str
        :return: None
        """
        self.orgs_url = url

    def set_present_url(self, url):
        """
        Set the url to data with presence and absence
        :param url: str
        :return: None
        """
        self.present_url = url

    def set_projects_url(self, url):
        """
        Set the url to data with projects and approved projects
        :param url: str
        :return: None
        """
        self.projects_url = url

    def get_salaries_data(self):
        """
        Get the data with salaries and save it
        :return: None
        """
        budg = requests.get(self.budget_url)
        data_budg = json.loads(budg.text)
        deputies = []
        salaries = []
        for i in data_budg:
            try:
                if "Невідомо" not in data_budg[i]["full_name"]:
                    deputies.append(data_budg[i]["full_name"])
                    salaries.append(float(data_budg[i]["amount"]))
            except:
                pass
        for j in range(len(deputies)):
            self.add_salaries(deputies[j], salaries[j])
        self.salaries = salaries

    def get_orgs_data(self):
        """
        Get the data with organizations and committees and save it
        :return: None
        """
        url_orgs = "https://data.rada.gov.ua/ogd/mps/skl8/mps08-data.json"

        org = requests.get(url_orgs)

        data_orgs = json.loads(org.text)

        ids1 = requests.get(self.orgs_url).content
        data = pd.read_csv(io.StringIO(ids1.decode('utf-8')))
        data = data['mp_id']
        orgs = dict(data.value_counts())
        ids_dict = {}
        for i in data_orgs:
            ids_dict[i["id"]] = i["full_name"]
            try:
                orgs[i["full_name"]] = orgs.pop(i["id"])
            except KeyError:
                pass
        for i, j in orgs.items():
            self.add_orgs(i, j)

    def get_present_data(self):
        """
        Get the data with presence and absence and save it
        :return: None
        """
        pres = requests.get(self.present_url)
        data = json.loads(pres.text)
        for i in data:
            try:
                # print(i["mp_name"], i["present"], i["absent"])
                self.add_present(i["mp_name"], (i["present"], i["absent"]))
            except:
                # print("hello")
                self.add_present(i["mp_name"], None)

    def get_projects_data(self):
        """
        Get the data with projects and approved projects and save it
        :return: None
        """
        pass

    def __len__(self):
        """
        Returns the length of dict
        :return: int
        """
        return len(self.deputies)

    def __str__(self):
        """
        String representation of the object
        :return: str
        """
        return str(self.deputies)

    def sort(self):
        """
        Sort dict by salaries
        :return: list
        """
        return sorted(self.salaries.items(), key=lambda x: x[1])

    def mean(self):
        """
        Returns the mean value of all salaries
        :return: float
        """
        total = 0
        for i in self.salaries.values():
            total += i
        mean = total / len(self.salaries)
        return round(mean, 2)

    def __iter__(self):
        """
        Iterate the object
        :return: iter
        """
        return iter(self.salaries.items())


if __name__ == "__main__":
    sals = DeputiesData()
    sals.set_salaries_url("https://data.rada.gov.ua/ogd/fin/dkaz/fin_transactions_mps_stat.json")
    sals.get_salaries_data()
    sals.set_orgs_url("https://data.rada.gov.ua/ogd/mps/skl8/mp-posts_ids.csv")
    sals.get_orgs_data()
    sals.set_present_url("https://data.rada.gov.ua/ogd/mps/koms/mps-kom_mps-skl8.json")
    sals.get_present_data()
    print(sals)
