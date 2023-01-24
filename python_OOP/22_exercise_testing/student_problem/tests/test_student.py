from unittest import TestCase

from student import Student


class StudentTests(TestCase):
    def setUp(self) -> None:
        self.student = Student("Test")

    def test_init_if_works_properly_with_none_courses(self):
        student = Student("Test")
        self.assertEqual("Test", student.name)
        self.assertEqual({}, student.courses)

    def test_enroll_if_no_such_course_there_with_no_notes(self):
        actual_result = self.student.enroll("Test course", "test note", "N")

        self.assertEqual({"Test course": []}, self.student.courses)
        self.assertEqual("Course has been added.", actual_result)

    def test_enroll_if_no_such_course_there_with_with_y_course_note(self):
        actual_result = self.student.enroll("Test course", "test note", "Y")

        self.assertEqual({"Test course": "test note"}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", actual_result)

    def test_enroll_if_no_such_course_there_with_with_empty_string_course_note(self):
        actual_result = self.student.enroll("Test course", "test note", "")

        self.assertEqual({"Test course": "test note"}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", actual_result)

    def test_enroll_if_such_course_already_there(self):
        self.student.enroll("Test course", ["test_note"])
        actual_result = self.student.enroll("Test course", ["new_test_note", "another_new_test_note"], "")

        self.assertEqual({"Test course": ["test_note", "new_test_note", "another_new_test_note"]}, self.student.courses)
        self.assertEqual("Course already added. Notes have been updated.", actual_result)

    def test_to_add_notes_if_course_not_found_raise(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Test course", ["test note", "another_test_note"])

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_to_add_notes_if_course_found(self):
        self.student.enroll("Test course", ["test_notes"])

        actual_result = self.student.add_notes("Test course", "more_test_notes")

        self.assertEqual({"Test course": ["test_notes", "more_test_notes"]}, self.student.courses)
        self.assertEqual("Notes have been updated", actual_result)

    def test_to_leave_course_if_course_not_found(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Test course")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_to_leave_course_if_course_found(self):
        self.student.enroll("Test course", ["test_notes"])

        actual_result = self.student.leave_course("Test course")

        self.assertEqual({}, self.student.courses)
        self.assertEqual("Course has been removed", actual_result)