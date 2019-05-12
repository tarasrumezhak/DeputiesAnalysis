from Deputy import Deputy
from unittest import TestCase

class TestDeputy(TestCase):
    """Test Deputy class"""
    def setUp(self):
        self.Deputy = Deputy("Тимошенко Юлія Володимирівна")
        self.Deputy.set_salary(2000000)
        self.Deputy.set_projects((90, 13))
        self.Deputy.set_present((74, 23))
        self.Deputy.set_orgs(8)
        self.Deputy.set_coef()

    def test_salary(self):
        """Test salary"""
        self.assertEqual(self.Deputy.salary, 2000000)

    def test_projects(self):
        """Test projects"""
        self.assertEqual(self.Deputy.projects, 90)
        self.assertEqual(self.Deputy.approved_projects, 13)


    def test_present(self):
        """Test presence and absence"""
        self.assertEqual(self.Deputy.present, 74)
        self.assertEqual(self.Deputy.absent, 23)

    def test_orgs(self):
        """Test organizations and committees"""
        self.assertEqual(self.Deputy.orgs, 8)

    def test_coef(self):
        """Test coefficient"""
        self.assertEqual(self.Deputy.coef, 0.76)

    def test_str(self):
        """Test text representation"""
        text = "Депутат Тимошенко Юлія Володимирівна, отримав з бюджету 2000000 грн.," \
               " бере участь у 8 комітетах та організаціях, на засіданнях був присутнім 74 раз" \
               " та відсутнім 23 раз, законопроектів - 90 (схвалених 13), КОЕФІЦІЄНТ = 0.76"
        self.assertEqual(str(self.Deputy), text)

    def test_csv(self):
        """Test csv like format representation"""
        text = "Тимошенко Юлія Володимирівна, 2000000, 8, 74, 23, 90, 13, 0.76"
        self.assertEqual(self.Deputy.csv_format(), text)