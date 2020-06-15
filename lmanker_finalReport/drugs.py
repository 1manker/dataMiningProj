from Simple import Simple
import pandas as pd
from sklearn.datasets import load_iris

def simplify(index):
	objs = []
	tars = []
	f = open("drug_consumption.data", "r")
	lines = f.readlines()
	for x in lines:
		x = x.split(',')
		if(float(x[1]) <= 0.49788): x[1] = "0" #less than 35
		else: x[1] = "1" #greater than 45
		if(float(x[2]) < 0): x[2] = "M"
		else: x[2] = "F"
		if(float(x[3]) <= -1.22751): x[3] = "DROPOUT"
		elif(float(x[3]) <= -0.05921): x[3] = "HIGHSCHOOL"
		else: x[3] = "COLLEGE"
		if(float(x[4]) == -0.09765): x[4] = "AUS"
		elif(float(x[4]) == 0.24923): x[4] = "CAN"
		elif(float(x[4]) == -0.46841): x[4] = "NZ"
		elif(float(x[4]) == 0.21128): x[4] = "IRE"
		elif(float(x[4]) == 0.96082): x[4] = "UK"
		elif(float(x[4]) == -0.57009): x[4] = "USA"
		else: x[4] = "OTHER"
		if(float(x[5]) == -0.50212): x[5] = "ASIAN"
		elif(float(x[5]) == -1.10702): x[5] = "BLACK"
		elif(float(x[5]) == -0.31685): x[5] = "WHITE"
		else: x[5] = "OTHER"
		if(float(x[6]) >= -2.52197): x[6] = "NOT_NEUROTIC"
		elif(float(x[6]) >= -2.05048): x[6] = "SLIGHTLY_NEUROTIC"
		elif(float(x[6]) >= -1.43907): x[6] = "NEUROTIC"
		else: x[6] = "VERY_NEUROTIC"
		if(float(x[7]) >= -2.72827): x[7] = "NOT_EXTRAVERTED"
		elif(float(x[7]) >= -2.21069): x[7] = "SLIGHTLY_EXTRAVERTED"
		elif(float(x[7]) >= -1.76250): x[7] = "EXTRAVERTED"
		else: x[7] = "VERY_EXTRAVERTED"
		if(float(x[8]) >= -2.39883): x[8] = "NOT_OPEN"
		elif(float(x[8]) >= -1.97495): x[8] = "SLIGHTLY_OPEN"
		elif(float(x[8]) >=  -1.55521): x[8] = "OPEN"
		else: x[8] = "VERY_OPEN"
		if(float(x[9]) >= -2.90161): x[9] = "NOT_AGGREEABLE"
		elif(float(x[9]) >= -2.53830): x[9] = "SLIGHTLY_AGGREEABLE"
		elif(float(x[9]) >= -2.07848): x[9] = "AGGREEABLE"
		else: x[9] = "VERY_AGGREEABLE"
		if(float(x[10]) >= -2.72827): x[10] = "NOT_CONSCIENTIOUS"
		elif(float(x[10]) >= -2.30408): x[10] = "SLIGHTLY_CONSCIENTIOUS"
		elif(float(x[10]) >=  -1.92173): x[10] = "CONSCIENTIOUS"
		else: x[10] = "VERY_CONSCIENTIOUS"
		if(float(x[11]) >= -0.71126): x[11] = "NOT_IMPULSIVE"
		elif(float(x[11]) >= 0.52975): x[11] = "SLIGHTLY_IMPULSIVE"
		elif(float(x[11]) >= 1.29221 ): x[11] = "IMPULSIVE"
		else: x[11] = "VERY_IMPULSIVE"
		if(float(x[12]) >= -1.18084): x[12] = "LOW_SENSATION"
		elif(float(x[12]) >= -0.21575): x[12] = "SLIGHT_SENSATION"
		elif(float(x[12]) >= 0.76540): x[12] = "AVG_SENSATION"
		else: x[12] = "HIGH_SENSATION"
		if(x[index] == ("CL0" or "CL1" or "CL2")): x[index] = 0
		elif(x[index] == ("CL3" or "CL4")): x[index] = 1
		else: x[index] = 2
		tempObj = Simple(x[1], x[2], x[3], x[4], x[5], x[6],
			x[7], x[8], x[9], x[10], x[11], x[12])
		objs.append(tempObj)
		tars.append(x[index])
	f.close()
	for x in objs:
		x.printToFile("coke.data")
	return tars

feature_names = ["age", "gender", "education", "country", "ethnicity", "nscore",
		"escore", "oscore", "ascore", "cscore", "impulse", "sensation"]

target_names = ["NOT_USER", "USER", "HEAVY_USER"]



target = simplify(22)
data = pd.read_csv("coke.data", header=[0])

X = pd.DataFrame(data, columns=feature_names)
#y = pd.Categorical.from_codes(target, target_names)
print(X.head())