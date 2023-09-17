import unittest
import numpy as np
import random
from functions.voronoi import graph_voronoi, generate_data, rent_estimation


class TestCodei(unittest.TestCase):

    def test_rent_estimation(self):
        data=[1,2,3]
        expected_result=[[0.003,0.001],[0.006, 0.002], [0.009, 0.003]]      
        self.assertEqual(rent_estimation(data), expected_result)


if __name__=="main":
    unittest.main()

