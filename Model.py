'''
Created July 9th 2020:
author: Artem Moshkin
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('/home/artem/PycharmProjects/Data Science Job Project/PostEDAData.xlsx')

#Picking the relevant columns and creating dummy variables
df_model = df[['avg_salary','Rating', 'Size', 'Type of ownership', 'Industry', 'Sector', 'Revenue', 'hourly', 'employer_provided', 'NumberComp', 'State', 'SimpJob', 'agecompany', 'python', 'Excel', 'Senior']]
df_dummies = pd.get_dummies(df_model)

#Train and Test Split:
from sklearn.model_selection import train_test_split

X= df_dummies.drop('avg_salary', axis=1)
y= df_dummies.avg_salary.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
#Multiple Linear Regressions
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_absolute_error

#Lasso Regression
las = Lasso()
las.fit(X_train,y_train)
print('Lasso Regression Train Score:')
print(np.mean(cross_val_score(las, X_train, y_train, scoring='neg_mean_absolute_error', cv=3)))
print('\n')
alpha = []
error = []

for i in range(1, 100):
    alpha.append(i/100)
    las2 = Lasso(alpha=(i/100))
    error.append(np.mean(cross_val_score(las2, X_train, y_train, scoring='neg_mean_absolute_error', cv=3)))

#plt.plot(alpha,error)

errortup = tuple(zip(alpha,error))
df_error = pd.DataFrame(errortup, columns=['alpha', 'error'])

lassoalpha = df_error[df_error.error == max(df_error.error)]['alpha']

lasso = Lasso(alpha=0.06)
lasso.fit(X_train, y_train)

#Random Forest

forest = RandomForestRegressor()
forest.fit(X_train, y_train)
print('Forest Regression Train Score:')
print(np.mean(cross_val_score(forest, X_train, y_train, scoring='neg_mean_absolute_error', cv=3)))
print('\n')

#Gradient Boosted Tree

grad = GradientBoostingRegressor()
grad.fit(X_train, y_train)
print('Gradient Regressor Train Score:')
print(np.mean(cross_val_score(grad, X_train, y_train, scoring='neg_mean_absolute_error', cv=3)))
print('\n')

#Tune Models using GridSearchCV for Random Forest:
from sklearn.model_selection import GridSearchCV
params = {'n_estimators': range(10, 300, 10), 'criterion': ('mse', 'mae'), 'max_features': ('auto', 'sqrt', 'log2')}

#GS = GridSearchCV(forest, params, scoring='neg_mean_absolute_error', cv=3)
#GS.fit(X_train, y_train)
#print(GS.best_score_)
#print(GS.best_estimator_)

forest = RandomForestRegressor(n_estimators=120, criterion='mae', max_features='auto')
forest.fit(X_train, y_train)

#Test Ensembles
tpred_las = las.predict(X_test)
tpred_forest = forest.predict(X_test)
t_pred_grad_forest = grad.predict(X_test)

print('Lasso Test Score:')
print(mean_absolute_error(y_test, tpred_las))
print('\n')
print('Forest Test Score:')
print(mean_absolute_error(y_test, tpred_forest))
print('\n')
print('Gradiant Forest Test Score:')
print(mean_absolute_error(y_test, t_pred_grad_forest))
print('\n')
print('85% Forest and 15% Gradient Forest Test Score:')
print(mean_absolute_error(y_test, (tpred_forest*.85+ t_pred_grad_forest*.15)))

import pickle
pickl ={'model': forest}
pickle.dump( pickl, open( 'model_file' + ".p", "wb") )

file_name = 'model_file.p'

with open(file_name, 'rb') as pickled:
    data = pickle.load(pickled)
    model = data['model']

#print(model.predict(X_test.iloc[1,:].values.reshape(1,-1)))

print(list(X_test.iloc[1,:]))