# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#importing libraries
import numpy
import matplotlib.pyplot as plot
import pandas

#importing data sheets
dataset = pandas.read_csv('C:/Users/jhays/Desktop/machine-learning/P14-Machine-Learning-AZ-Template-Folder/Machine Learning A-Z Template Folder/Part 1 - Data Preprocessing/data.csv');
X = dataset.iloc[:, :-1].values;
Y = dataset.iloc[:, 3].values;
