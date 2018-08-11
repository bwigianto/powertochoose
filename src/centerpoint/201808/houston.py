from plan import *

plan = Plan(tdu_base=5.47, tdu_per_kwh=0.038711)

def infinite_energy_smart_apartment_12(x):
  return plan \
    .with_base_charge(34) \
    .with_tier(lower=0, upper=500, rate=0) \
    .with_tier(lower=501, rate=.2) \
    .tdu_charges_included() \
    .calculate(x)

def discount_power_economy_12(x):
  return plan \
    .with_base_charge(15.50) \
    .with_tier(lower=0, upper=500, rate=0.0017) \
    .with_tier(lower=501, upper=1000, rate=0.1317) \
    .with_tier(lower=1001, rate=0.1232) \
    .calculate(x)

def pennywise_power_wise_buy_conserve_saver_plus_12(x):
  return plan \
    .with_tier(upper=500, rate=0.033) \
    .with_tier(lower=501, upper=1000, rate=0) \
    .with_tier(lower=1001, rate=0.199) \
    .calculate(x)

def gexa_energy_right_choice_basic_12(x):
  return plan \
    .with_base_charge(41.50) \
    .with_tier(lower=0, upper=700, rate=0) \
    .with_tier(lower=701, rate=0.1390) \
    .calculate(x)

def windrose_energy_saver(x):
  return plan \
    .with_fixed_rate(0.047) \
    .calculate(x)

def think_energy_think_simple_6(x):
  return plan \
    .with_fixed_rate(0.047) \
    .calculate(x)

def infuse_keep_it_simple_savings_12(x):
  return plan \
    .with_tier(lower=0, upper=1000, base=49) \
    .with_tier(lower=1001, rate=.114, base=139) \
    .tdu_charges_included() \
    .calculate(x)

def gexa_choice_lite_9(x):
  return plan \
    .with_fixed_rate(0.0686) \
    .with_credit(lower=0, credit=10) \
    .calculate(x)

def express_fast_lane_12(x):
  return plan \
    .with_mutually_exclusive_tier(lower=0, upper=500, rate=.155) \
    .with_mutually_exclusive_tier(lower=501, upper=1000, base=50) \
    .with_mutually_exclusive_tier(lower=1001, rate=.139) \
    .calculate(x)

def constellation_tx_tier(x):
  return plan \
    .with_tier(lower=0, upper=500, cumulative_base=51) \
    .with_tier(lower=501, upper=1000) \
    .with_tier(lower=1001, upper=1500, cumulative_base=129) \
    .with_tier(lower=1501, upper=2000) \
    .with_tier(lower=2001, rate=0.119) \
    .tdu_charges_included() \
    .calculate(x)

def volterra_shine_on_12(x):
  return plan \
    .with_fixed_rate(.05199) \
    .calculate(x)

def discount_power_easy_24(x):
  return plan \
    .with_base_charge(20) \
    .with_tier(upper=1000, rate=.0102) \
    .with_tier(lower=1001, rate=.1797) \
    .calculate(x)

def green_mountain_conserve_12(x):
  return plan \
    .with_base_charge(20) \
    .with_tier(upper=1000, rate=.012318) \
    .with_tier(lower=1001, rate=.117788) \
    .calculate(x)

def discount_premier_12(x):
  return plan \
    .with_fixed_rate(.1444) \
    .with_credit(lower=500, credit=35) \
    .tdu_charges_included() \
    .calculate(x)
