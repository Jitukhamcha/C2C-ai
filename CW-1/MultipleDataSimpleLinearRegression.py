#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from mpl_toolkits import mplot3d
# %%
#multiple X
Md=pd.read_csv('C:\\Users\\Ghost\\Desktop\\AIML\\c2c-ai\\CW-1\\Salary_multiple.csv')

# %%
print(Md.head())

# %%
#preprocessing
Md.loc[:,'Field'].replace(['Technical','Non-Technical'],[0,1],inplace=True)
print(Md.describe)
# %%
#split x and y
x=Md.iloc[:,:-1].values
print(x)
y=Md.iloc[:,2].values
print(y)
# %%
#spliting dataset
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
# %%
#now model training fitting
MultRegresser=LinearRegression()
model=MultRegresser.fit(x_train,y_train)
print(x_train.shape)
print(y_train.shape)
# %%
print(model.coef_)
print(model.intercept_)
#%%
#now predicting values
custom_value=np.array([[13, 0],[300, 1]])
print(model.predict(custom_value))
#%%
#for plotting 
Years=[row[0] for row in x_train]
TechOrNot=[row[1] for row in x_train]
#Years=Years.reshape(-1,1)
print(Years)
# %%
#plotting
ax = plt.axes(projection='3d')
plt.title("Plot of Salary with Years of Experience")
ax.set_xlabel('Years of Experience')
ax.set_ylabel('Salary')
ax.set_zlabel('Tech or Non-Tech')
ax.scatter(Years,TechOrNot,y_train)
ax.plot3D(Years,TechOrNot,MultRegresser.predict(x_train),c='g')
# %%
