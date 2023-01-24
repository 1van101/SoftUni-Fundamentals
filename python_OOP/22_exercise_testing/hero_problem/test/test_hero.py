from unittest import TestCase

from hero import Hero


class HeroTests(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Test", 10, 100, 50)
        self.enemy = Hero("TestTest", 10, 100, 50)

    def test_constructor(self):
        hero = Hero("Test", 10, 100, 50)
        self.assertEqual("Test", hero.username)
        self.assertEqual(10, hero.level)
        self.assertEqual(100, hero.health)
        self.assertEqual(50, hero.damage)

    def test_if_attacks_himself_raises(self):

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_if_hero_health_is_zero_or_negative_raises(self):
        for health in [0, -1]:
            self.hero.health = health

            with self.assertRaises(Exception) as ex:
                self.hero.battle(self.enemy)

            self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_if_enemy_health_is_zero_or_negative_raises(self):
        for health in [0, -1]:
            self.enemy.health = health

            with self.assertRaises(Exception) as ex:
                self.hero.battle(self.enemy)

            self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ex.exception))

    def test_if_draw_with_both_players_negative_health(self):
        # TODO zero health

        hero_dmg = self.hero.damage * self.hero.level
        enemy_dmg = self.enemy.damage * self.enemy.level

        expected_hero_health = self.hero.health - enemy_dmg
        expected_enemy_health = self.enemy.health - hero_dmg

        actual_result = self.hero.battle(self.enemy)

        self.assertEqual(expected_hero_health, self.hero.health)
        self.assertEqual(expected_enemy_health, self.enemy.health)
        self.assertEqual("Draw", actual_result)

    def test_if_enemy_health_negative(self):
        # TODO zero health

        self.hero.health = 600
        expected_hero_damage = self.hero.damage + 5
        expected_hero_health = self.hero.health - (self.enemy.damage * self.enemy.level) + 5

        actual_result = self.hero.battle(self.enemy)

        self.assertEqual(11, self.hero.level)
        self.assertEqual(expected_hero_health, self.hero.health)
        self.assertEqual(expected_hero_damage, self.hero.damage)
        self.assertEqual("You win", actual_result)

    def test_if_hero_health_negative(self):
        self.enemy.health = 600
        expected_enemy_damage = self.enemy.damage + 5
        expected_enemy_health = self.enemy.health - (self.hero.damage * self.hero.level) + 5

        actual_result = self.hero.battle(self.enemy)

        self.assertEqual(11, self.enemy.level)
        self.assertEqual(expected_enemy_health, self.enemy.health)
        self.assertEqual(expected_enemy_damage, self.enemy.damage)
        self.assertEqual("You lose", actual_result)

    def test_if_returns_string_method_properly(self):
        actual_result = str(self.hero)
        expected_result = "Hero Test: 10 lvl\n" \
                          "Health: 100\n" \
                          "Damage: 50\n"

        self.assertEqual(expected_result, actual_result)
