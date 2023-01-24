class StudentTaxes:
    def __init__(self, name, semester_tax, avg_grade):
        self.name = name
        self.semester_tax = semester_tax
        self.avg_grade = avg_grade

    def get_discount(self):
        if self.avg_grade > 5:
            return self.semester_tax * 0.4


