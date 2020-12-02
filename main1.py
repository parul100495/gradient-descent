import numpy as np
import matplotlib.pyplot as plt


def projection(x):
    v = np.sort(x)[:: -1]
    temp2 = []
    for i in range(len(v)):
        temp1 = v[i] + (1 - np.sum(v[:i+1]))/(i+1)
        if temp1 >0:
            temp2.append(i+1)
    temp2 = np.asarray(temp2)
    rho = np.max(temp2)
    lambda_ = (1 - np.sum(v[: rho]))/rho
    return np.maximum(x+lambda_, 0)


def get_return(x, data):
    return_value = 1
    for i in range(data.shape[1]) :
        return_value *= np.dot(data[:, i], x)
    return return_value


def online_gradient_descent(ret, x, eta, t):
    ret = ret[: ,:t]
    df_dx = -np.sum(np.divide(ret, np.dot(ret.transpose(), x)), axis = 1)
    x = x - eta * df_dx
    return projection(x), get_return(projection(x), ret)


def get_top_stocks(sorted_index):
    with open("stockNames.csv", "r") as f:
        stocks = f.readline()
        stock_list = stocks.split(",")
    top_10_stocks = [stock_list[i[0]] for i in sorted_index][0:10]
    top_10_values = [i[1] for i in sorted_index][0:10]
    return top_10_stocks, top_10_values


def third_part():
    data = np.genfromtxt('stockData.csv', delimiter=',')
    return_value = np.zeros_like(data)
    old_data = data[:, 0]
    for i in range(1000):
        return_value[:, i] = data[:, i]/old_data
        old_data = data[:, i]
    n = len(data)
    x = [1/ n ]*n  # equal distribution - initialisation
    eta_array = [0.5]  # [0.01, 0.05, 0.1, 0.5]
    for eta in eta_array:
        returns = []
        for t in range(1, 1000):
            x , t = online_gradient_descent(return_value, x , eta ,t)
            returns.append(t)
        returns = np.array(returns)
        plt.plot(returns)
        plt.show()
        print(returns[-1])

        sort_index = [(i[0], i[1]) for i in sorted(enumerate(x), 
                                                   key=lambda y:y[1], 
                                                   reverse=True)]
        best_stocks, best_values = get_top_stocks(sort_index)
        print(best_stocks, best_values)


third_part()
