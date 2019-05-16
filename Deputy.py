class Deputy:
    """Deputy representation class"""
    def __init__(self, fullname):
        """Initialize the object"""
        self.fullname = fullname
        self.salary = 0
        self.orgs = 0
        self.present = 0
        self.absent = 0
        self.projects = 0
        self.approved_projects = 0
        self.coef = 0

    def set_salary(self, amount):
        """Set the salary to particular deputy"""
        self.salary = amount

    def set_orgs(self, count):
        """Set organizations and committees to particular deputy"""
        self.orgs = count

    def set_present(self, pres):
        """Set presence and absence to particular deputy"""
        self.present = pres[0]
        self.absent = pres[1]

    def set_projects(self, pros):
        """Set projects and approved projects to particular deputy"""
        self.projects = pros[0]
        self.approved_projects = pros[1]

    def set_coef(self):
        pres_coef = self.present * (self.present / (self.absent + self.present))
        self.coef = round(((self.orgs * 10 + pres_coef + self.projects + self.approved_projects * 100) /
                           self.salary) * 1000, 2)

    def __str__(self):
        """Comfortable string representation of the object"""
        text = "Депутат {}, отримав з бюджету {} грн., бере участь у {} " \
               "комітетах та організаціях, на засіданнях був присутнім {} " \
               "раз та відсутнім {} раз, законопроектів - {} (схвалених {}), КОЕФІЦІЄНТ = {}".format(self.fullname,
                    self.salary, self.orgs, self.present, self.absent, self.projects, self.approved_projects, self.coef)
        return text

    def csv_format(self):
        """Comfortable csv representation of the object"""
        text = "{}, {}, {}, {}, {}, {}, {}, {}".format(self.fullname, self.salary, self.orgs,
                                                   self.present, self.absent, self.projects,
                                                   self.approved_projects, self.coef)
        return text

    def visualize(self):
        """Visualize the statistics about deputy"""
        pass
