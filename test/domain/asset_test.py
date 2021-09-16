import unittest
from src.domain.asset import Asset


class AssetTest(unittest.TestCase):

    def test_should_be_create_correctly(self):
        asset = Asset("TAEE11", 20, 1000)
        self.assertEquals(20, asset.shares())
        self.assertEqual(1000, asset.value())
        self.assertEqual(50, asset.mean_price())