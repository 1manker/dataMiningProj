from Simple import Simple
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO 
from IPython.display import Image 
from pydot import graph_from_dot_data
import pandas as pd
import numpy as np
import os
import sys

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

def simplify(index, objs):
	tars = []
	f = open("drug_consumption.data", "r")
	lines = f.readlines()
	for x in lines:
		x = x.split(',')
		if(x[index] == ("CL0" or "CL1" or "CL2")): x[index] = 0
		elif(x[index] == ("CL3" or "CL4")): x[index] = 1
		else: x[index] = 2
		if(x[20] == ("CL0" or "CL1" or "CL2")): x[20] = 0
		else: x[20] = 1 
		tempObj = [float(x[1]),float(x[2]),float(x[3]),float(x[4]),float(x[5]),
		float(x[6]),float(x[7]),float(x[8]),float(x[9]),float(x[10]),float(x[11]),
		float(x[12]),float(x[20])]
		objs.append(tempObj)
		tars.append(x[index])
	f.close()
	return tars

# feature_names = ["age", "gender", "education", "country", "ethnicity", "nscore",
# 		"escore", "oscore", "ascore", "cscore", "impulse", "sensation"]

feature_names = ["age", "gender", "education", "country", "ethnicity", "nscore",
 		"escore", "oscore", "ascore", "cscore", "impulse", "sensation", 
 		"cokeUser"]

target_names = ["NOT_USER", "USER", "HEAVY_USER"]



data = []
target = simplify(23, data)



X = pd.DataFrame(data, columns=feature_names)
y = pd.Categorical.from_codes(target, target_names)
X.head()
y = pd.get_dummies(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7, 
	test_size=0.3, random_state=1)

dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)

dot_data = StringIO()
export_graphviz(dt, out_file=dot_data, feature_names=feature_names,
	class_names=target_names)
(graph, ) = graph_from_dot_data(dot_data.getvalue())
Image(graph.create_png())
#graph.write_png("crack.png")

y_pred = dt.predict(X_test)
sets = np.array(y_test).argmax(axis=1)
predictions = np.array(y_pred).argmax(axis=1)
matrix = confusion_matrix(sets, predictions)
print(matrix)
tp1 = matrix[0][0]
fp1 = matrix[1][0] + matrix[2][0]
fn1 = matrix[0][1] + matrix[0][2]
tn1 = matrix[1][1] + matrix[2][2]
prec1 = tp1/(tp1+fp1)
recall1 = tp1/(tp1+fn1)
f11 = 2*((prec1*recall1)/(prec1+recall1))
tp2 = matrix[1][1]
fp2 = matrix[0][1] + matrix[2][1]
fn2 = matrix[1][0] + matrix[1][2]
tn2 = matrix[0][0] + matrix[2][2]
prec2 = tp2/(tp2+fp2)
recall2 = tp2/(tp2+fn2)
f12 = 2*((prec2*recall2)/(prec2+recall2))
tp3 = matrix[2][2]
fp3 = matrix[0][2] + matrix[1][2]
fn3 = matrix[2][0] + matrix[2][1]
tn3 = matrix[0][0] + matrix[1][1]
prec3 = tp3/(tp3+fp3)
recall3 = tp3/(tp3+fn3)
f13 = 2*((prec3*recall3)/(prec3+recall3))
print("\nPrecision for NOT_USER: "+ str(prec1))
print("\nRecall for NOT_USER: "+ str(recall1))
print("\nF1-Score for NOT_USER: " + str(f11))
print("\nPrecision for USER: "+ str(prec2))
print("\nRecall for USER: "+ str(recall2))
print("\nF1-Score for USER: " + str(f12))
print("\nPrecision for HEAVY_USER: "+ str(prec3))
print("\nRecall for HEAVY_USER: "+ str(recall3))
print("\nF1-Score for HEAVY_USER: " + str(f13))
feat_importance = dt.tree_.compute_feature_importances(normalize=False)
print("\nfeat importance = " + str(feat_importance))