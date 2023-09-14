#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 09:00:02 2023

@author: anoushkajawale
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#reading and viewing data 
pulsar_data_train = pd.read_csv("pulsar_data_train.csv")
print(pulsar_data_train.columns)
print(pulsar_data_train.index)
print(pulsar_data_train.head())
print(pulsar_data_train.tail())
print(pulsar_data_train.describe(include='all'))
#decising which visualization technique is best 
print(pulsar_data_train.dtypes) #all are float64 continuous values, indicating a histogram can be used to visualize the features

#feature visualization
for col in pulsar_data_train.columns : 
    fig, axs = plt.subplots(figsize=(22, 9))
    sns.histplot(data=pulsar_data_train, x=col, hue="target_class")


#finding missing value counts per column 
print(pulsar_data_train.isnull().sum())
#percentage of missing values within train dataset 
print(pulsar_data_train.isnull().sum()/len(pulsar_data_train)*100)
#excess kurtosis of the integrated profile and standard deviation of the DN-SNR curve have the highest outlier percentage

#using iterative imputer to fill in the missing values 
imputer = IterativeImputer(max_iter=10, random_state=1)
imputed_data = pd.DataFrame(imputer.fit_transform(pulsar_data_train), columns=pulsar_data_train.columns.values.tolist())

print(imputed_data.isnull().sum()) #now there are no null values 


#outlier detection and revisualization 

for feature in imputed_data.columns: 
    fig, axis = plt.subplots(figsize=(22, 9))
    fig.suptitle(feature, fontsize=30)
    sns.histplot(data=imputed_data, x=feature, hue="target_class")

for feature in imputed_data.columns : 
    fig, axis = plt.subplots(figsize=(22, 9))
    fig.suptitle(feature, fontsize=30)
    sns.boxplot(data=imputed_data, x="target_class", y=feature)

#based on above: 
#integrated profile: 
    #mean of the integrated profile - higher mean for non pulsars, as well as more outliers. Pulsars have no considered outliers.
    #This indicates that non-pulsars on average emit a higher average intensity of observed signal. 
    #standard deviation of the integrated profile - non-pulsars have a higher standard deviation, as well as tails and outliers. Pulsars also contain outliers 
    #excess kurtosis - non-pulsars have a smaller distribution as well as more outliers than pulsars. 
    #skewness of integrated profile - non-pulsars have a much smaller distribution, but much higher sjew values which pulsars have a larger distribution 


#outlier handling/treatment
#first finding how many outliers by percentage each column contains: 

Q1 = pulsar_data_train.quantile(0.25)
Q3 = pulsar_data_train.quantile(0.75)
print(Q1[' Mean of the integrated profile'])
IQR = Q3 - Q1
lower_bound =Q1-(1.5*IQR)
upper_bound = Q3+(1.5*IQR)
print("Outliers by percentage:")
print(((imputed_data < (lower_bound)) | (imputed_data > (upper_bound))).sum()/len(imputed_data)*100)

#capping outliers 
imputed_out = imputed_data.copy()
print(imputed_out[' Mean of the integrated profile'])
#looping through all columns excluding  target class
for col in imputed_out.columns[:-1]:
  imputed_out[col] = np.where(imputed_out[col]>upper_bound[col],upper_bound[col],imputed_out[col])
  imputed_out[col] = np.where(imputed_out[col]<lower_bound[col],lower_bound[col],imputed_out[col])

#comparing box plots of before and after outlier capping
cols = list(imputed_data.columns)
imputed_data.boxplot(vert=0, column=cols)

imputed_out.boxplot(vert=False, column=cols)
plt.xlim(-200, 1000)

#for feature selection, visualizing heatmap after outlier treatment
corr_matrix=imputed_out.corr()
plt.figure(figsize=(10, 10))
sns.heatmap(corr_matrix, annot=True)

#from the heatmap, ###features are highly correlated features with too many missing values and outliers were removed 
final_data = imputed_out.drop([' Excess kurtosis of the integrated profile', 
                                     ' Skewness of the DM-SNR curve', 
                                     ' Standard deviation of the DM-SNR curve'],axis=1)

#splitting data for training 

x = final_data.drop(['target_class'], axis=1)
y = final_data['target_class']


#splitting data 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=20)
model = LogisticRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print(accuracy_score(y_test, y_pred)) #accuracy 0.97
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))













