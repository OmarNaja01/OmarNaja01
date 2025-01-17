# -*- coding: utf-8 -*-
"""01_Linear_Regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pzjceldxJ7abb3eLf5pt82z1fwD_6HG-

# Linear Regression

Let us consider the [iris dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set).

In the dataset we have data regarding specific species of flowers :
- Sepal length;
- Sepal width;
- Petal length;
- Petal width;
- Species (*Iris setosa*, *Iris virginica* e *Iris versicolor*).

In the specific, we have N = 150 total samples (50 per class).

<img src='https://drive.google.com/uc?id=1cBVClKfJOVXwK-VCjwd9XzRgCN-wvec_' width=250>

## Loading

We need to import **matplotlib** and **pandas** to handle data and plots.
"""

import pandas as pd #https://pandas.pydata.org/
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

"""We can find the dataset we need to analyse online. We use pandas to load the csv to a **pandas.DataFrame**."""

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)

"""We can start to have a look the data we have"""

dataset.head()

"""we do not care about the flower species in this lesson, hence we remove that column:"""

dataset = dataset.drop('class', axis=1)

dataset.head()

"""We will try to understand how the feature are distributed, by printing some statistics:"""

dataset.describe()

"""Visualizing data can also be very helpful:"""

dataset.hist(figsize=(16,9))
plt.show()

scatter_matrix(dataset, figsize=(16, 9))
plt.show()

"""*petal-lenght* and *petal-width* seem to have a strong relationship... we should investigate it more in detail!"""

dataset.plot.scatter('petal-length', 'petal-width', grid=True, figsize=(16,9))

"""## Preprocessing

Once we inspected the data, we should operate some preprocessing procedures. On a
generic dataset one should perform:

- shuffling;
- remove inconsistent data;
- remove outliers;
- normalize or standardize data;
- fill missing data.

In this case we are going to use the entire dataset, with a non-iterative method, hence we do not need to **shuffle**.

There seems not to be **outliers** from previous inspection.

Is there any **missing data**?
"""

import numpy as np #https://numpy.org/

np.any(np.isnan(dataset.values))

"""we are lucky, no missing data, no outliers...

However it is always better to work with data in the same scale, hence we should normalize the columns we are going to use.

\begin{align*}
	s &\leftarrow \frac{s - \bar{s}}{S} \\
	s &\leftarrow \frac{s - \min_n \{ s_n \}}{\max_n \{ s_n \} - \min_n \{ s_n \}}
\end{align*}

The **zscore** function operates a standardization of its inputs.
"""

from scipy.stats import zscore #https://scipy.org/

x = zscore(dataset['petal-length'].values).reshape(-1, 1) # we reshape our feature column as a (n_sample, n_features) matrix
y = zscore(dataset['petal-width'].values)

np.std(x)

"""## Using Scikit-Learn Toolbox

A linear model seems to be a good choice to predict *petal-width* given petal-length, let's use **scikit-learn** tools to do a linear regression:
"""

from sklearn import linear_model #https://scikit-learn.org/stable/

lin_model = linear_model.LinearRegression()
lin_model.fit(x, y)

lin_model.coef_

lin_model.intercept_

"""since we want to customize our plot, we will use matplotlib directly this time:"""

with plt.style.context('seaborn'): # use your favorite style, if you don't like the standard one
  plt.figure(figsize=(16,9))
  plt.scatter(x, y, label='true')

  w1 = lin_model.coef_ # weights of the model are stored here
  w0 = lin_model.intercept_ # and here it is the intercept

  # Compute the y component of the regression line

  y_pred = lin_model.predict(x)
  #y_pred = [w1 * sample + w0 for sample in x.flatten()]

  # (we used a list comprehension here, have a look to the python tutorial
  #  if you don't know what it is!)

  plt.plot(x, y_pred, label='predicted', color='red')

  # enlarging fonts
  plt.legend(prop={'size': 20})
  plt.xticks(fontsize=20)
  plt.yticks(fontsize=20)

  plt.show()

"""To evaluate the quality of our regression we can analyse some metrics:"""

from sklearn.metrics import mean_squared_error, r2_score

"""### Residual Sum of Squares

$RSS = \sum_n (\hat{t}_n-t_n)^2$, it tells us how much of the prediction differs from the true value.
"""

RSS = np.sum((y_pred-y)**2)
RSS

"""### Coefficient of determination

$R^2 = 1 - \frac{RSS}{\sum_n (\bar{t}-t_n)^2}$, it tells us how the fraction of the variance of the data explained by the model (how much better we are doing w.r.t. just using the mean of the target $\bar{t} = \frac{\sum_n t_n}{N}$).

In spaces with a single feature this is equal to the correlation coefficient between the input and the output;

For a more detailed explanation: https://en.wikipedia.org/wiki/Coefficient_of_determination
"""

r2_score(y, y_pred)

"""### Mean Squared Error

$MSE = \frac{\sum_n (\hat{t}_n-t_n)^2}{N}$, it tells approximately how much error we get on a predicted data over the training set (i.e., a normalized version of the RSS).
"""

mean_squared_error(y, y_pred)

"""Under the assumption that the observations $t_n$ are i.i.d. and satisfies $t_n = w_0 + \sum_j w_j x_{nj} + \epsilon$, where $\epsilon$ is a Gaussian noise with zero mean and variance $\sigma^2$ (i.e., the data are generated by a linear model with noise), the computed coefficients $\hat{w}_j$ are distributed as follows:
\begin{equation*}
	\frac{\hat{w}_j - w_j}{\hat{\sigma} \sqrt{v_j}} \sim t_{N - M -1}
\end{equation*}
where $w_j$ is the true parameter, $\hat{\sigma}$ is the unbiased estimated for the target variance, i.e., $\hat{\sigma}^2 = \frac{\sum_n (t_n - \hat{t}_n)^2}{N - M - 1}$, $v_j$ is the $j$-th diagonal element of the matrix $(X^T X)^{-1}$ and $t_{N - M-1}$ is the t-student distribution with $N - M - 1$ degrees of freedom.

This allow us to formulate some **statistical tests**:

### Single coefficients statistical test:
$$H_0: w_j = 0 \qquad \text{ vs. } \qquad H_1: w_j \neq 0$$
\begin{equation*}
t_{stat} = \frac{\hat{w}_j - w_j}{\hat{\sigma} \sqrt{v_j}} \sim t_{N - M - 1}
\end{equation*}
where $t_{N - M - 1}$ is the T-Student distribution with $N-M-1$ degrees of freedom

### Overall significance of the model: F-statistic

It considers the following hypothesis test:

$$H_0: w_1 = \dots = w_M = 0 \text{ vs. }  H_1: \exists w_j \neq 0$$


The F-statistic can be computed and is distributed as follows:
$$ F = \frac{dfe}{M }\frac{\sum_n (\overline{t}_n-t_n)^2- RSS}{RSS} \sim F_{M, N-M-1} $$

where $F_{M, N-M-1}$ is the Fisher-Snedecor distribution with parameters $M$ and $N-M-1$.
"""

from sklearn.feature_selection import f_regression

f_regression(x, y) # it outputs a tuple: (value of the F-statistics, its p-value)

"""If one wants all the information about the output of a linear model in a single instruction, just use the library **statsmodels** and use the function **summary()** on the result of the Ordinary Least Square optimization procedure"""

from statsmodels import api as sm
lin_model2 = sm.OLS(y, x).fit()
print(lin_model2.summary())

lin_model2._results.params

lin_model2._results.k_constant

"""## Custom Implementation

We can also implement Least-Squares from scratch, using its closed-form:

\begin{equation}
\hat{\mathbb{w}}_{OLS} = (\mathbb{\Phi}^{\top}\mathbb{\Phi})^{-1}\mathbb{\Phi}^{\top}\ \mathbb{t},
\end{equation}

where $\mathbb{\Phi}= (\phi(x_1), \dots, \phi(x_N))^{\top}$ and $\mathbb{t} = (t_1, \dots, t_N)^{\top}.$

By using **numpy**:

"""

from numpy.linalg import inv

n_samples = len(x)
Phi = np.ones((n_samples, 2))
Phi[:, 1] = x.flatten() # the second column is the feature
# the field 'T' represents the transposed matrix, @ is the matrix product, the method 'dot' is the matrix product
w = inv(Phi.T @ Phi) @ (Phi.T.dot(y))

w

"""## Regularization

If we need to mitigate over-fitting effects in a model we might resort to some regularization techniques, like Ridge regression or Lasso regression.

### Ridge Regression
Linear least squares with l2 regularization.
"""

ridge_model = linear_model.Ridge(alpha=10)
ridge_model.fit(x, y)

"""### Lasso Regression

Linear Model trained with L1 prior as regularizer.
"""

lasso_model = linear_model.Lasso(alpha=10)
lasso_model.fit(x, y)

with plt.style.context('seaborn'):
  plt.figure(figsize=(16,9))
  plt.scatter(x, y, label='original samples')
  y_linear = [lin_model.coef_ * x_i + lin_model.intercept_ for x_i in x]
  plt.plot(x, y_linear, label='linear regression', color='red')
  for alpha in [0.1, 0.2, 0.5]:
    # lasso regression
    lasso_model = linear_model.Lasso(alpha=alpha)
    lasso_model.fit(x, y)
    y_lasso = [lasso_model.coef_ * x_i + lasso_model.intercept_ for x_i in x]
    plt.plot(x, y_lasso, label='lasso, alpha={}'.format(alpha))


  # enlarging fonts
  plt.legend(prop={'size': 20})
  plt.xticks(fontsize=20)
  plt.yticks(fontsize=20)

  plt.show()

mean_squared_error(y, lasso_model.predict(x))

"""## Homeworks

Here we propose some exercises in python for you. They are not mandatory, but they can be helpful to better understand the contents of the lecture, by giving you the opportunity to develop some code by yourself.

### 1) Predicting petal width

Consider again the Iris dataset, and complete the following code, by writing a script which is able to predict the petal width by using, this time, **all** the other features as input.
"""

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)

# Get input and output
x =  ... ### WRITE YOUR CODE HERE
y = zscore(dataset['petal-width'].values)

# Fit your model
### WRITE YOUR CODE HERE ###

"""Comment on the parameters we would like to introduce or exclude from the prediction process.

Does this model is better than the one trained with a single input?

How do you check if the two models are significantly different from each other?

*(hint: look at the exercise session on Bias-Variance tradeoff)*

### 2) Implementing closed-form ridge regression
Ridge regression can be obtained in closed form, as we have seen at lesson. Implement it by yourself, by completing the code below.
"""

alpha = 100
ridge_model = linear_model.Ridge(alpha=alpha)
ridge_model.fit(x, y)


w = ...  ### WRITE YOUR CODE HERE ###

# Compare your solution it with the scikit-learn one!
assert np.isclose(w, ridge_model.coef_), 'Something wrong!, try again...'

"""### 3) Implementing LS for multiple outputs

We have seen at lesson that LS is possible also when we have multiple outputs.

Implement it by extending the LS custom implementation that we have seen.
"""

### WRITE YOUR CODE HERE ###

"""### 4) Try it on another dataset

Try to repeat the procedure that we have seen for the Iris dataset on a new dataset of your choice:

- select a dataset (many are available online, e.g. https://www.kaggle.com/datasets)
- visualize data, in order to spot interesting relationships
- preprocess data
- apply linear regression
"""

### WRITE YOUR CODE HERE ###