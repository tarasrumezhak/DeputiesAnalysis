class Deputy:
    """Deputy representation class"""
    def __init__(self, fullname):
        """Initialize the object"""
        self.fullname = fullname
        self.salary = None
        self.orgs = None
        self.present = None
        self.absent = None
        self.projects = None
        self.approved_projects = None
        self.coef = None

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

    def __str__(self):
        """Comfortable string representation of the object"""
        text = "Депутат {}, отримав з бюджету {} грн., бере участь у {} " \
               "комітетах та організаціях, на засіданнях був присутнім {} " \
               "раз та відсутнім {} раз, законопроектів - {} (схвалених {})".format(self.fullname,
                    self.salary, self.orgs, self.present, self.absent, self.projects, self.approved_projects)
        return text

    def visualize(self):
        """Visualize the statistics about deputy"""
        pass
