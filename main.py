import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style


df = pd.read_csv('main.csv')
df = df.T

i = 0
j=i+1
while i<6054:
	var1 = df[i]
	while j<6054:
		var2 = df[j]
		if(var1[0]==var2[0] and var1[2]==var2[2] and var1[3]==var2[3]):  
			df.drop(columns=j)
		j = j+1
	i = i+1
	j=i+1	



i = 0
j=i+1
while i<6054:
	var1 = df.iloc[i,:]
	while j<6054:
		var2 = df.iloc[j,:]
		if(var1[0]==var2[0] and var1[2]==var2[2] and var1[3]==var2[3]):
			print(df.iloc[i,:])
			df.set_value(i, 'Requirement', var1[4]+var2[4])
			df.set_value(i, 'Availability', var1[5]+var2[5]) 
			print(df.iloc[i,:])
			df.drop(j)
		j = j+1
	i = i+1	
print(df)




			