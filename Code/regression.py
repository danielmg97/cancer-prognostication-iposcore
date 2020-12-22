# -*- coding: utf-8 -*-
"""[Regr] DEFAULT

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cJFL-qaQV8F5wqEYVntks0EOi4VlsWyu
"""

import warnings
warnings.filterwarnings("ignore")

import math
import numpy as np
import pandas as pd
import global_variables
import load_and_run

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.linear_model import ElasticNet
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import PolynomialFeatures
from xgboost import XGBRegressor
from sklearn.cross_decomposition import PLSRegression
from sklearn.neural_network import MLPRegressor

OUTPUT = global_variables.outputs[2]    ##### IMPORTANTE ALTERAR #####
n_outputs = 7                           ##### IMPORTANTE ALTERAR #####

import sys

orig_stdout = sys.stdout
f = open("REG-results_"+OUTPUT+"(DRN).txt", 'w')
sys.stdout = f

# Use this to use all the variables
variables = global_variables.binarias+global_variables.categoricas+global_variables.numericas

# Use this for variable selection
# variables = ['ARISCAT procedimento emergente', 'ARISCAT anemia pré-operativa', 'morte (%)', 'pneumonia (%)', 'complicações sérias (%)', 'ACS - previsão dias internamento', 'qualquer complicação (%)', 'Discharge to Nursing or Rehab Facility (%)', '% mortalidade P-Possum', 'falência renal (%)', 'complicações cardíacas (%)', 'reoperação (%)', '% morbilidade P-Possum', 'tromboembolismo venoso (%)', 'Score gravidade cirúrgica P-Possum', 'Score fisiológico P-Possum', 'readmissão (%)', 'risco médio.11', 'ITU (%)', 'ARISCAT PONTUAÇÃO TOTAL', 'risco médio.12', 'risco médio', 'risco médio.1', 'risco médio.13', 'infeção cirúrgica (%)', 'risco médio.4', 'SCORE ARISCAT', 'risco médio.7']

dataset = load_and_run.load_data(OUTPUT,variables)
dataset.dropna(how="any",subset=dataset.columns[[-1]], inplace=True) #this is a bug fix

headers = dataset.columns
to_dummify = []
for i in range(0,len(headers)):
  if headers[i] in global_variables.categoricas:
    to_dummify.append(i)

dataset = dataset.to_numpy()

print("*** Linear ***")
load_and_run.reg_k_fold(LinearRegression(),dataset,headers,to_dummify,n_outputs)

print("*** Ridge ***")
load_and_run.reg_k_fold(Ridge(),dataset,headers,to_dummify,n_outputs)

print("*** Lasso ***")
load_and_run.reg_k_fold(linear_model.Lasso(),dataset,headers,to_dummify,n_outputs)

print("*** SVM ***")
load_and_run.reg_k_fold(svm.SVR(),dataset,headers,to_dummify,n_outputs)

print("*** Elastic ***")
load_and_run.reg_k_fold(ElasticNet(random_state=0),dataset,headers,to_dummify,n_outputs)

print("*** KNN ***")
load_and_run.reg_k_fold(KNeighborsRegressor(),dataset,headers,to_dummify,n_outputs)

print("*** DT ***")
load_and_run.reg_k_fold(DecisionTreeRegressor(random_state=0),dataset,headers,to_dummify,n_outputs)

print("*** RF ***")
load_and_run.reg_k_fold(RandomForestRegressor(random_state=0),dataset,headers,to_dummify,n_outputs)

print("*** XGB ***")
load_and_run.reg_k_fold(XGBRegressor(),dataset,headers,to_dummify,n_outputs)

print("*** PLS ***")
load_and_run.reg_k_fold(PLSRegression(),dataset,headers,to_dummify,n_outputs)

print("*** MLP ***")
load_and_run.reg_k_fold(MLPRegressor(),dataset,headers,to_dummify,n_outputs)