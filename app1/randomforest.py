import numpy as np
import pandas as pd

dataset = pd.read_csv('app1\Datasets\ckd_clean_16.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
temp = [[1.02,0,0,1,1,121,36,5,44,7800,5.2,0,0,1,1,1]]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Training the Random Forest Classification model on the Training set
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 20, criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)

# Predicting a new result
def randomforest_pred(temp):
    #temp = [[1.02,0,0,1,1,121,36,5,44,7800,5.2,0,0,1,1,1]]
    val = classifier.predict(sc.transform(temp))
    #print(val[0])
    return val[0]

"""
# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
print('Accuracy:',100 * accuracy_score(y_test, y_pred))
"""
result = randomforest_pred(temp)
print(result)