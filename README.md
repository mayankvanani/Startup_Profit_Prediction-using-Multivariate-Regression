# Startup_Profit_Prediction_using_Multivariate_Regression
Given the Dataset _'50_Startups'_  is the dataset of 50 startups in US and its various expenditure on Administration and  Marketing and the location  where the startup is based on.

## OBJECTIVE
We need to draw out a model that can predict the profitability of any future Startup given the input parameters same as above.

## Multivariate Regression
- Accuracy = **93.14%**

## Improving Model - Significance Test
- Algorithm = **Backward Elimination**
- Library = **statsmodels**
- Monitoring and eliminating the parameters with **p-values > 0.5** 

**NOTE**: The statsmodel library operates on multivariate regression witht different initial condition. <br/>
Equation of multivariate regression is: <br/>
**y = b<sub>sub0</sub>*x<sub>0</sub> + b<sub>1</sub>*x<sub>1</sub> + b<sub>2</sub>*x<sub>2</sub> + .... + b<sub>n</sub>*x<sub>n</sub>**. <br/>
But, the equation of multivariate rergession for **statsmodels** is: <br/>
**y = b<sub>sub0</sub>*x<sub>0</sub> + b<sub>1</sub>*x<sub>1</sub> + b<sub>2</sub>*x<sub>2</sub> + .... + b<sub>n</sub>*x<sub>n</sub>**. <br/>

Here there is **no considereation for constant**. So _x0_ can be made such that x0 = 1. As a result, **b<sub>0</sub>** will behave as constant.
