# tests_12_3.py
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False  # Управляющий атрибут для заморозки тестов

    def freeze_control(method):
        def wrapper(self, *args, **kwargs):
            if not self.is_frozen:
                return method(self, *args, **kwargs)
            else:
                self.skipTest('Тесты в этом кейсе заморожены')
        return wrapper

    @freeze_control
    def test_challenge(self):
        self.assertEqual(1 + 1, 2)

    @freeze_control
    def test_run(self):
        self.assertTrue(True)

    @freeze_control
    def test_walk(self):
        self.assertFalse(False)


class TournamentTest(unittest.TestCase):
    is_frozen = True  # Управляющий атрибут для заморозки тестов

    def freeze_control(method):
        def wrapper(self, *args, **kwargs):
            if not self.is_frozen:
                return method(self, *args, **kwargs)
            else:
                self.skipTest('Тесты в этом кейсе заморожены')
        return wrapper

    @freeze_control
    def test_first_tournament(self):
        self.assertEqual(2 * 2, 4)

    @freeze_control
    def test_second_tournament(self):
        self.assertEqual(3 + 2, 5)

    @freeze_control
    def test_third_tournament(self):
        self.assertEqual(4 - 1, 3)
