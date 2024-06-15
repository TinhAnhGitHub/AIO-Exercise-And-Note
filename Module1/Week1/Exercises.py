import math
import random


########TODO: Exercise 1 ##############
def exercise1(tp: int, fp:int, fn: int) -> int:
    if tp <= 0 or fp <= 0 or fn <= 0:
        print('tp and fp and fn must be greater than zero')
        return -1
    
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * precision * recall / (precision + recall)
    
    return f1_score
    
########TODO: Exercise 1 ##############


########TODO: Exercise 2 ##############
def is_number(n):
    try:
        float(n)
    except ValueError: 
        return False
    return True

def exercise2() -> float:
    x = input("Input x: ")
    if not is_number(x):
        print("x must be a number")
        return -1
    x = float(x)

    activation_function = input("Input activation Function (sigmoid|relu|elu): ")
    result = 0.0
    if activation_function == 'sigmoid':
        result = 1 / (1 + math.exp(-x))
        return result
    elif activation_function == 'relu':
        result = max(0, x)
        return result
    elif activation_function == 'elu':
        alpha = 0.01
        result = x if x > 0 else alpha * (math.exp(x) - 1)
        return result
    else:
        print(f'{activation_function} is not supported')
        return -1
########TODO: Exercise 2 ##############



########TODO: Exercise 3 ##############
# def exercise3():
#     num_samples = input("Input number of samples (integer number) which are generated: ")
#     if not num_samples.isnumeric():
#         print('Number of samples must be an integer number')
#         return



#     loss_name = input("Input loss name (MAE|MSE|RMSE): ")
#     samples = []

#     for i in range(num_samples):
#         pred = random.uniform(0, 10)
#         target = random.uniform(0, 10)

#         samples.append((pred, target))

#         if loss_name == 'MAE':
#             loss = abs(pred - target)
#         elif loss_name == 'MSE':
#             loss = (pred - target) ** 2
#         elif loss_name == 'RMSE':
#             loss = math.sqrt((pred - target) ** 2)
#         else:
#             print(f'{loss_name} is not supported')
#             return
#         print(f'loss name: {loss_name}, sample: {i}, pred: {pred}, target: {target}, loss: {loss}')

def calc_ae(y, y_hat):
    return abs(y - y_hat)


def calc_se(y, y_hat):
    return (y - y_hat) ** 2
########TODO: Exercise 3 ##############





######TODO: Exercise 4 ##############
def factorial(n : int):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def approx_sin(x, n):
    result = 0
    for i in range(n):
        sign = (-1) ** i
        result += sign * (x ** (2 * i + 1) ) / factorial(2 * i + 1)
    print(result)
    return result

def approx_cos(x, n):
    result = 0
    for i in range(n):
        sign = (-1) ** i
        result += sign * (x ** (2 * i)/ (factorial(2 * i)))
    print(result)
    return result

def approx_sinh(x, n):
    result = 0
    for i in range(n):
        result += (x ** (2 * i + 1)) / factorial(2 * i + 1)
    print(result)
    return result

def approx_cosh(x, n):
    result = 0
    for i in range(n):
        result += (x ** (2 * i)) / factorial(2 * i)
    print(result)
    return result
######TODO: EXERCISE 4###############



#######TODO: Exercise 5##############
# def MD_nRE(samples, n= 2, p= 1):
#     m = len(samples)
#     total_error = 0
#     for y_i, y_hat in samples:
#         error = (math.pow(y_i, (1/n)) - math.pow(y_hat, (1/n))) ** p
#         total_error += error
#     mean_error = total_error / m

#     print(mean_error)
#     return mean_error