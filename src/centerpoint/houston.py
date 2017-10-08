import sys, json

def discount_power_economy12(x):
  base = 3.25 + 5.47
  if x <= 500:
    return base + (0.83 + 3.57) / 100 * x
  if x <= 1000:
    return base + (0.83 + 3.57) / 100 * 500 + (11.37 + 3.57) / 100 * (x - 500)
  if x > 1001:
    return base + (0.83 + 3.57) / 100 * 500 + (11.37 + 3.57) / 100 * 500 + (10.58 + 3.57) / 100 * (x - 1000)

def gexa_my_choice12(x):
  base = 15.47
  if x <= 1000:
    return base + (0.0021 + 0.0357) * x
  if x <= 1250:
    return base + (0.0021 + 0.0357) * 1000 + (0.49 + 0.0357) * (x - 1000)
  if x <= 2000:
    return base + (0.0021 + 0.0357) * 1000 + (0.49 + 0.0357) * 250 + (0.0001 + 0.0357) * (x - 1250)

def discount_power_easy24(x):
  base = 18.47
  if x <= 1000:
    return base + (0.0013 + 0.0357) * x
  return base + (0.0013 + 0.0357) * 1000 + (0.1357 + 0.0357) * (x - 1000)

def power_express_summer24(x):
  base = 14.25 + 5.47
  if x <= 1000:
    return base + (0.1 + 0.0357) * x
  return base + (0.1 + 0.0357) * 1000 + (0.1364 + 0.0357) * (x - 1000)

def infuse_savings6(x):
  if x <= 1000:
    return 39
  return 99 + (x - 1000) * 0.106

def pioneer_choice24(x):
  return 0.0834 * x

def green_mountain_conserve12(x):
  base = 5.47 + 10
  if x <= 1000:
    return base + (0.018343 + 0.035686) * x
  return base + (0.018343 + 0.035686) * 1000 + (0.093813 + 0.035686) * (x - 1000)

def discount_super_saver(x):
  base = 5.47
  return base + (0.04003 + 0.0357) * x

def pioneer_simple24(x):
  base = 3.25
  return base + (0.0801) * x

def infinite_tremendous(x):
  base = 5.47
  if x <= 500:
    return base + (0.0357 + 0.044311) * x
  if x <= 1000:
    return base + (0.0357 + 0.044311) * 500 + (0.0357 + 0.034311) * (x - 500)
  return (0.094311 + 0.0357) * (x - 1000) + base + (0.0357 + 0.044311) * 500 + (0.0357 + 0.034311) * 500

def reliant_secure(x):
  base = 10.47
  return base + (0.035686 + 0.038) * x

def wise_buy_conserve_saver6(x):
  base = 5.47
  if x <= 500:
    return base + (0.03 + 0.0357) * x
  if x <= 1000:
    return base + (0.03 + 0.0357) * 500 + 0.0357 * (x - 500)
  return base + (0.03 + 0.0357) * 500 + 0.0357 * 500 + (0.0357 + 0.119) * (x - 1000)

def pennywise_conserve_saver6(x):
  base = 5.47
  if x <= 500:
    return base + (0.03 + 0.0357) * x
  if x <= 1000:
    return base + (0.03 + 0.0357) * 500 + 0.0357 * (x - 500)
  return base + (0.03 + 0.0357) * 500 + 0.0357 * 500 + (0.119 + 0.0357) * (x - 1000)

def test(f):
  kwh = [int(x) for x in sys.argv[1:]]
  return sum(f(x) for x in kwh)

function_dict = {
  'discount_power_economy12': discount_power_economy12,
  'gexa_my_choice12': gexa_my_choice12,
  'discount_power_easy24': discount_power_easy24,
  'power_express_summer24': power_express_summer24,
  'infuse_savings6': infuse_savings6,
  'pioneer_choice24': pioneer_choice24,
  'green_mountain_conserve12': green_mountain_conserve12,
  'discount_super_saver': discount_super_saver,
  'pioneer_simple24': pioneer_simple24,
  'infinite_tremendous': infinite_tremendous,
  'reliant_secure': reliant_secure,
  'pennywise_conserve_saver6': pennywise_conserve_saver6
}

def all_estimates():
  plan_dict = {}
  for key, value in function_dict.items():
    plan_dict[key] = test(value)
  print(json.dumps(plan_dict, sort_keys=True, indent=4))

all_estimates()