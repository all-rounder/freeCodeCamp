import numpy as np


def calculate(list):

    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')

    a = np.reshape(list, (3,3))

    mean_c = a.mean(axis=0).tolist()
    mean_r = a.mean(axis=1).tolist()
    mean_f = a.mean()
    print(mean_c, mean_r, mean_f)

    var_c = a.var(axis=0).tolist()
    var_r = a.var(axis=1).tolist()
    var_f = a.var()
    print(var_c, var_r, var_f)

    std_c = a.std(axis=0).tolist()
    std_r = a.std(axis=1).tolist()
    std_f = a.std()
    print(std_c, std_r, std_f)

    max_c = a.max(axis=0).tolist()
    max_r = a.max(axis=1).tolist()
    max_f = a.max()
    print(max_c, max_r, max_f)

    min_c = a.min(axis=0).tolist()
    min_r = a.min(axis=1).tolist()
    min_f = a.min()
    print(min_c, min_r, min_f)

    sum_c = a.sum(axis=0).tolist()
    sum_r = a.sum(axis=1).tolist()
    sum_f = a.sum()
    print(sum_c, sum_r, sum_f)

    result = {'mean': [mean_c, mean_r, mean_f],
              'variance': [var_c, var_r, var_f],
              'standard deviation': [std_c, std_r, std_f],
              'max': [max_c, max_r, max_f],
              'min': [min_c, min_r, min_f],
              'sum': [sum_c, sum_r, sum_f]}
    return result

# calculate([2, 6, 2, 8, 4, 0, 1, 5, 7])