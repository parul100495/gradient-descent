import numpy as np


def best_stock(profit_ratio):
    return np.max(profit_ratio)


def equal_proportion(profit_ratio):
    return np.average(profit_ratio)


def equal_percent(data):
    stock_old = 1
    for i in range(1, 1000) :
        return_value = np.divide(data[:, i], data[:, i-1])
        stock_new = stock_old * np.average(return_value)
        stock_old = stock_new
    return np.average(stock_new)


def first_part():
    data = np.genfromtxt('stockData.csv', delimiter=',')
    return_value = np.zeros_like(data)
    old_data = data[:, 0]
    for i in range(1000):
        return_value[:, i] = data[:, i]/old_data
        old_data = data[:, i]

    profit_ratio = np.divide(data[:, 999], data[:, 0])

    print("Best stock: ", best_stock(profit_ratio))
    print("Equal money stocks : ", equal_proportion(profit_ratio))
    print("Equal percent stocks (CRP): ", equal_percent(data))


first_part()
