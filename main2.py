import numpy as np
import matplotlib.pyplot as plt


def grad_new(x, return_value):
    df_dx = []

    for i in range(490):
        delta_val = 0
        for j in range(1000):
            denominator = np.dot(return_value[:,j], x)
            delta_val += return_value[i,j]/denominator
        df_dx.append(-delta_val)
    return df_dx


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
        return_value *= np.dot(data[:, i].transpose(), x)
    return return_value


def get_top_stocks(sorted_index):
    with open("stockNames.csv", "r") as f:
        stocks = f.readline()
        stock_list = stocks.split(",")
    top_10_stocks = [stock_list[i[0]] for i in sorted_index][0:10]
    top_10_values = [i[1] for i in sorted_index][0:10]
    return top_10_stocks, top_10_values


def second_part():
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
        xs = [[1/ n ]* n]
        returns = []
        for step in range(100) :
            t1 = x - eta * np.array(grad_new(x, return_value))
            t = projection(t1)
            x = t
            returns.append(get_return(x, data))
        plt.plot(returns)
        plt.show()
        sort_index = [(i[0], i[1]) for i in sorted(enumerate(x), 
                                           key=lambda y:y[1], 
                                           reverse=True)]
	ret_ = get_return(x, data)
	best_stocks, best_values = get_top_stocks(sort_index)
        print(best_stocks, best_values)
    return x

second_part()
