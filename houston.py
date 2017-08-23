def discount_power_economy12(x):
  base = 3.25+5.47
  if x <= 500:
    return base + (.83+3.57)/100*x
  if x <= 1000:
    return base + (.83+3.57)/100*500 + (11.37+3.57)/100*(x-500)
  if x > 1001:
    return base + (.83+3.57)/100*500 + (11.37+3.57)/100*500 + (10.58+3.57)/100*(x-1000)

def gexa_my_choice12(x):
  base = 15.47
  if x <= 1000:
    return base + (.0021+.0357)*x
  if x <= 1250:
    return base+(.0021+.0357)*1000 + (.49+.0357)*(x-1000)
  if x <=  2000:
    return base+(.0021+.0357)*1000 + (.49+.0357)*(250) + (.0001+.0357)*(x-1250)
  
def discount_power_easy24(x):
  base = 18.47
  if x <= 1000:
    return base + (.0013+.0357)*x
  return base + (.0013+.0357)*1000 + (.1357+.0357)*(x-1000)

def power_express_summer24(x):
  base = 14.25+5.47
  if x <= 1000:
    return base + (.1 + .0357)*x
  return base + (.1+.0357)*1000 + (.1364+.0357)*(x-1000)

def infuse_savings6(x):
  if x <= 1000:
    return 39
  return 99 + (x-1000)*.106

def pioneer_choice24(x):
  return 0.0834*x

def green_mountain_conserve12(x):
  base = 5.47 + 10
  if x <= 1000:
    return base + (.018343+.035686)*x
  return base + (.018343+.035686)*1000 + (.093813+.035686)*(x-1000)

def discount_super_saver(x):
  base = 5.47
  return base + (.04003+.0357)*x

def pioneer_simple24(x):
  base = 3.25
  return base + (.0801)*x

def infinite_tremendous(x):
  base = 5.47
  if x <= 500:
    return base + (.0357+.044311)*x
  if x <= 1000:
    return base + (.0357+.044311)*500 + (.0357+.034311)*(x-500)
  return (.094311+.0357)*(x-1000) + base + (.0357+.044311)*500 + (.0357+.034311)*500

def reliant_secure(x):
  base = 10.47
  return base + (.035686+ .038)*x

def wise_buy_conserve_saver6(x):
  base = 5.47
  if x <= 500:
    return base + (.03+.0357)*x
  if x <= 1000:
    return base + (.03+.0357)*500 + (.0357)*(x-500)
  return base + (.03+.0357)*500 + (.0357)*500 + (.0357+.119)*(x-1000)

def pennywise_conserve_saver6(x):
  base = 5.47
  if x <= 500:
    return base + (.03+.0357)*x
  if x <= 1000:
    return base + (.03+.0357)*500 + (.0357)*(x-500)
  return base + (.03+.0357)*500 + .0357*500 + (.119+.0357)*(x-1000)
  
def test(f):
  #kwh = [100, 250, 500, 750, 1000, 1250, 1500, 2000]
  kwh = [103, 185, 337, 615, 861, 1200, 400, 350, 200, 200, 200, 150]
  #return [f(x) for x in kwh]
  return sum(f(x) for x in kwh)


print(test(discount_power_economy12))
print(test(gexa_my_choice12))
print(test(discount_power_easy24))
print(test(power_express_summer24))
print(test(infuse_savings6))
print(test(pioneer_choice24))
print(test(green_mountain_conserve12))
print(test(discount_super_saver))
print(test(pioneer_simple24))
print(test(infinite_tremendous))
print(test(reliant_secure))
print(test(pennywise_conserve_saver6)) #cheapest at $370


