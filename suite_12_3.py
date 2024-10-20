# suite_12_3.py
import unittest
from tests_12_3 import RunnerTest, TournamentTest

def run_tests():
    # Создаем TestSuite
    suite = unittest.TestSuite()

    # Создаем экземпляр TestLoader
    loader = unittest.TestLoader()

    # Загружаем тесты из RunnerTest и TournamentTest
    suite.addTest(loader.loadTestsFromTestCase(RunnerTest))
    suite.addTest(loader.loadTestsFromTestCase(TournamentTest))

    # Запускаем тесты с TextTestRunner
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == "__main__":
    run_tests()
