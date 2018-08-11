class Plan():

    def __init__(self, **kwargs):
        self.tdu_base = kwargs.get('tdu_base', 0)
        self.tdu_per_kwh = kwargs.get('tdu_per_kwh', 0)
        self.rep_base = kwargs.get('rep_base', 0)
        self.rep_fixed_rate = kwargs.get('rep_fixed_rate', 0)
        self.tiers = kwargs.get('tiers', [])
        self.mutually_exclusive_tiers = kwargs.get('mutually_exclusive_tiers', [])
        self.credits = kwargs.get('credits', [])

    def tdu_charges_included(self):
        return Plan(tdu_base=0,
                tdu_per_kwh=0,
                rep_base=self.rep_base,
                rep_fixed_rate=self.rep_fixed_rate,
                tiers=self.tiers,
                mutually_exclusive_tiers=self.mutually_exclusive_tiers,
                credits=self.credits)

    def with_tier(self, **kwargs):
        return Plan(tdu_base=self.tdu_base,
                tdu_per_kwh=self.tdu_per_kwh,
                rep_base=self.rep_base,
                rep_fixed_rate=self.rep_fixed_rate,
                tiers=self.tiers + [kwargs],
                mutually_exclusive_tiers=self.mutually_exclusive_tiers,
                credits=self.credits)

    def with_base_charge(self, rep_base):
        return Plan(tdu_base=self.tdu_base,
                tdu_per_kwh=self.tdu_per_kwh,
                rep_base=rep_base,
                rep_fixed_rate=self.rep_fixed_rate,
                tiers=self.tiers,
                mutually_exclusive_tiers=self.mutually_exclusive_tiers,
                credits=self.credits)

    def with_fixed_rate(self, rep_fixed_rate):
        return Plan(tdu_base=self.tdu_base,
                tdu_per_kwh=self.tdu_per_kwh,
                rep_base=self.rep_base,
                rep_fixed_rate=rep_fixed_rate,
                tiers=self.tiers,
                mutually_exclusive_tiers=self.mutually_exclusive_tiers,
                credits=self.credits)

    def with_credit(self, **kwargs):
        return Plan(tdu_base=self.tdu_base,
                tdu_per_kwh=self.tdu_per_kwh,
                rep_base=self.rep_base,
                rep_fixed_rate=self.rep_fixed_rate,
                tiers=self.tiers,
                mutually_exclusive_tiers=self.mutually_exclusive_tiers,
                credits=self.credits + [kwargs])

    def with_mutually_exclusive_tier(self, **kwargs):
        return Plan(tdu_base=self.tdu_base,
                tdu_per_kwh=self.tdu_per_kwh,
                rep_base=self.rep_base,
                rep_fixed_rate=self.rep_fixed_rate,
                tiers=self.tiers,
                mutually_exclusive_tiers=self.mutually_exclusive_tiers + [kwargs],
                credits=self.credits)

    def calculate(self, x):
        tot = self.tdu_base + self.rep_base
        if not self.tiers and not self.mutually_exclusive_tiers:
            tot += (self.tdu_per_kwh + self.rep_fixed_rate) * x
        last_upper = 0

        for kwargs in self.tiers:
            lower = kwargs.get('lower', 0)
            upper = kwargs.get('upper', float("inf"))
            r = kwargs.get('rate', 0)
            tier_base = kwargs.get('base', 0)
            cumulative_tier_base = kwargs.get('cumulative_base', 0)
            if x <= upper:
                tot += cumulative_tier_base + tier_base + (self.tdu_per_kwh + r) * (x - last_upper)
                break
            else:
                tot += cumulative_tier_base + (self.tdu_per_kwh + r) * (upper - last_upper)
            last_upper = upper

        for kwargs in self.mutually_exclusive_tiers:
            lower = kwargs.get('lower', 0)
            upper = kwargs.get('upper', float("inf"))
            r = kwargs.get('rate', 0)
            tier_base = kwargs.get('base', 0)
            if lower <= x and x <= upper:
                tot += tier_base + (self.tdu_per_kwh + r) * x

        for kwargs in self.credits:
            lower = kwargs.get('lower', 0)
            upper = kwargs.get('upper', float("inf"))
            credit = kwargs.get('credit', 0)
            if lower <= x and x <= upper:
                tot -= credit
        return tot


