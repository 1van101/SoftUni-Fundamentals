from unittest import TestCase

from project.team import Team


class TeamTests(TestCase):
    def setUp(self) -> None:
        self.team = Team("Test")

    def test_setter_for_name_with_invalid_data_raises(self):
        with self.assertRaises(ValueError) as ve:
            Team("Tes7")

        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_to_add_member(self):
        result = self.team.add_member(Ivan=30, Stoyan=20, Gosho=40)

        self.assertEqual({"Ivan": 30, "Stoyan": 20, "Gosho": 40}, self.team.members)
        self.assertEqual("Successfully added: Ivan, Stoyan, Gosho", result)

        second_result = self.team.add_member(Ivan=50, Todor=25)
        self.assertEqual({"Ivan": 30, "Stoyan": 20, "Gosho": 40, "Todor": 25}, self.team.members)
        self.assertEqual("Successfully added: Todor", second_result)

    def test_ro_remove_member_if_member_exists(self):
        self.team.add_member(Ivan=30, Stoyan=20, Gosho=40)

        result = self.team.remove_member("Ivan")

        self.assertEqual({"Stoyan": 20, "Gosho": 40}, self.team.members)
        self.assertEqual("Member Ivan removed", result)

    def test_ro_remove_member_if_member_doesnt_exist(self):
        self.team.add_member(Ivan=30, Stoyan=20, Gosho=40)

        result = self.team.remove_member("Todor")

        self.assertEqual({"Ivan": 30, "Stoyan": 20, "Gosho": 40}, self.team.members)
        self.assertEqual("Member with name Todor does not exist", result)

    def test_gt_method(self):
        other_team = Team("Other")

        self.team.add_member(Ivan=30, Stoyan=20, Gosho=40)
        other_team.add_member(Ivan=30, Stoyan=20)

        result = self.team > other_team
        self.assertEqual(True, result)

        other_team.add_member(Gosho=40, Todor=50)

        new_result = self.team > other_team

        self.assertEqual(False, new_result)

    def test_gt_method_with_equal_members(self):

        other_team = Team("Other")
        self.team.add_member(Ivan=30, Stoyan=20)
        other_team.add_member(Ivan=30, Stoyan=20)

        result = self.team > other_team
        self.assertEqual(False, result)

    def test_len_method(self):
        self.team.add_member(Ivan=30, Stoyan=20, Gosho=40)

        self.assertEqual(3, len(self.team))

    def test_add_method(self):
        other_team = Team("Other")

        self.team.add_member(Ivan=30, Stoyan=20, Gosho=40)
        other_team.add_member(Ivan=30, Petar=20)

        new_team = self.team.__add__(other_team)

        self.assertEqual("TestOther", new_team.name)
        self.assertEqual({"Ivan": 30, "Stoyan": 20, "Gosho": 40,"Petar": 20}, new_team.members)

    def test_string_method(self):
        self.team.add_member(Ivan=30, Stoyan=20, Gosho=40, Aleks=40)

        expected_result = "Team name: Test" \
                          "\nMember: Aleks - 40-years old" \
                          "\nMember: Gosho - 40-years old" \
                          "\nMember: Ivan - 30-years old" \
                          "\nMember: Stoyan - 20-years old"

        self.assertEqual(expected_result, str(self.team))