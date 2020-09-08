# -*- coding: utf-8 -*-
"""project  final copy

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CYcqpegsppC_bS4w4OLbS-WzCLBUcKQd
"""

import numpy as np
import pandas as pd

train = pd.read_csv('/content/sample_data/train.csv')
test = pd.read_csv('/content/sample_data/test.csv')
feature = pd.read_csv('/content/sample_data/features.csv')
store = pd.read_csv('/content/sample_data/stores.csv')



train.head(2)

store.head(2)

feature.head(2)

train = train.merge(feature).merge(store)
train.head(2)

train.info()

import matplotlib.pyplot as plt

plot = plt.figure(figsize=(18, 14))
corr = train.corr()
c = plt.pcolor(corr)
plt.yticks(np.arange(0.5, len(corr.index), 1), corr.index)
plt.xticks(np.arange(0.5, len(corr.columns), 1), corr.columns)
plot.colorbar(c)

import seaborn as sns

sns.pairplot(train, vars=['Weekly_Sales', 'Fuel_Price', 'Size', 'CPI', 'Dept', 'Temperature', 'Unemployment'])

plt.figure(figsize=(12,6))
sns.distplot(train['Weekly_Sales'], color='y')
plt.legend(['Weekly_Sales'], loc='best', fontsize=16)
plt.show()

sns.countplot(train['IsHoliday'])

sns.countplot(train['Type'])

corr_matrix = train.corr()
corr_df = corr_matrix['Weekly_Sales'].sort_values(ascending = False)
corr_df

type = pd.get_dummies(train['Type'], prefix = 'Type')
type.head(2)

train = pd.concat([train, type], axis=1)
train.head(3)

train['Date'] = pd.to_datetime(train['Date'])
train['Day'] = train['Date'].dt.day
train['Month'] = train['Date'].dt.month
train['Year'] = train['Date'].dt.year

train.info()

train.drop('Date', axis=1, inplace=True)

train.drop('Type', axis=1, inplace=True)

train.isna().sum()

train.fillna(value=0, inplace=True)

train.isna().sum()

corr_matrix = train.corr()
corr_df = corr_matrix['Weekly_Sales'].sort_values(ascending = False)
corr_df

plt.figure(figsize=(16,8))
sns.heatmap(train.corr(), annot=True)
plt.show()

train.drop(['Unemployment','Fuel_Price'], axis=1, inplace=True)

x= train.drop('Weekly_Sales', axis=1).values

y = train['Weekly_Sales'].values

from sklearn.model_selection import train_test_split

train_x,test_x,train_y,test_y = train_test_split(x,y,test_size=0.3,random_state=100)

train_x

train_y

from sklearn.metrics import mean_absolute_error, mean_squared_error

from sklearn.linear_model import LinearRegression

linear = LinearRegression()
linear.fit(train_x, train_y)
pred_linear_y = linear.predict(test_x)

linear_score=linear.score(test_x, test_y)*100
linear_score

mse_linear = np.sqrt(mean_squared_error(test_y,pred_linear_y))
mse_linear

mae_linear = mean_absolute_error(test_y,pred_linear_y)
mae_linear

print('Accuracy Score:',linear_score)
print('Root Mean Square Error: ', mse_linear)
print('Mean Absolute Error: ', mae_linear)

plt.scatter(test_y, pred_linear_y)
plt.show()

from sklearn.neighbors import KNeighborsRegressor

knn = KNeighborsRegressor(n_neighbors=9)
knn.fit(train_x, train_y)
pred_knn_y = knn.predict(test_x)
score_knn=knn.score(test_x, test_y)
score_knn=score_knn*100

mse_knn = np.sqrt(mean_squared_error(test_y,pred_knn_y))
mse_knn

mae_knn = mean_absolute_error(test_y,pred_knn_y)
mae_knn

plt.scatter(test_y, pred_knn_y)
plt.show()

print('Accuracy Score:', score_knn)
print('Root Mean Square Error: ', mse_knn)
print('Mean Absolute Error: ', mae_knn)

from sklearn.ensemble import ExtraTreesRegressor

etg = ExtraTreesRegressor(n_estimators=100,max_features='auto', verbose=1, n_jobs=1)
etg.fit(train_x, train_y)
pred_etg_y = etg.predict(test_x)

score_etg=etg.score(test_x, test_y)
score_etg=score_etg*100
mse_etg = np.sqrt(mean_squared_error(test_y,pred_etg_y))
mae_etg = mean_absolute_error(test_y,pred_etg_y)
score_etg

plt.scatter(test_y, pred_etg_y)
plt.show()

print('Accuracy Score:', score_etg)
print('Root Mean Square Error: ', mse_etg)
print('Mean Absolute Error: ', mae_etg)

from sklearn.ensemble import RandomForestRegressor

rfg = RandomForestRegressor(n_estimators=100,max_features='log2', verbose=1)
rfg.fit(train_x, train_y)
pred_rfg_y = rfg.predict(test_x)

score_rfg=rfg.score(test_x, test_y)
score_rfg=score_rfg*100
mse_rfg = np.sqrt(mean_squared_error(test_y,pred_rfg_y))
mae_rfg = mean_absolute_error(test_y,pred_rfg_y)
score_rfg

plt.scatter(test_y, pred_rfg_y)
plt.show()

print('Accuracy Score:', score_rfg)
print('Root Mean Square Error: ', mse_rfg)
print('Mean Absolute Error: ', mae_rfg)

"""**XGBoost Regressor**"""

import xgboost as xgb

reg = xgb.XGBRegressor(n_estimators=500)
reg.fit(train_x, train_y)
pred_reg_y = reg.predict(test_x)

score_reg=reg.score(test_x, test_y)
score_reg=score_reg*100
mse_reg = np.sqrt(mean_squared_error(test_y,pred_reg_y))
mae_reg = mean_absolute_error(test_y,pred_reg_y)

plt.scatter(test_y, pred_reg_y)
plt.show()

print('Accuracy Score:', score_reg)
print('Root Mean Square Error: ', mse_reg)
print('Mean Absolute Error: ', mae_reg)

!pip install catboost
from catboost import CatBoostRegressor

cbr = CatBoostRegressor()
cbr.fit(train_x, train_y)
pred_cbr_y = cbr.predict(test_x)

score_cbr=cbr.score(test_x, test_y)
score_cbr=score_cbr*100
mse_cbr = np.sqrt(mean_squared_error(test_y,pred_reg_y))
mae_cbr = mean_absolute_error(test_y,pred_reg_y)

plt.scatter(test_y, pred_cbr_y)
plt.show()

print('Accuracy Score:', score_cbr)
print('Root Mean Square Error: ', mse_cbr)
print('Mean Absolute Error: ', mae_cbr)

algorithms = ['Linear Regression', 'KNN', 'Extra Tree Regressor', 'Random Forest Regressor', 'XGBoost', 'catBoostRegresor']
rmse = [mse_linear, mse_knn, mse_etg, mse_rfg, mse_reg, mse_cbr]
mae = [mae_linear, mae_knn, mae_etg, mae_rfg, mae_reg, mae_cbr]
score = [linear_score, score_knn, score_etg, score_rfg, score_reg, score_cbr]

plt.figure(figsize=(16, 6))
sns.barplot(algorithms, rmse)

plt.figure(figsize=(16, 6))
sns.barplot(algorithms, mae)

plt.figure(figsize=(16, 6))
sns.barplot(algorithms, score)

test = pd.read_csv('/content/sample_data/test.csv')
test=test.merge(feature, how='left').merge(store, how='left')

type_test = pd.get_dummies(test['Type'], prefix = 'Type')
type_test.head(2)

test[['MarkDown1','MarkDown2','MarkDown3','MarkDown4', 'MarkDown5']] = test[['MarkDown1','MarkDown2','MarkDown3','MarkDown4','MarkDown5']].fillna(0)
test = test.fillna(0)
column_date =  test['Date']

test['Date'] = pd.to_datetime(test['Date'])
test['Day'] = test['Date'].dt.day
test['Month'] = test['Date'].dt.month
test['Year'] = test['Date'].dt.year

test.info()

test = pd.concat([test, type_test], axis=1)
test.head(3)

test.info()

test.drop('Date', axis=1, inplace=True)

test.drop('Type', axis=1, inplace=True)

test.info()

test.drop(['Unemployment','Fuel_Price'], axis=1, inplace=True)

prediction = etg.predict(test)

test.isna().sum()

prediction = prediction.round(2)
prediction

test['Weekly_Sales'] = prediction
test['Date'] = column_date
test['id'] = test['Store'].astype(str) + '_' +  test['Dept'].astype(str) + '_' +  test['Date'].astype(str)
test = test[['id', 'Weekly_Sales']]
test = test.rename(columns={'id': 'Id', 'Weekly_Sales': 'Weekly_Sales'})

test.to_csv('/content/sample_data/output.csv', index=False)

op = pd.read_csv('/content/sample_data/output.csv')

op.head()

