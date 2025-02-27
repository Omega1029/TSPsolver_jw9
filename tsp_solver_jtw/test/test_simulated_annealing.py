import unittest

from tsp_solver_jtw.algorithms.simulated_annealing import simulated_annealing
from tsp_solver_jtw.utils import generate_random_cities


class TestTSPSimulatedAnnealing(unittest.TestCase):
    def setUp(self):
        self.cities = generate_random_cities(6)


    def test_simulated_annealing(self):
        route, distance = simulated_annealing(self.cities)
        self.assertIsInstance(route, list)
        self.assertIsInstance(distance, float)



if __name__ == "__main__":
    unittest.main()