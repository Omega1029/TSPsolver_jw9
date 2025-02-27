import unittest

from tsp_solver_jtw.algorithms.Asearch import a_star_search
from tsp_solver_jtw.algorithms.hill_climbing import hill_climbing
from tsp_solver_jtw.algorithms.random_search import random_search
from tsp_solver_jtw.algorithms.simulated_annealing import simulated_annealing
from tsp_solver_jtw.utils import generate_random_cities


class TestTSPRandomSearch(unittest.TestCase):
    def setUp(self):
        self.cities = generate_random_cities(6)

    def test_random_search(self):
        route, distance = random_search(self.cities)
        self.assertIsInstance(route, list)
        self.assertIsInstance(distance, float)

    def test_hill_climbing(self):
        route, distance = hill_climbing(self.cities)
        self.assertIsInstance(route, list)
        self.assertIsInstance(distance, float)

    def test_simulated_annealing(self):
        route, distance = simulated_annealing(self.cities)
        self.assertIsInstance(route, list)
        self.assertIsInstance(distance, float)

    def test_a_star_search(self):
        route, distance = a_star_search(self.cities)
        self.assertIsInstance(route, list)
        self.assertIsInstance(distance, float)


if __name__ == "__main__":
    unittest.main()