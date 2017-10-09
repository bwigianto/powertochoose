import houston
import inspect
import sys, json

all_functions = inspect.getmembers(houston, inspect.isfunction)

def calc_total_billing(f):
  kwh = [int(x) for x in sys.argv[1:]]
  return sum(f(x) for x in kwh)

def all_estimates():
  plan_dict = {}
  for key, value in all_functions:
    plan_dict[key] = calc_total_billing(value)
  return json.dumps(plan_dict, sort_keys=True, indent=4)


if __name__ == "__main__":
    print(all_estimates())