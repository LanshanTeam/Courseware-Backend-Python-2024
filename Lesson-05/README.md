# 机器学习

机器学习指计算机通过观察环境，与环境交互，在吸取信息中学习、自我更新和进步。

对计算机而言，"经验"通常以"数据"形式存在因此机器学习所研究的主要内容，是关于在计算机上从数据中产生"模型"的算法，即"学习算法"。我们把经验数据提供给它，它就能基于这些数据产生模型;在面对新的情况时，模型会给我们提供相应的判断。

简单地说，大多数机器学习算法可以分成 **训练(training)** 和 **测试(testing)** 两个步骤。训练，一般需要训练数据，就是告诉机器前人的经验，比如什么是猫、什么是狗、看到什么该停车。
训练学习的结果，可以认为是机器写的程序或者存储的数据，即模型。

机器学习有一类学习方法叫做**监督学习**，它是说为了训练一个模型，我们要提供这样一堆训练样本：每个训练样本既包括输入特征x，也包括对应的输出y(y也叫做标记，label)。也就是说，我们要找到很多人，我们既知道他们的特征(工作年限，行业...)，也知道他们的收入。我们用这样的样本去训练模型，让模型既看到我们提出的每个问题(输入特征x)，也看到对应问题的答案(标记y)。当模型看到足够多的样本之后，它就能总结出其中的一些规律。然后，就可以预测那些它没看过的输入所对应的答案了。

另外一类学习方法叫做**无监督学习**，这种方法的训练样本中只有x而没有y。模型可以总结出特征x的一些规律，但是无法知道其对应的答案y。
很多时候，既有x又有y的训练样本是很少的，大部分样本都只有x。比如在语音到文本(STT)的识别任务中，x是语音，y是这段语音对应的文本。我们很容易获取大量的语音录音，然而把语音一段一段切分好并标注上对应文字则是非常费力气的事情。这种情况下，为了弥补带标注样本的不足，我们可以用无监督学习方法先做一些聚类，让模型总结出哪些音节是相似的，然后再用少量的带标注的训练样本，告诉模型其中一些音节对应的文字。这样模型就可以把相似的音节都对应到相应文字上，完成模型的训练。

>有监督好比有老师告诉你正确答案；无监督仅靠观察自学，机器自己在数据里找模式和特征。

## 基本概念

**数据（Data）**：关于研究对象的记录或信息。根据是否包含标签，可分为有标签数据（监督学习）和无标签数据（无监督学习）。

**数据集（Data Set）**：由多个数据记录组成的集合，用于训练或测试机器学习模型。

**样本（Sample）**：数据集中的一条记录，用于训练或测试模型。

**特征（Feature）**：反映事件或对象在某方面的表现或性质的事项，用于训练机器学习模型。

假如我们把某件事物的属性作为坐标轴，例如书本的颜色、类型、页数，则它们张成一个用于描述书本的n维空间，每本书都可在这个空间中找到自己的坐标位置。
由于空间中的每个点对应一个坐标向量，因此我们也把一个样本称为一个 **特征向量(feature vector)**。

**标签（Label）**：关于样本结果的信息，用于监督学习中指导模型学习。

从数据中学得模型的过程称为 **学习 (learning)** 或 **训练 (training)** ，这个过程通过执行某个学习算法来完成。训练过程中使用的数据称为**训练数据(training data)**，
其中每个样本称为一个**训练样本(training sample)**, 训练样本组成的集合称为**训练集 (training set)**。学得模型对应了关于数据的某种潜在的规律。
若我们欲预测的是离散值，例如书的好坏，此类学习任务称为**分类(classification)**; 若欲预测的是连续值，例如书籍受欢迎度：0.85、 0.47。此类学习任务称为**回归(regression)**。

## 方法

模型假设、评价函数和优化算法是构成模型的三个关键要素。

模型假设：我们可以把学习过程看作一个在所有假设组成的空间中进行搜索的过程，搜索目标是找到与训练集匹配的假设，即能够将训练集中的对象判断正确的假设。假设的表示一旦确定，假设空间及其规模大小就确定了。

评价函数：寻找最优之前，我们需要先定义什么是最优，即评价关系的好坏的指标。通常衡量该关系是否能很好的拟合现有观测样本，将拟合的误差最小作为优化目标。

优化算法：设置了评价指标后，就可以在假设圈定的范围内，将使得评价指标最优的关系找出来，这个寻找最优解的方法即为优化算法。

## 常见模型

>机器学习会涉及到许多模型，例如线性模型、决策树、支持向量机、神经网络等等，这里简单介绍线性模型和神经网络


> ### 线性回归

### 2.1 模型表示

我们的第一个学习算法是线性回归算法。你会看到这个算法的概况，更重要的是你将会了解监督学习过程完整的流程。

让我们通过一个例子来开始：这个例子是预测住房价格的，我们要使用一个数据集，数据集包含俄勒冈州波特兰市的住房价格。在这里，我要根据不同房屋尺寸所售出的价格，画出我的数据集。比方说，如果你朋友的房子是1250平方尺大小，你要告诉他们这房子能卖多少钱。那么，你可以做的一件事就是构建一个模型，也许是条直线，从这个数据模型上来看，也许你可以告诉你的朋友，他能以大约220000(美元)左右的价格卖掉这个房子。这就是监督学习算法的一个例子。

[![](https://github.com/fengdu78/Coursera-ML-AndrewNg-Notes/raw/master/images/8e76e65ca7098b74a2e9bc8e9577adfc.png)


它被称作监督学习是因为对于每个数据来说，我们给出了“正确的答案”，即告诉我们：根据我们的数据来说，房子实际的价格是多少，而且，更具体来说，这是一个回归问题。回归一词指的是，我们根据之前的数据预测出一个准确的输出值，对于这个例子就是价格，同时，还有另一种最常见的监督学习方式，叫做分类问题，当我们想要预测离散的输出值，例如，我们正在寻找癌症肿瘤，并想要确定肿瘤是良性的还是恶性的，这就是0/1离散输出的问题。更进一步来说，在监督学习中我们有一个数据集，这个数据集被称训练集。

**我将在整个课程中用小写的 $m$ 来表示训练样本的数目。**

以之前的房屋交易问题为例，假使我们回归问题的训练集（**Training Set**）如下表所示：

![](https://github.com/fengdu78/Coursera-ML-AndrewNg-Notes/raw/master/images/44c68412e65e62686a96ad16f278571f.png)

我们将要用来描述这个回归问题的标记如下:

$m$ 代表训练集中实例的数量

$x$  代表特征/输入变量

$y$ 代表目标变量/输出变量

$\left( x,y \right)$ 代表训练集中的实例

$({{x}^{(i)}},{{y}^{(i)}})$ 代表第 $i$ 个观察实例

$h$ 代表学习算法的解决方案或函数也称为假设（**hypothesis**）

![](https://github.com/fengdu78/Coursera-ML-AndrewNg-Notes/raw/master/images/ad0718d6e5218be6e6fce9dc775a38e6.png)

这就是一个监督学习算法的工作方式，我们可以看到这里有我们的训练集里房屋价格
我们把它喂给我们的学习算法，学习算法的工作了，然后输出一个函数，通常表示为小写 $h$ 表示。 $h$ 代表**hypothesis**(**假设**)， $h$ 表示一个函数，输入是房屋尺寸大小，就像你朋友想出售的房屋，因此 $h$ 根据输入的 $x$ 值来得出 $y$ 值，$y$ 值对应房子的价格 因此，$h$ 是一个从 $x$ 到 $y$ 的函数映射。

我将选择最初的使用规则 $h$ 代表**hypothesis**，因而，要解决房价预测问题，我们实际上是要将训练集“喂”给我们的学习算法，进而学习得到一个假设 $h$ ，然后将我们要预测的房屋的尺寸作为输入变量输入给 $h$ ，预测出该房屋的交易价格作为输出变量输出为结果。那么，对于我们的房价预测问题，我们该如何表达 $h$ ？

一种可能的表达方式为： $h_\theta \left( x \right)=\theta_{0} + \theta_{1}x$ ，因为只含有一个特征/输入变量，因此这样的问题叫作单变量线性回归问题。

### 2.2 代价函数

我们将定义代价函数的概念，这有助于我们弄清楚如何把最有可能的直线与我们的数据相拟合。如图

![](https://github.com/fengdu78/Coursera-ML-AndrewNg-Notes/raw/master/images/d385f8a293b254454746adee51a027d4.png)

在线性回归中我们有一个像这样的训练集， $m$ 代表了训练样本的数量，比如 $m = 47$ 。而我们的假设函数，也就是用来进行预测的函数，是这样的线性函数形式： $h_\theta \left( x \right)=\theta_{0}+\theta_{1}x$ 。

接下来我们会引入一些术语我们现在要做的便是为我们的模型选择合适的**参数**（**parameters**） $\theta_{0}$ 和 $\theta_{1}$ ，在房价问题这个例子中便是直线的斜率和在 $y$ 轴上的截距。

我们选择的参数决定了我们得到的直线相对于我们的训练集的准确程度，模型所预测的值与训练集中实际值之间的差距（下图中蓝线所指）就是**建模误差**（**modeling error**）。

![](https://github.com/fengdu78/Coursera-ML-AndrewNg-Notes/raw/master/images/6168b654649a0537c67df6f2454dc9ba.png)

我们的目标便是选择出可以使得建模误差的平方和能够最小的模型参数。 即使得代价函数 $J \left( \theta_0, \theta_1 \right) = \frac{1}{2m}\sum\limits_{i=1}^m \left( h_{\theta}(x^{(i)})-y^{(i)} \right)^{2}$ 最小。

我们绘制一个等高线图，三个坐标分别为 $\theta_{0}$ 和 $\theta_{1}$ 和 $J(\theta_{0}, \theta_{1})$ ：


![](https://github.com/fengdu78/Coursera-ML-AndrewNg-Notes/raw/master/images/27ee0db04705fb20fab4574bb03064ab.png)

则可以看出在三维空间中存在一个使得 $J(\theta_{0}, \theta_{1})$ 最小的点。

代价函数也被称作平方误差函数，有时也被称为平方误差代价函数。我们之所以要求出误差的平方和，是因为误差平方代价函数，对于大多数问题，特别是回归问题，都是一个合理的选择。还有其他的代价函数也能很好地发挥作用，但是平方误差代价函数可能是解决回归问题最常用的手段了。

在后续课程中，我们还会谈论其他的代价函数，但我们刚刚讲的选择是对于大多数线性回归问题非常合理的。

也许这个函数 $J(\theta_{0}, \theta_{1})$ 有点抽象，可能你仍然不知道它的内涵，我们更进一步解释代价函数J的工作原理，并尝试更直观地解释它在计算什么，以及我们使用它的目的。

### 2.3 代价函数的直观理解I

在上一节中，我们给了代价函数一个数学上的定义。让我们通过一些例子来获取一些直观的感受，看看代价函数到底是在干什么。

![](https://github.com/fengdu78/Coursera-ML-AndrewNg-Notes/raw/master/images/10ba90df2ada721cf1850ab668204dc9.png)

![](https://github.com/fengdu78/Coursera-ML-AndrewNg-Notes/raw/master/images/2c9fe871ca411ba557e65ac15d55745d.png)

### 2.4 代价函数的直观理解II

这节中，我们将更深入地学习代价函数的作用，假设你已经认识等高线图，如果你对等高线图不太熟悉的话，这节中的某些内容你可能会听不懂，但不要紧，如果你跳过这段的话，也没什么关系，不听这节课对后续课程理解影响不大。

![](https://github.com/fengdu78/Coursera-ML-AndrewNg-Notes/raw/master/images/0b789788fc15889fe33fb44818c40852.png)

代价函数的样子，等高线图，则可以看出在三维空间中存在一个使得 $J(\theta_{0}, \theta_{1})$ 最小的点。

![](https://github.com/fengdu78/Coursera-ML-AndrewNg-Notes/raw/master/images/86c827fe0978ebdd608505cd45feb774.png)

通过这些图形，我希望你能更好地理解这些代价函数 $J$ 所表达的值是什么样的，它们对应的假设是什么样的，以及什么样的假设对应的点，更接近于代价函数 $J$ 的最小值。

当然，我们真正需要的是一种有效的算法，能够自动地找出这些使代价函数 $J$ 取最小值的参数 $\theta_{0}$ 和 $\theta_{1}$ 来。

我们也不希望编个程序把这些点画出来，然后人工的方法来读出这些点的数值，这很明显不是一个好办法。我们会遇到更复杂、更高维度、更多参数的情况，而这些情况是很难画出图的，因此更无法将其可视化，因此我们真正需要的是编写程序来找出这些最小化代价函数的 $\theta_{0}$ 和 $\theta_{1}$ 的值，我们将介绍一种算法，能够自动地找出能使代价函数 $J$ 最小化的参数 $\theta_{0}$ 和 $\theta_{1}$ 的值。

### 2.5 梯度下降

梯度下降是一个用来求函数最小值的算法，我们将使用梯度下降算法来求出代价函数 $J(\theta_{0}, \theta_{1})$ 的最小值。

梯度下降背后的思想是：开始时我们随机选择一个参数的组合 $\left( {\theta_{0}},{\theta_{1}},......,{\theta_{n}} \right)$ ，计算代价函数，然后我们寻找下一个能让代价函数值下降最多的参数组合。我们持续这么做直到找到一个局部最小值（**local minimum**），因为我们并没有尝试完所有的参数组合，所以不能确定我们得到的局部最小值是否便是全局最小值（**global minimum**），选择不同的初始参数组合，可能会找到不同的局部最小值。

![](https://github.com/fengdu78/Coursera-ML-AndrewNg-Notes/raw/master/images/db48c81304317847870d486ba5bb2015.jpg)

想象一下你正站立在山的这一点上，站立在你想象的公园这座红色山上，在梯度下降算法中，我们要做的就是旋转360度，看看我们的周围，并问自己要在某个方向上，用小碎步尽快下山。这些小碎步需要朝什么方向？如果我们站在山坡上的这一点，你看一下周围，你会发现最佳的下山方向，你再看看周围，然后再一次想想，我应该从什么方向迈着小碎步下山？然后你按照自己的判断又迈出一步，重复上面的步骤，从这个新的点，你环顾四周，并决定从什么方向将会最快下山，然后又迈进了一小步，并依此类推，直到你接近局部最低点的位置。

批量梯度下降（**batch gradient descent**）算法的公式为：

![](https://github.com/fengdu78/Coursera-ML-AndrewNg-Notes/raw/master/images/7da5a5f635b1eb552618556f1b4aac1a.png)

其中 $a$ 是学习率（**learning rate**），它决定了我们沿着能让代价函数下降程度最大的方向向下迈出的步子有多大，在批量梯度下降中，我们每一次都同时让所有的参数减去学习速率乘以代价函数的导数。

![](https://github.com/fengdu78/Coursera-ML-AndrewNg-Notes/raw/master/images/ef4227864e3cabb9a3938386f857e938.png)

在梯度下降算法中，还有一个更微妙的问题，梯度下降中，我们要更新 ${\theta_{0}}$ 和 ${\theta_{1}}$ ，当 $j=0$ 和 $j=1$ 时，会产生更新，所以你将更新 $J\left( {\theta_{0}} \right)$ 和 $J\left( {\theta_{1}} \right)$ 。实现梯度下降算法的微妙之处是，在这个表达式中，如果你要更新这个等式，你需要同时更新 ${\theta_{0}}$ 和 ${\theta_{1}}$ ，我的意思是在这个等式中，我们要这样更新：

${\theta_{0}}$ := ${\theta_{0}}$ ，并更新 ${\theta_{1}}$ := ${\theta_{1}}$ 。

实现方法是：你应该计算公式右边的部分，通过那一部分计算出 ${\theta_{0}}$ 和 ${\theta_{1}}$ 的值，然后同时更新 ${\theta_{0}}$ 和 ${\theta_{1}}$ 。

让我进一步阐述这个过程：

![](https://github.com/fengdu78/Coursera-ML-AndrewNg-Notes/raw/master/images/13176da01bb25128c91aca5476c9d464.png)

在梯度下降算法中，这是正确实现同时更新的方法。我不打算解释为什么你需要同时更新，同时更新是梯度下降中的一种常用方法。我们之后会讲到，同步更新是更自然的实现方法。当人们谈到梯度下降时，他们的意思就是同步更新。

在接下来的视频中，我们要进入这个微分项的细节之中。我已经写了出来但没有真正定义，如果你已经修过微积分课程，如果你熟悉偏导数和导数，这其实就是这个微分项：

$\alpha \frac{\partial }{\partial \theta_{0}} J(\theta_{0}, \theta_{1})$

$\alpha \frac{\partial }{\partial \theta_{1}} J(\theta_{0}, \theta_{1})$

如果你不熟悉微积分，不用担心，即使你之前没有看过微积分，或者没有接触过偏导数，接下来，你会得到一切你需要知道，如何计算这个微分项的知识。

### 2.6 梯度下降的直观理解

在之前，我们给出了一个数学上关于梯度下降的定义，我们更深入研究一下，更直观地感受一下这个算法是做什么的，以及梯度下降算法的更新过程有什么意义。梯度下降算法如下：

${\theta_{j}}:={\theta_{j}}-\alpha \frac{\partial }{\partial {\theta_{j}}}J\left(\theta \right)$

描述：对 $\theta $ 赋值，使得 $J\left( \theta  \right)$ 按梯度下降最快方向进行，一直迭代下去，最终得到局部最小值。其中 $a$ 是学习率（**learning rate**），它决定了我们沿着能让代价函数下降程度最大的方向向下迈出的步子有多大。

![](https://github.com/fengdu78/Coursera-ML-AndrewNg-Notes/raw/master/images/ee916631a9f386e43ef47efafeb65b0f.png)


对于这个问题，求导的目的，基本上可以说取这个红点的切线，就是这样一条红色的直线，刚好与函数相切于这一点，让我们看看这条红色直线的斜率，就是这条刚好与函数曲线相切的这条直线，这条直线的斜率正好是这个三角形的高度除以这个水平长度，现在，这条线有一个正斜率，也就是说它有正导数，因此，我得到的新的 ${\theta_{1}}$ , ${\theta_{1}}$ 更新后等于 ${\theta_{1}}$ 减去一个正数乘以 $a$ 。

这就是我梯度下降法的更新规则：${\theta_{j}}:={\theta_{j}}-\alpha \frac{\partial }{\partial {\theta_{j}}}J\left( \theta  \right)$

让我们来看看如果 $a$ 太小或 $a$ 太大会出现什么情况：

如果 $a​$ 太小了，即我的学习速率太小，结果就是只能这样像小宝宝一样一点点地挪动，去努力接近最低点，这样就需要很多步才能到达最低点，所以如果$a$太小的话，可能会很慢，因为它会一点点挪动，它会需要很多步才能到达全局最低点。

如果 $a$ 太大，那么梯度下降法可能会越过最低点，甚至可能无法收敛，下一次迭代又移动了一大步，越过一次，又越过一次，一次次越过最低点，直到你发现实际上离最低点越来越远，所以，如果 $a$ 太大，它会导致无法收敛，甚至发散。

我们来看一个例子，这是代价函数 $J\left( \theta  \right)$ 。

![](https://github.com/fengdu78/Coursera-ML-AndrewNg-Notes/raw/master/images/4668349e04cf0c4489865e133d112e98.png)

我想找到它的最小值，首先初始化我的梯度下降算法，在那个品红色的点初始化，如果我更新一步梯度下降，也许它会带我到这个点，因为这个点的导数是相当陡的。现在，在这个绿色的点，如果我再更新一步，你会发现我的导数，也即斜率，是没那么陡的。随着我接近最低点，我的导数越来越接近零，所以，梯度下降一步后，新的导数会变小一点点。然后我想再梯度下降一步，在这个绿点，我自然会用一个稍微跟刚才在那个品红点时比，再小一点的一步，到了新的红色点，更接近全局最低点了，因此这点的导数会比在绿点时更小。所以，我再进行一步梯度下降时，我的导数项是更小的， ${\theta_{1}}$ 更新的幅度就会更小。所以随着梯度下降法的运行，你移动的幅度会自动变得越来越小，直到最终移动幅度非常小，你会发现，已经收敛到局部极小值。

回顾一下，在梯度下降法中，当我们接近局部最低点时，梯度下降法会自动采取更小的幅度，这是因为当我们接近局部最低点时，很显然在局部最低时导数等于零，所以当我们接近局部最低时，导数值会自动变得越来越小，所以梯度下降将自动采取较小的幅度，这就是梯度下降的做法。所以实际上没有必要再另外减小 $a$ 。

这就是梯度下降算法，你可以用它来最小化任何代价函数 $J$ ，不只是线性回归中的代价函数 $J$ 。

在接下来的视频中，我们要用代价函数 $J$ ，回到它的本质，线性回归中的代价函数。也就是我们前面得出的平方误差函数，结合梯度下降法，以及平方代价函数，我们会得出第一个机器学习算法，即线性回归算法。

### 2.7 梯度下降的线性回归

在以前的视频中我们谈到关于梯度下降算法，梯度下降是很常用的算法，它不仅被用在线性回归上和线性回归模型、平方误差代价函数。在这段视频中，我们要将梯度下降和代价函数结合。我们将用到此算法，并将其应用于具体的拟合直线的线性回归算法里。

梯度下降算法和线性回归算法比较如图：

![](https://github.com/fengdu78/Coursera-ML-AndrewNg-Notes/raw/master/images/5eb364cc5732428c695e2aa90138b01b.png)

我们刚刚使用的算法，有时也称为批量梯度下降。实际上，在机器学习中，通常不太会给算法起名字，但这个名字”**批量梯度下降**”，指的是在梯度下降的每一步中，我们都用到了所有的训练样本，在梯度下降中，在计算微分求导项时，我们需要进行求和运算，所以，在每一个单独的梯度下降中，我们最终都要计算这样一个东西，这个项需要对所有$m$个训练样本求和。因此，批量梯度下降法这个名字说明了我们需要考虑所有这一"批"训练样本，而事实上，有时也有其他类型的梯度下降法，不是这种"批量"型的，不考虑整个的训练集，而是每次只关注训练集中的一些小的子集。在后面的课程中，我们也将介绍这些方法。

但就目前而言，应用刚刚学到的算法，你应该已经掌握了批量梯度算法，并且能把它应用到线性回归中了，这就是用于线性回归的梯度下降法。

现在我们已经掌握了梯度下降，我们可以在不同的环境中使用梯度下降法，我们还将在不同的机器学习问题中大量地使用它。所以，祝贺大家成功学会你的第一个机器学习算法。


```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

引入数据

```
path =  'data1.txt'
data = pd.read_csv(path, header=None, names=['Population', 'Profit'])
data.plot(kind='scatter', x='Population', y='Profit', figsize=(12,8))
#看下数据长什么样子
plt.show()
```

首先，我们将创建一个以参数θ为特征函数的代价函数
$J\\left( \\theta  \\right)=\\frac{1}{2m}\\sum\\limits_{i=1}^{m}{{{\\left( {{h}_{\\theta }}\\left( {{x}^{(i)}} \\right)-{{y}^{(i)}} \\right)}^{2}}}$

其中： $h_{\theta}(x) = \theta^{T}X = \theta_{0}x_{0} + \theta_{1}x_{1} + \theta_{2}x_{2} + \dots + \theta_{n}x_{n}\$

```
#代价函数
def computeCost(X, y, theta):
    inner = np.power(((X * theta.T) - y), 2)
    return np.sum(inner) / (2 * len(X))
```

让我们在训练集中添加一列，以便我们可以使用向量化的解决方案来计算代价和梯度。
```
data.insert(0, 'Ones', 1)
```

现在我们来做一些变量初始化。
```
# set X (training data) and y (target variable)
cols = data.shape[1]
X = data.iloc[:,0:cols-1]#X是所有行，去掉最后一列
y = data.iloc[:,cols-1:cols]#X是所有行，最后一列
```

代价函数是应该是numpy矩阵，所以我们需要转换X和Y，然后才能使用它们。 我们还需要初始化theta。
```
X = np.matrix(X.values)
y = np.matrix(y.values)
theta = np.matrix(np.array([0,0]))
```

计算代价函数 (theta初始值为0).
```
computeCost(X, y, theta)
```

# batch gradient decent（批量梯度下降）

```
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
```

初始化一些附加变量 - 学习速率α和要执行的迭代次数。
```
alpha = 0.01
iters = 1000
```

现在让我们运行梯度下降算法来将我们的参数θ适合于训练集。
```
g, cost = gradientDescent(X, y, theta, alpha, iters)
g
```

最后，我们可以使用我们拟合的参数计算训练模型的代价函数（误差）。
```
computeCost(X, y, g)
```

现在我们来绘制线性模型以及数据，直观地看出它的拟合。
```
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
```


## 线性神经网络

神经元接收到来自n个其他神经元传递过来的输入信号，这些输入信号通过带权重的连接进行传递，
神经元接收到的总输入值将与神经元的阀值进行比较，然后通过"激活函数" (activation function) 处理以产生神经元的输出。

### 感知器

为了理解神经网络，我们应该先理解神经网络的组成单元——**神经元**。神经元也叫做**感知器**。

![深度学习实战教程(一)：感知器](https://cuijiahua.com/wp-content/uploads/2018/10/dl-7-2.png)

神经元：神经网络中每个节点称为神经元，由两部分组成：

加权和：将所有输入加权求和。

激活函数：加权和的结果经过一个非线性函数变换，让神经元计算具备非线性的能力。



(1) **输入权值** 一个感知器可以接收多个输入：

[![深度学习实战教程(一)：感知器](https://cuijiahua.com/wp-content/uploads/2018/10/dl-7-4.png)](https://cuijiahua.com/wp-content/uploads/2018/10/dl-7-4.png)

每个输入上有一个**权值**：

[![深度学习实战教程(一)：感知器](https://cuijiahua.com/wp-content/uploads/2018/10/dl-7-5.png)](https://cuijiahua.com/wp-content/uploads/2018/10/dl-7-5.png)

此外还有一个**偏置项**：

[![深度学习实战教程(一)：感知器](https://cuijiahua.com/wp-content/uploads/2018/10/dl-7-6.png)](https://cuijiahua.com/wp-content/uploads/2018/10/dl-7-6.png)

就是上图中的w0。

(2) **激活函数** 感知器的激活函数可以有很多选择，比如我们可以选择下面这个**阶跃函数f**来作为激活函数：

[![深度学习实战教程(一)：感知器](https://cuijiahua.com/wp-content/uploads/2018/10/dl-7-7.png)](https://cuijiahua.com/wp-content/uploads/2018/10/dl-7-7.png)

(3) **输出** 感知器的输出由下面这个公式来计算：

[![深度学习实战教程(一)：感知器](https://cuijiahua.com/wp-content/uploads/2018/10/dl-7-8-1.png)](https://cuijiahua.com/wp-content/uploads/2018/10/dl-7-8-1.png)

### 训练一个与函数

| x1   | x2   | y    |
| ---- | ---- | ---- |
| 0    | 0    | 0    |
| 0    | 1    | 0    |
| 1    | 0    | 0    |
| 1    | 1    | 1    |

我们令：

[![深度学习实战教程(一)：感知器](https://cuijiahua.com/wp-content/uploads/2018/10/dl-7-10.png)](https://cuijiahua.com/wp-content/uploads/2018/10/dl-7-10.png)

而激活函数就f是前面写出来的**阶跃函数**，这时，感知器就相当于**and**函数。不明白？我们验算一下：

输入上面真值表的第一行，即x1=0；x2=0，那么根据公式(1)，计算输出：

[![深度学习实战教程(一)：感知器](https://cuijiahua.com/wp-content/uploads/2018/10/dl-7-11.png)](https://cuijiahua.com/wp-content/uploads/2018/10/dl-7-11.png)

也就是当x1x2都为0的时候，y为0，这就是**真值表**的第一行。

**获得权重项和偏置项**

感知器训练算法：将权重项和偏置项初始化为0，然后，利用下面的**感知器规则**迭代的修改wi和b，直到训练完成。

[![深度学习实战教程(一)：感知器](https://cuijiahua.com/wp-content/uploads/2018/10/dl-7-16.png)](https://cuijiahua.com/wp-content/uploads/2018/10/dl-7-16.png)

其中:

[![深度学习实战教程(一)：感知器](https://cuijiahua.com/wp-content/uploads/2018/10/dl-7-17.png)](https://cuijiahua.com/wp-content/uploads/2018/10/dl-7-17.png)

wi是与输入xi对应的权重项，b是偏置项。事实上，可以把b看作是值永远为1的输入xb所对应的权重。t是训练样本的**实际值**，一般称之为**label**。而y是感知器的输出值，它是根据**公式(1)**计算得出。η是一个称为**学习速率**的常数，其作用是控制每一步调整权的幅度。

每次从训练数据中取出一个样本的输入向量x，使用感知器计算其输出y，再根据上面的规则来调整权重。每处理一个样本就调整一次权重。经过多轮迭代后（即全部的训练数据被反复处理多轮），就可以训练出感知器的权重，使之实现目标函数。

```python
# 感知器训练学习
from functools import reduce


class Perceptron:
    def __init__(self, input_num, activator):
        """
        初始化感知器，设置输入参数的个数，以及激活函数。
        激活函数的类型为double -> double
        :param input_num: 输入参数的个数
        :param activator: 激活函数，接受一个double类型的输入，返回一个double类型的输出
        """
        self.activator = activator
        # 权重向量初始化为0
        # 用来存储感知器模型的权重参数。权重参数决定了每个输入特征对感知器输出的影响程度。
        # [0.0 for _ in range(input_num)] 这部分代码使用了列表推导式来创建一个包含
        # input_num 个元素的列表，并将每个元素初始化为0.0。这就构成了初始的权重向量
        self.weights = [0.0 for _ in range(input_num)]
        # 偏置项初始化为0
        self.bias = 0.0

    def __str__(self):
        """
        打印学习到的权重、偏置项
        :return: 学习到的权重和偏置项的字符串表示
        """
        return 'weights\t:%s\nbias\t:%f\n' % (self.weights, self.bias)

    def predict(self, input_vec):
        """
        输入向量，输出感知器的计算结果
        :param input_vec: 输入向量
        :return: 感知器的计算结果
        """
        # 把input_vec[x1,x2,x3...]和weights[w1,w2,w3,...]打包在一起
        # 变成[(x1,w1),(x2,w2),(x3,w3),...]
        # 然后利用map函数计算[x1*w1, x2*w2, x3*w3]
        # 最后利用reduce求和
        return self.activator(
            reduce(lambda a, b: a + b, list(map(lambda x, w: x * w, input_vec, self.weights)), 0.0) + self.bias)

    # iteration 是指训练迭代的次数
    def train(self, input_vecs, labels, iteration, rate):
        """
        输入训练数据：一组向量、与每个向量对应的label；以及训练轮数、学习率
        :param input_vecs: 输入向量的列表
        :param labels: 对应的标签列表
        :param iteration: 训练轮数
        :param rate: 学习率
        """
        for i in range(iteration):
            self._one_iteration(input_vecs, labels, rate)

    def _one_iteration(self, input_vecs, labels, rate):
        """
        一次迭代，把所有的训练数据过一遍
        :param input_vecs: 输入向量的列表
        :param labels: 对应的标签列表
        :param rate: 学习率
        """
        # 把输入和输出打包在一起，成为样本的列表[(input_vec, label), ...]
        # 而每个训练样本是(input_vec, label)
        samples = zip(input_vecs, labels)
        # 对每个样本，按照感知器规则更新权重
        for (input_vec, label) in samples:
            # 计算感知器在当前权重下的输出
            output = self.predict(input_vec)
            # 更新权重
            self._update_weights(input_vec, output, label, rate)

    def _update_weights(self, input_vec, output, label, rate):
        """
        按照感知器规则更新权重
        :param input_vec: 输入向量
        :param output: 感知器的输出
        :param label: 实际标签
        :param rate: 学习率
        """
        # 把input_vec[x1,x2,x3,...]和weights[w1,w2,w3,...]打包在一起
        # 变成[(x1,w1),(x2,w2),(x3,w3),...]
        # 然后利用感知器规则更新权重
        delta = label - output
        # 新权重 = 旧权重 + 学习率 * 误差 * 输入特征
        self.weights = list(map(lambda x, w: w + rate * delta * x, input_vec, self.weights))
        # 新偏置项 = 旧偏置项 + 学习率 * 误差
        self.bias += rate * delta
        print("权重更新")
        print(self.weights)
        print(self.bias)


def f(x):
    """
    定义激活函数f
    :param x: 输入值
    :return: 激活函数的输出值
    """
    return 1 if x > 0 else 0


def get_training_dataset():
    """
    基于and真值表构建训练数据
    :return: 输入向量列表和对应的标签列表
    """
    # 构建训练数据
    # 输入向量列表
    input_vecs = [[1, 1], [0, 0], [1, 0], [0, 1]]
    # 期望的输出列表，注意要与输入一一对应
    # [1,1] -> 1, [0,0] -> 0, [1,0] -> 0, [0,1] -> 0
    labels = [1, 0, 0, 0]
    return input_vecs, labels


def train_and_perceptron():
    """
    使用and真值表训练感知器
    :return: 训练好的感知器对象
    """
    # 创建感知器，输入参数个数为2（因为and是二元函数），激活函数为f
    p = Perceptron(2, f)
    # 训练，迭代10轮, 学习速率为0.1
    input_vecs, labels = get_training_dataset()
    p.train(input_vecs, labels, 10, 0.1)
    # 返回训练好的感知器
    return p


if __name__ == '__main__':
    # 训练and感知器
    and_perception = train_and_perceptron()
    # 打印训练获得的权重
    print(and_perception)
    # 测试
    print('1 and 1 = %d' % and_perception.predict([1, 1]))
    print('0 and 0 = %d' % and_perception.predict([0, 0]))
    print('1 and 0 = %d' % and_perception.predict([1, 0]))
    print('0 and 1 = %d' % and_perception.predict([0, 1]))
```

> 你可能已经看晕了，但是没办法，我们必须理解好这个才能往下走。

**感知器**可以被看作是机器学习中的一种基础模型，特别是在二分类问题中，它可以用于判断一个样本属于哪个类别。虽然感知器相对简单，但它展示了机器学习的几个重要概念和步骤:

1. 数据准备：与其他机器学习模型一样，使用感知器前需要准备训练数据。数据应该包括输入特征和对应的标签或类别，以便模型能够学习输入特征与输出之间的关系。
2. 特征权重和偏置项初始化：感知器的核心是为每个输入特征分配一个权重，并设置一个偏置项。初始时，可以随机初始化这些权重和偏置项。
3. 预测输出：对于给定的输入特征，感知器将计算加权和，并通过阈值函数（如阶跃函数）将结果映射到预测输出。这个预测输出可以被视为二分类的预测结果。
4. 计算损失：将感知器的预测输出与真实标签进行比较，计算损失或误差。常用的损失函数是均方误差（Mean Squared Error）或交叉熵损失（Cross Entropy Loss），具体选择取决于任务类型。
5. 参数更新：使用优化算法（如梯度下降），根据损失函数的梯度来调整感知器的权重和偏置项，以减小损失。这个过程被称为参数更新或模型训练。
6. 重复训练：重复进行步骤3到5，直到达到停止条件。停止条件可以是达到一定的训练轮数、达到一定的精度要求或损失函数收敛等。
7. 预测和评估：训练完成后，使用感知器对新样本进行预测，并评估模型的性能。常用的评估指标包括准确率、精确率、召回率和F1分数等。

> 这是与函数的图形化表示，我们通过跃阶函数将这条线的上方区域转化成1,下方转化称成0。
>
> ![深度学习实战教程(一)：感知器](https://cuijiahua.com/wp-content/uploads/2018/10/dl-7-14.png)
>
> 但是通过这个感知器，你无法实现以下的函数，异或函数（相同得0,不同得1），因为你找不到一条直线可以把圆形和叉分在两边。
>
> ![深度学习实战教程(一)：感知器](https://cuijiahua.com/wp-content/uploads/2018/10/dl-7-15.png)
>
### 线性单元

感知器有一个问题，当面对的数据集不是线性可分的时候，感知器规则可能无法收敛，这意味着我们永远也无法完成一个感知器的训练。为了解决这个问题，我们使用一个可导的线性函数来替代感知器的阶跃函数，这种感知器就叫做线性单元。线性单元在面对线性不可分的数据集时，会收敛到一个最佳的近似上。

为了简单起见，我们可以设置线性单元的激活函数f为：f(x)=x

这样的线性单元如下图所示：

![](https://cuijiahua.com/wp-content/uploads/2018/10/dl-8-2.png)

对比此前我们讲过的感知器

![](https://cuijiahua.com/wp-content/uploads/2018/10/dl-7-2.png)

这样替换了激活函数之后，线性单元将返回一个实数值而不是0,1分类。因此线性单元用来解决回归问题而不是分类问题。

当我们说模型时，我们实际上在谈论根据输入x预测输出y的算法。比如，x可以是一个人的工作年限，y可以是他的月薪，我们可以用某种算法来根据一个人的工作年限来预测他的收入。比如y：

y=h(x)=w∗x+b

函数h(x)叫做假设，而w、b是它的参数。我们假设参数w=1000，参数b=500，如果一个人的工作年限是5年的话，我们的模型会预测他的月薪为

y=h(x)=1000∗5+500=5500(元)

你也许会说，这个模型太不靠谱了。是这样的，因为我们考虑的因素太少了，仅仅包含了工作年限。如果考虑更多的因素，比如所处的行业、公司、职级等等，可能预测就会靠谱的多。我们把工作年限、行业、公司、职级这些信息，称之为特征。对于一个工作了5年，在IT行业，百度工作，职级T6这样的人，我们可以用这样的一个特征向量来表示他x=(5,IT,百度,T6)。既然输入x变成了一个具备四个特征的向量，相对应的，仅仅一个参数w就不够用了，我们应该使用4个参数w1,w2,w3,w4每个特征对应一个。这样，我们的模型就变成

y=h(x)=w1∗x1+w2∗x2+w3∗x3+w4∗x4+b

其中，x1对应工作年限，x2对应行业，x3对应公司，x4对应职级。

为了书写和计算方便，我们可以令w0等于b，同时令w0对应于特征w0。由于w0其实并不存在，我们可以令它的值永远为1。也就是说

b=w0∗x0其中x0=1

这样上面的式子就可以写成

y=h(x)=w1∗x1+w2∗x2+w3∗x3+w4∗x4+b=w0∗x0+w1∗x1+w2∗x2+w3∗x3+w4∗x4

我们还可以把上式写成向量的形式

y=h(x)=wTx(式1)

长成这种样子模型就叫做线性模型，因为输出y就是输入特征x1,x2,x3,...的线性组合。

## 实现线性单元

```python
from perceptron import Perceptron
#定义激活函数f
f = lambda x: x
class LinearUnit(Perceptron):
    def __init__(self, input_num):
        '''初始化线性单元，设置输入参数的个数'''
        Perceptron.__init__(self, input_num, f)

def get_training_dataset():
    '''
    捏造5个人的收入数据
    '''
    # 构建训练数据
    # 输入向量列表，每一项是工作年限
    input_vecs = [[5], [3], [8], [1.4], [10.1]]
    # 期望的输出列表，月薪，注意要与输入一一对应
    labels = [5500, 2300, 7600, 1800, 11400]
    return input_vecs, labels    
def train_linear_unit():
    '''
    使用数据训练线性单元
    '''
    # 创建感知器，输入参数的特征数为1（工作年限）
    lu = LinearUnit(1)
    # 训练，迭代10轮, 学习速率为0.01
    input_vecs, labels = get_training_dataset()
    lu.train(input_vecs, labels, 10, 0.01)
    #返回训练好的线性单元
    return lu
if __name__ == '__main__': 
    '''训练线性单元'''
    linear_unit = train_linear_unit()
    # 打印训练获得的权重
    print(linear_unit)
    # 测试
    print('Work 3.4 years, monthly salary = %.2f' % linear_unit.predict([3.4]))
    print('Work 15 years, monthly salary = %.2f' % linear_unit.predict([15]))
    print('Work 1.5 years, monthly salary = %.2f' % linear_unit.predict([1.5]))
    print('Work 6.3 years, monthly salary = %.2f' % linear_unit.predict([6.3]))

```

拟合的直线如下图

![](https://cuijiahua.com/wp-content/uploads/2018/11/dl-8-7.png)

事实上，一个机器学习算法其实只有两部分

模型从输入特征x预测输入y的那个函数h(x)
目标函数 目标函数取最小(最大)值时所对应的参数值，就是模型的参数的最优值。很多时候我们只能获得目标函数的局部最小(最大)值，因此也只能得到模型参数的局部最优值。
因此，如果你想最简洁的介绍一个算法，列出这两个函数就行了。

接下来，你会用优化算法去求取目标函数的最小(最大)值。随机梯度{下降|上升}算法就是一个优化算法。针对同一个目标函数，不同的优化算法会推导出不同的训练规则。我们后面还会讲其它的优化算法。

其实在机器学习中，算法往往并不是关键，真正的关键之处在于选取特征。选取特征需要我们人类对问题的深刻理解，经验、以及思考。而神经网络算法的一个优势，就在于它能够自动学习到应该提取什么特征，从而使算法不再那么依赖人类，而这也是神经网络之所以吸引人的一个方面。

