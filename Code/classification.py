# -*- coding: utf-8 -*-
"""[Class] DEFAULT

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lon23OLl8AHhNmvXAPdV1z9kO0hwSzq8
"""

import warnings
warnings.filterwarnings("ignore")

import math
import numpy as np
import global_variables
import load_and_run

import xgboost
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier

OUTPUT = global_variables.outputs[3]

import sys

orig_stdout = sys.stdout
f = open("results_"+OUTPUT+"(DRN).txt", 'w')
sys.stdout = f

# Use this to use all the variables
variables = global_variables.binarias+global_variables.categoricas+global_variables.numericas

# Use this for variable selection
# variables = ['ARISCAT procedimento emergente', 'ARISCAT anemia pré-operativa', 'morte (%)', 'pneumonia (%)', 'complicações sérias (%)', 'ACS - previsão dias internamento', 'qualquer complicação (%)', 'Discharge to Nursing or Rehab Facility (%)', '% mortalidade P-Possum', 'falência renal (%)', 'complicações cardíacas (%)', 'reoperação (%)', '% morbilidade P-Possum', 'tromboembolismo venoso (%)', 'Score gravidade cirúrgica P-Possum', 'Score fisiológico P-Possum', 'readmissão (%)', 'risco médio.11', 'ITU (%)', 'ARISCAT PONTUAÇÃO TOTAL', 'risco médio.12', 'risco médio', 'risco médio.1', 'risco médio.13', 'infeção cirúrgica (%)', 'risco médio.4', 'SCORE ARISCAT', 'risco médio.7']

dataset = load_and_run.load_data(OUTPUT,variables)

headers = dataset.columns
to_dummify = []
for i in range(0,len(headers)):
  if headers[i] in global_variables.categoricas:
    to_dummify.append(i)

dataset = dataset.to_numpy()
dataset[:,-1] = [str(x) for x in dataset[:,-1]]  # Unknown target type error solved!

print("*** Naive Bayes ***")
load_and_run.k_fold(GaussianNB(),dataset,headers,to_dummify)

print("*** KNN ***")
load_and_run.k_fold(KNeighborsClassifier(),dataset,headers,to_dummify)

print("*** DT ***")
load_and_run.k_fold(tree.DecisionTreeClassifier(),dataset,headers,to_dummify)

print("*** RF ***")
load_and_run.k_fold(RandomForestClassifier(),dataset,headers,to_dummify)

print("*** SVM ***")
load_and_run.k_fold(svm.SVC(probability=True),dataset,headers,to_dummify)

print("*** Logistic ***")
load_and_run.k_fold(LogisticRegression(),dataset,headers,to_dummify)

print("*** XGB ***")
load_and_run.k_fold(XGBClassifier(),dataset,headers,to_dummify)

print("*** MLP ***")
load_and_run.k_fold(MLPClassifier(),dataset,headers,to_dummify)