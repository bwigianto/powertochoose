import unittest
from plan import *

class TestPlan(unittest.TestCase):

    def test_includes_tdu_charges(self):
        charge = Plan(tdu_base=5, tdu_per_kwh=3) \
            .calculate(10)
        self.assertEqual(charge, 5 + 3 * 10)

    def test_can_exclude_tdu_charges(self):
        charge = Plan(tdu_base=5, tdu_per_kwh=3) \
            .tdu_charges_included() \
            .calculate(10)
        self.assertEqual(charge, 0)

    def test_can_add_1_tier(self):
        charge = Plan(tdu_base=5, tdu_per_kwh=3) \
            .with_tier(lower=0, upper=500, rate=2) \
            .calculate(10)
        self.assertEqual(charge, 5 + (3 + 2) * 10)

    def test_can_add_2_tiers(self):
        charge = Plan(tdu_base=5, tdu_per_kwh=3) \
            .with_tier(lower=0, upper=500, rate=2) \
            .with_tier(lower=501, rate=5) \
            .calculate(750)
        self.assertEqual(charge, 5 + (3 + 2) * 500 + (3 + 5) * (750 - 500))

    def test_can_add_rep_base(self):
        charge = Plan(tdu_base=5, tdu_per_kwh=3) \
            .with_base_charge(6) \
            .with_tier(lower=0, upper=500, rate=2) \
            .with_tier(lower=501, rate=5) \
            .calculate(750)
        self.assertEqual(charge, 6 + 5 + (3 + 2) * 500 + (3 + 5) * (750 - 500))

    def test_ignores_unused_tiers(self):
        charge = Plan(tdu_base=5, tdu_per_kwh=3) \
            .with_tier(lower=0, upper=500, rate=2) \
            .with_tier(lower=501, upper=1000, rate=3) \
            .calculate(10)
        self.assertEqual(charge, 5 + (3 + 2) * 10)

    def test_can_add_fixed_rate(self):
        charge = Plan(tdu_base=5, tdu_per_kwh=3) \
            .with_fixed_rate(2) \
            .calculate(40)
        self.assertEqual(charge, 5 + (3 + 2) * 40)

    def test_can_add_tiered_base_charge(self):
        charge = Plan(tdu_base=5, tdu_per_kwh=3) \
            .with_tier(lower=0, upper=50, base=7) \
            .calculate(40)
        self.assertEqual(charge, 5 + 7 + 3 * 40)

    def test_tiered_block_charges_dont_accumulate(self):
        charge = Plan(tdu_base=5, tdu_per_kwh=3) \
            .with_tier(lower=0, upper=20, base=7) \
            .with_tier(lower=21, upper=50, base=8) \
            .calculate(40)
        self.assertEqual(charge, 5 + 8 + 3 * 40)

    def test_tiered_block_charges_can_accumulate(self):
        charge = Plan(tdu_base=5, tdu_per_kwh=3) \
            .with_tier(lower=0, upper=20, cumulative_base=7) \
            .with_tier(lower=21, upper=50, cumulative_base=8) \
            .calculate(40)
        self.assertEqual(charge, 5 + 8 + 7 + 3 * 40)

    def test_can_add_usage_credit(self):
        charge = Plan(tdu_base=5, tdu_per_kwh=3) \
            .with_credit(lower=0, credit=10) \
            .calculate(40)
        self.assertEqual(charge, 5 + 3 * 40 - 10)

    def test_can_add_mutually_exclusive_tier(self):
        charge = Plan(tdu_base=5, tdu_per_kwh=3) \
            .with_mutually_exclusive_tier(lower=0, upper=10, rate=3) \
            .with_mutually_exclusive_tier(lower=11, upper=20, rate=4) \
            .calculate(15)
        self.assertEqual(charge, 5 + (3 + 4) * 15)

if __name__ == '__main__':
    unittest.main()
