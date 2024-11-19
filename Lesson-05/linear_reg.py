import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#引入数据
path =  'data1.txt'
data = pd.read_csv(path, header=None, names=['Population', 'Profit'])
data.plot(kind='scatter', x='Population', y='Profit', figsize=(12,8))
#看下数据长什么样子
plt.show()
#代价函数
def computeCost(X, y, theta):
    inner = np.power(((X * theta.T) - y), 2)
    return np.sum(inner) / (2 * len(X))
#让我们在训练集中添加一列，以便我们可以使用向量化的解决方案来计算代价和梯度。即偏置项
data.insert(0, 'Ones', 1)
#现在我们来做一些变量初始化。
# set X (training data) and y (target variable)
cols = data.shape[1]
X = data.iloc[:,0:cols-1]#X是所有行，去掉最后一列
y = data.iloc[:,cols-1:cols]#X是所有行，最后一列
#代价函数是应该是numpy矩阵，所以我们需要转换X和Y，然后才能使用它们。 我们还需要初始化theta。
X = np.matrix(X.values)
y = np.matrix(y.values)
theta = np.matrix(np.array([0,0]))
#计算代价函数 (theta初始值为0).
computeCost(X, y, theta)

#批量梯度下降
def gradientDescent(X, y, theta, alpha, iters):
    temp = np.matrix(np.zeros(theta.shape))
    parameters = int(theta.ravel().shape[1])
    cost = np.zeros(iters)

    for i in range(iters):
        error = (X * theta.T) - y

        for j in range(parameters):
            term = np.multiply(error, X[:, j])
            temp[0, j] = theta[0, j] - ((alpha / len(X)) * np.sum(term))

        theta = temp
        cost[i] = computeCost(X, y, theta)

    return theta, cost
#初始化一些附加变量 - 学习速率α和要执行的迭代次数。
alpha = 0.01
iters = 1000
#现在让我们运行梯度下降算法来将我们的参数θ适合于训练集。
g, cost = gradientDescent(X, y, theta, alpha, iters)
#最后，我们可以使用我们拟合的参数计算训练模型的代价函数（误差）。
computeCost(X, y, g)

#现在我们来绘制线性模型以及数据，直观地看出它的拟合。
x = np.linspace(data.Population.min(), data.Population.max(), 100)
f = g[0, 0] + (g[0, 1] * x)

fig, ax = plt.subplots(figsize=(12,8))
ax.plot(x, f, 'r', label='Prediction')
ax.scatter(data.Population, data.Profit, label='Traning Data')
ax.legend(loc=2)
ax.set_xlabel('Population')
ax.set_ylabel('Profit')
ax.set_title('Predicted Profit vs. Population Size')
plt.show()