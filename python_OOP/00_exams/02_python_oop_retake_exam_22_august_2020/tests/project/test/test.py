from unittest import TestCase, main

from project.student_report_card import StudentReportCard


class StudentReportCardTests(TestCase):
    def setUp(self) -> None:
        self.student_report_card = StudentReportCard("StudentName", 12)

    def test_init(self):
        student_report_card = StudentReportCard("StudentName", 1)
        self.assertEqual("StudentName", student_report_card.student_name)
        self.assertEqual(12, self.student_report_card.school_year)
        self.assertEqual({}, self.student_report_card.grades_by_subject)

    def test_invalid_student_name_setter_raises(self):
        with self.assertRaises(ValueError) as ve:
            StudentReportCard("", 12)

        self.assertEqual("Student Name cannot be an empty string!", str(ve.exception))

    def test_invalid_school_year_raises(self):
        with self.assertRaises(ValueError) as ve:
            StudentReportCard("Name", 13)

        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_to_add_grade(self):
        self.student_report_card.add_grade("Math", 5.50)
        self.student_report_card.add_grade("Math", 4.00)

        self.assertEqual({"Math": [5.50, 4.00]}, self.student_report_card.grades_by_subject)
        self.assertEqual([5.50, 4.00], self.student_report_card.grades_by_subject["Math"])

        self.student_report_card.add_grade("Chemistry", 4.00)

        self.assertEqual({"Math": [5.50, 4.00], "Chemistry": [4.00]}, self.student_report_card.grades_by_subject)
        self.assertEqual([4.00], self.student_report_card.grades_by_subject["Chemistry"])

    def test_average_grades_by_subject(self):
        self.student_report_card.add_grade("Math", 5.50)
        self.student_report_card.add_grade("Math", 4.00)
        self.student_report_card.add_grade("Chemistry", 4.00)

        actual_result = self.student_report_card.average_grade_by_subject()
        expected_result = "Math: 4.75\nChemistry: 4.00"

        self.assertEqual(expected_result, actual_result)
        self.assertEqual([5.50, 4.00], self.student_report_card.grades_by_subject["Math"])
        self.assertEqual([4.00], self.student_report_card.grades_by_subject["Chemistry"])

    def test_average_grades_by_subject_with_no_subjects_added(self):
        actual_result = self.student_report_card.average_grade_by_subject()

        self.assertEqual("", actual_result)

    def test_average_grade_all_subjects(self):
        self.student_report_card.add_grade("Math", 5.50)
        self.student_report_card.add_grade("Math", 4.00)
        self.student_report_card.add_grade("Chemistry", 4.00)

        actual_result = self.student_report_card.average_grade_for_all_subjects()

        self.assertEqual("Average Grade: 4.50", actual_result)

    # def test_average_grade_all_subjects_with_no_subjects_raises(self):
    #     with self.assertRaises(ZeroDivisionError) as zde:
    #         self.student_report_card.average_grade_for_all_subjects()
    #
    #     self.assertEqual("division by zero", str(zde.exception))

    def test_repr_method(self):
        self.student_report_card.add_grade("Math", 5.50)
        self.student_report_card.add_grade("Math", 4.00)
        self.student_report_card.add_grade("Chemistry", 4.00)

        actual_result = repr(self.student_report_card)
        expected_result = "Name: StudentName\n" \
                          "Year: 12\n" \
                          "----------\n" \
                          "Math: 4.75\nChemistry: 4.00\n" \
                          "----------\n" \
                          "Average Grade: 4.50"

        self.assertEqual(expected_result, actual_result)

    # def test_repr_method_no_data_raises(self):
    #     with self.assertRaises(ZeroDivisionError) as zde:
    #         repr(self.student_report_card)
    #
    #     self.assertEqual("division by zero", str(zde.exception))


if __name__ == "__main__":
    main()
