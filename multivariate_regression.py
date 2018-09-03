#####		MULTIPLE LINEAR REGRESSION

import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

## importing the dataset
df = pd.read_csv('50_Startups.csv')

## classifying features and labels
X = np.array(df.drop(['Profit'], 1))
y = np.array(df['Profit'])

## encoding - categorical data 
# its the 3rd column that requires encoding - 3 categories
from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()
# labelencoder_X.fit_transform(X[:,3])
X[:,3] = labelencoder_X.fit_transform(X[:,3])

## dummy encoding - one hot encoder
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features=[3])		#categorical_features[indices of the columm you want to onehot vectorise]
X = onehotencoder.fit_transform(X).toarray()

## -------------------------------------------------------------
## Avoiding the dummy variable trap as its a multiple linear regression
X = X[:, 1:] 	## droped the first column to avoid dummy variable trap

## -------------------------------------------------------------

## train and test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/5, random_state=0)
print(y_test.astype(int))
	
## fitting multiple linear regression model to training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

## predicting the Test results
y_predict = regressor.predict(X_test)
print(y_predict.astype(int))
# results are not that satisfactory. Hence, the model can be imporved

## accuracy 
accuracy = regressor.score(X_test, y_test)
print('accuracy: {}'.format(accuracy))





























