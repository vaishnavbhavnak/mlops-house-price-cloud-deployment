import os 
import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression

data=pd.DataFrame({
    "area":[800,1000,1200,1500,2000,2200,2500,3000],
    "bedrooms":[2,2,2,3,3,3,4,4],
    "age":[15,10,8,12,5,4,6,2],
    "price":[30,38,45,55,68,75,80,100]
})

X=data[["area","bedrooms","age"]]
y=data["price"]

model=LinearRegression()
model.fit(X,y)

os.makedirs("models",exist_ok=True)

with open("models/house_price_model.pkl","wb") as file:
    pickle.dump(model,file)
    
print("Model trained successfully and saved")
print("Training Score: ",model.score(X,y))