#!/usr/bin/env sage

# Modulus Prime
p = 298161833288328455288826827978944092433
# Generator
g = 216590906870332474191827756801961881648

# Public Keys
g_power_a = 181553548982634226931709548695881171814
g_power_b = 64889049934231151703132324484506000958

F = IntegerModRing(p)

# Solve for discrete log
a = discrete_log(F(g_power_a), F(g))
print('Private Key A:', a)

b = discrete_log(F(g_power_b), F(g))
print('Private Key B:', b)

# Solve for shared key
key = pow(g, a*b, p)
print('Shared Key:', key)
