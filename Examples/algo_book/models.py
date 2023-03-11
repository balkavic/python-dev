import numpy as np
import math
from scipy.optimize import curve_fit


def linear_model(n, a, b):
    return a * n + b


def log_log_model(n, a):
    print(type(n))
    print(n)
    log1 = np.log2(n)
    return a * (np.log2(log1))


def f4(N):
    ct = 1
    while N >= 2:
        ct = ct + 1
        N = N ** 0.5
    return ct


# Sample data
# xs = [100, 1000, 10000]
# ys = [0.063, 0.565, 5.946]
#
# # Coefficients are returned as first argument
# [(a, b), _] = curve_fit(linear_model, np.array(xs), np.array(ys))
# print('Linear = {}*N + {}'.format(a, b))


xs = [2 ** 5, 2 ** 10, 2 ** 20]
ys = [4, 5, 6]

# Coefficients are returned as first argument
[a, _] = curve_fit(log_log_model, np.array(xs), np.array(ys))
print('Log(log) = {}*log(log(N))'.format(a))

for n in range(1, 51):
    model_res = a * math.log(math.log(2 ** n, 2), 2)
    real = f4(2 ** n)
    print("{}: --- Model: {} --- Real: {}".format(n, model_res, real))

# N = 2 ** 50
# ct = f4(N)
#
# print('f4({}) = {}'.format(N, ct))

