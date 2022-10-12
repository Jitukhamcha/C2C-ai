#%%
import numpy as np
from sklearn.linear_model import LogisticRegression

# %%
x=np.arange(10)
x=x.reshape(-1,1) #converting array to matrices
print(x)
# %%
y=np.array([0,1,0,1,1,0,1,0,1,1])

# %%
#now Modeling as datas already preprocessed
model=LogisticRegression()
model=model.fit(x,y)
# %%
print(model.classes_)
# %%
model.predict(x)
# %%
model.predict_proba(x)
# %%
model.predict_proba(np.array([[3.5]]))
# %%
plt.title('Logistics')
plt.grid()
plt.scatter(x,y)
plt.plot(x,model.predict(x),c='g')
# %%
