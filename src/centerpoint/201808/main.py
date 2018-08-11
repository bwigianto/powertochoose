import houston
import inspect
import sys, json

all_functions = inspect.getmembers(houston, inspect.isfunction)

def calc_total_billing(f):
  kwh = [int(x) for x in sys.argv[1:]]
  return sum(f(x) for x in kwh)

def all_estimates():
  plans = {}
  for key, value in all_functions:
    plans[key] = calc_total_billing(value)
  sorted_plans = sorted(plans.items(), key=lambda x: x[1])
  return json.dumps(sorted_plans, sort_keys=True, indent=4)

if __name__ == "__main__":
    print(all_estimates())
