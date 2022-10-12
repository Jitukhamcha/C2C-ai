#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
# %%
dataset=pd.read_csv('C:\\Users\\Ghost\\Desktop\\AIML\\c2c-ai\\CW-1\\Salary.csv')
# %%
print(dataset.head())
# %%
#For stats info
print(dataset.describe())
# %%
#Data preprocessing
x=dataset.iloc[:,:-1].values #remember iloc and loc[:,'column']
y=dataset.iloc[:,1].values
print(x)
print(y)
# %%
#split dataset
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
# %%
print(x_train.shape)
print(y_train.shape)
# %%
#now model Training/Fiting
regresser=LinearRegression()

# %%
model=regresser.fit(x_train,y_train)
# %%
print(model)
# %%
print(model.coef_)
print(model.intercept_)
# %%
#prediction
y_pred=model.predict(x_test)
print(y_pred)
print('******')
print(y_test)
# %%
#predict future
custom_value=np.array([[13],[300]])
print(model.predict(custom_value))
# %%
plt.title("Plot of Salary with Years of Experience")
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.scatter(x_train,y_train,c='b')
plt.scatter(x_test,y_test,c='r')
plt.plot(x_train,regresser.predict(x_train),c='g')
# %%
