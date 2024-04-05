# -*- coding: utf-8 -*-
"""WXML SP24

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r8DipgLvT7pW7P0TaxDG841PKlrjNKFW

**TO DO:**
*   Change the size of the testing set from 0.4 to 0.3=>
*   Instead of having uniformly generated random, make it more structured (i.e., use normal distribution, columns that are not independent entirely)
*   The CCPAlpha in FAAFO (Part 1) will reduce overfitting (even though we want overfit, it would be nice to show no matter how much you try to generalise it is impossible to)
*   Fix the string datetime problem: https://towardsdatascience.com/machine-learning-with-datetime-feature-engineering-predicting-healthcare-appointment-no-shows-5e4ca3a85f96
*   One Hot Encoding: https://developer.nvidia.com/blog/three-approaches-to-encoding-time-information-as-features-for-ml-models/#:~:text=We%20can%20use%20the%20following,time%20feature%20into%20two%20features.&text=In%20the%20snippet%20below%2C%20we,using%20the%20sine%2Fcosine%20transformations.

*   https://medium.com/@swethalakshmanan14/simple-ways-to-extract-features-from-date-variable-using-python-60c33e3b0501

* https://cienciadedatos.net/documentos/py27-time-series-forecasting-python-scikitlearn.html

**Notes:** Maybe I did this completely wrong (specifically because I ask it to predict strings of time) but it memorizes a 100% of the time whether you give it (birth chart + random inputs) or (random inputs)
"""

import pandas as pd
import numpy as np

df = pd.read_csv("WXML_SP24_DF.csv")
df.head()

X = df.iloc[:, 1:-1]
y = df.iloc[:, 12]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 13, test_size = 0.2)

# X_train.shape, X_test.shape, y_train.shape, y_test.shape

from sklearn.tree import DecisionTreeClassifier

dtc = DecisionTreeClassifier()

dtc.get_params()

dtc.fit(X_train, y_train)

y_pred_train = dtc.predict(X_train)
y_pred_test = dtc.predict(X_test)

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

import warnings
warnings.filterwarnings("ignore")

print(classification_report(y_train, y_pred_train))

print(classification_report(y_test, y_pred_test))

print(confusion_matrix(y_train, y_pred_train))

print(confusion_matrix(y_test, y_pred_test))

dtc.feature_importances_

"""FAAFO Stuff (Part 1)"""

dtc.feature_importances_
#[0.08520323, 0.0847836 , 0.08183479, 0.08154077, 0.08993497,
      #  0.07459044, 0.06392073, 0.07256542, 0.06520508, 0.11528103,
      #  0.110025  , 0.07511494]

X.columns

features = pd.DataFrame(dtc.feature_importances_, index = X.columns)
features.head(15)

dtc2 = DecisionTreeClassifier(criterion = 'entropy', ccp_alpha = 0.10)

dtc2.fit(X_train, y_train)

y_pred2 = dtc.predict(X_test)

print(classification_report(y_test, y_pred2))

print(dtc2.feature_importances_)

"""FAAFO Stuff (Part 2)"""

df2 = pd.read_csv("WXML_SP24_DF.csv")
df2.drop(columns = ['Sun','Moon','Mercury','Venus','Mars','Jupiter','Saturn', 'Uranus', 'Neptune'])
df2.head()

X2= df.iloc[:, 10:-1]
y2 = df.iloc[:, 3]

X2.head()

y2.head()

X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, random_state = 13, test_size = 0.2)

dtc.fit(X2_train, y2_train)

y2_pred_train = dtc.predict(X2_train)
y2_pred_test = dtc.predict(X2_test)

print(classification_report(y2_train, y2_pred_train))

print(classification_report(y2_test, y2_pred_test))

dtc.feature_importances_