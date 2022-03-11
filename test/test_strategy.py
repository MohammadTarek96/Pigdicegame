
import unittest
from pig.core.player import Strategy, LowRiskStrategy, MediumRiskStrategy, HighRiskStrategy

class TestStrategies(unittest.TestCase):

    def test_basic_strategy(self):
        strategy = Strategy()
        strategy.threshold = 70
        
        self.assertTrue(strategy.should_roll(59))
        self.assertTrue(strategy.should_roll(70))
        self.assertFalse(strategy.should_roll(71))

    def test_low_risk_strategy(self):
        
        strategy = LowRiskStrategy()

        self.assertTrue(strategy.should_roll(5))
        self.assertTrue(strategy.should_roll(6))
        self.assertFalse(strategy.should_roll(7))

    def test_medium_risk_strategy(self):
        
        strategy = MediumRiskStrategy()

        self.assertTrue(strategy.should_roll(5))
        self.assertTrue(strategy.should_roll(12))
        self.assertFalse(strategy.should_roll(18))

    def test_high_risk_strategy(self):
        
        strategy = HighRiskStrategy()

        self.assertTrue(strategy.should_roll(5))
        self.assertTrue(strategy.should_roll(18))
        self.assertFalse(strategy.should_roll(20))
