import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


data = {
    "TV_Ad_Spend": [230, 44, 17, 151, 180, 8, 57, 120, 199, 60],
    "Sales": [22, 10, 8, 18, 20, 5, 9, 15, 21, 11]
}
df = pd.DataFrame(data)

X = df[["TV_Ad_Spend"]]
Y = df["Sales"]


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

plt.figure(figsize=(6, 4))  
plt.scatter(X_test, y_test, color='blue', label='Actual Sales')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression Line')
plt.xlabel("TV Ad Spend")
plt.ylabel("Sales")
plt.legend()


plt.savefig("regression_plot.png", dpi=300) 
plt.show()